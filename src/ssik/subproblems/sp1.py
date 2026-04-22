"""Subproblem 1: rotate a vector to match another vector.

Given a unit axis ``k``, a vector ``p``, and a target vector ``q``, find the
angle ``theta`` such that::

    Rot(k, theta) @ p == q

Exact solution exists iff ``|p| == |q|`` and ``k . p == k . q``. Otherwise the
function returns the least-squares optimum: the angle that minimises
``|Rot(k, theta) p - q|^2``. The LS form continuously extends the exact one.

**Solution count:** always exactly 1 (exact or LS), so the return type is a
scalar ``theta`` plus an ``is_ls`` flag.

**Derivation.** Decompose ``p = (k.p)k + p_perp`` where ``p_perp`` is the
component of ``p`` perpendicular to ``k``; similarly for ``q``. Rotating ``p``
around ``k`` leaves ``(k.p)k`` unchanged and rotates ``p_perp`` in the plane
spanned by ``p_perp`` and ``k x p_perp``. Matching ``q_perp``::

    cos(theta) = (p_perp . q_perp) / |p_perp|^2
    sin(theta) = ((k x p_perp) . q_perp) / |p_perp|^2

So ``theta = atan2((k x p) . q, p . q - (k.p)(k.q))`` where we dropped the
axial components inside the dot products since they cancel after projection.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

__all__ = ["solve"]


def solve(
    k: NDArray[np.float64],
    p: NDArray[np.float64],
    q: NDArray[np.float64],
) -> tuple[float, bool]:
    """Solve SP1.

    :param k: unit rotation axis, shape ``(3,)``.
    :param p: vector to rotate, shape ``(3,)``.
    :param q: target vector, shape ``(3,)``.
    :returns: ``(theta, is_ls)`` where ``theta`` is the solution angle in
        radians and ``is_ls`` is ``True`` when the exact feasibility
        conditions do not hold (so ``theta`` is the LS optimum).
    """
    kxp = np.cross(k, p)
    kp = float(np.dot(k, p))
    kq = float(np.dot(k, q))
    theta = float(np.arctan2(np.dot(kxp, q), np.dot(p, q) - kp * kq))

    # Feasibility check: |p_perp| = |q_perp| and k.p = k.q. Equivalently
    # |p| = |q| and k.p = k.q (the axial components cancel in the LS
    # analysis but differ in raw magnitude -- use the projected form).
    p_perp_sq = float(np.dot(p, p)) - kp * kp
    q_perp_sq = float(np.dot(q, q)) - kq * kq
    is_ls = abs(p_perp_sq - q_perp_sq) > 1e-9 or abs(kp - kq) > 1e-9
    return theta, is_ls
