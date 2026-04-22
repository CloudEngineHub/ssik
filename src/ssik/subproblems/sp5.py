"""Subproblem 5: three-rotation composition.

Given three unit axes ``k1, k2, k3``, four position vectors ``p0, p1, p2, p3``
and a target ``p``, find ``(theta1, theta2, theta3)`` such that::

    p0 + Rot(k1, theta1) [p1 + Rot(k2, theta2) [p2 + Rot(k3, theta3) p3]] == p

Up to 4 solutions in the generic feasible case.

**Status: not yet implemented.** SP5 reduces to a quartic polynomial in
``tan(theta3 / 2)`` after eliminating ``theta2`` and ``theta1`` via SP4 and
SP1 respectively. Substituting ``V(theta3) = p2 + Rot(k3, theta3) p3`` and
``q = p - p0`` yields two SP4-type equations in ``theta2`` (one from the
magnitude constraint ``|p1 + Rot(k2, theta2) V| = |q|``, one from the axial
projection ``k1 . (p1 + Rot(k2, theta2) V) = k1 . q``). Solving the pair
linearly for ``(cos theta2, sin theta2)`` and enforcing ``cos^2 + sin^2 = 1``
gives a polynomial equation in ``tan(theta3 / 2)`` of degree <= 4. The roots
of that polynomial are the candidate ``theta3`` values; each recovers
``theta2`` and then ``theta1 = SP1(k1, w, q)`` where ``w`` is the resulting
``p1 + Rot(k2, theta2) V``.

The closed-form polynomial derivation is nontrivial and deferred to the
follow-up Phase B.2 (see umbrella #37). Dispatcher solvers that need SP5
(certain tier-1 / tier-2 chain topologies) will not be unblocked until the
polynomial reduction lands.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

__all__ = ["solve"]


def solve(
    p0: NDArray[np.float64],
    p1: NDArray[np.float64],
    p2: NDArray[np.float64],
    p3: NDArray[np.float64],
    k1: NDArray[np.float64],
    k2: NDArray[np.float64],
    k3: NDArray[np.float64],
    p: NDArray[np.float64],
) -> tuple[list[tuple[float, float, float]], bool]:
    """SP5 is not yet implemented; see module docstring for the deferral note."""
    del p0, p1, p2, p3, k1, k2, k3, p  # keep the signature canonical
    raise NotImplementedError(
        "SP5 (three-rotation composition) is deferred to Phase B.2; "
        "see ssik.subproblems.sp5 module docstring for the polynomial-reduction "
        "plan and umbrella issue #37 for phase tracking."
    )
