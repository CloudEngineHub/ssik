"""Subproblem 6: two coupled SP4-like equations in two unknowns.

Given axes ``k1, k2``, direction pairs ``(h1, h2, h3, h4)``, vector pairs
``(p1, p2, p3, p4)``, and scalars ``d1, d2``, find ``(theta1, theta2)`` such
that::

    h1 . Rot(k1, theta1) p1 + h2 . Rot(k2, theta2) p2 == d1
    h3 . Rot(k1, theta1) p3 + h4 . Rot(k2, theta2) p4 == d2

Up to 4 solutions in the generic feasible case.

**Status: not yet implemented.** Each equation is linear in
``(cos theta1, sin theta1, cos theta2, sin theta2)`` after Rodrigues
expansion. Substituting ``t_i = tan(theta_i / 2)`` and clearing denominators
produces two polynomial equations in ``(t1, t2)``, each of degree <= 2 per
variable. By Bezout, up to 4 common roots. Eliminating ``t2`` via Sylvester
resultant gives a quartic in ``t1`` whose real roots can be recovered with
``numpy.roots``; each root recovers a corresponding ``t2`` via linear
back-substitution.

The derivation is deferred to the follow-up Phase B.2 (see umbrella #37)
alongside SP5. Dispatcher solvers that need SP6 will be blocked until then.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

__all__ = ["solve"]


def solve(
    h1: NDArray[np.float64],
    h2: NDArray[np.float64],
    h3: NDArray[np.float64],
    h4: NDArray[np.float64],
    k1: NDArray[np.float64],
    k2: NDArray[np.float64],
    p1: NDArray[np.float64],
    p2: NDArray[np.float64],
    p3: NDArray[np.float64],
    p4: NDArray[np.float64],
    d1: float,
    d2: float,
) -> tuple[list[tuple[float, float]], bool]:
    """SP6 is not yet implemented; see module docstring for the deferral note."""
    del h1, h2, h3, h4, k1, k2, p1, p2, p3, p4, d1, d2
    raise NotImplementedError(
        "SP6 (coupled SP4 pair) is deferred to Phase B.2; "
        "see ssik.subproblems.sp6 module docstring for the polynomial-reduction "
        "plan and umbrella issue #37 for phase tracking."
    )
