"""Integration smoke: hand-built UR5 chain + vendored IKFastSolver.

Marked ``slow`` — symbolic IK for a 6R arm runs on the order of seconds to
minutes and is not appropriate for the default CI pass. Opt in with
``pytest -m slow``.

This test's *only* goal is the issue #5 success criterion: the solver must
produce sympy output without crashing on a real chain fed through the shim.
Correctness validation against numerical ground truth belongs to #13.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.slow


def test_forward_kinematics_chain_runs() -> None:
    """Cheaper than a full IK solve: exercises *every* shim method the solver
    invokes on the chain (context manager, GetDOF, GetJointFromDOFIndex,
    GetChain, GetName, IsStatic, GetHierarchy*, Is{Revolute,Prismatic,Mimic},
    GetDOFIndex) without the combinatorial cost of ``generateIkSolver``.
    """
    from fixtures.ur5 import ur5_specs
    from ikfastpy._kinbody import build_kinbody
    from ikfastpy._vendor.ikfast import IKFastSolver

    kb = build_kinbody(ur5_specs())
    solver = IKFastSolver(kinbody=kb)
    chainlinks = kb.GetChain("base_link", "ee_link", returnjoints=False)
    chainjoints = kb.GetChain("base_link", "ee_link", returnjoints=True)
    links_raw, jointvars = solver.forwardKinematicsChain(chainlinks, chainjoints)

    # Six revolute joints → six joint variables, seven link transforms.
    assert len(jointvars) == 6
    assert len(links_raw) >= 1


def test_generate_ik_solver_produces_output() -> None:
    """Full issue #5 criterion: ``generateIkSolver`` returns sympy output.

    Uses Translation3D (3-DOF solve with the last three joints free) so it
    completes in a reasonable wall time while still exercising the full
    generate → solve pipeline. A Transform6D solve on UR5 with no free
    joints can take many minutes and is orthogonal to the "does the shim
    work" question this test is answering.
    """
    from fixtures.ur5 import ur5_specs
    from ikfastpy._kinbody import build_kinbody
    from ikfastpy._vendor.ikfast import IKFastSolver

    kb = build_kinbody(ur5_specs())
    solver = IKFastSolver(kinbody=kb)
    chaintree = solver.generateIkSolver(
        baselink="base_link",
        eelink="ee_link",
        freeindices=[3, 4, 5],
        solvefn=IKFastSolver.solveFullIK_Translation3D,
    )
    assert chaintree is not None
