"""Shared Rodrigues rotation helper for the subproblem solvers.

Kept private (underscore-prefixed) and internal to the subproblems package.
If another package needs rotations later we will move this to
:mod:`ssik.kinematics` -- for now keeping it here avoids one more public
surface point to maintain.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

__all__ = ["rotate"]


def rotate(k: NDArray[np.float64], theta: float, v: NDArray[np.float64]) -> NDArray[np.float64]:
    """Rotate vector ``v`` by angle ``theta`` about unit axis ``k`` (Rodrigues).

    ``rotate(k, theta, v) = v cos(theta) + (k x v) sin(theta) + k (k . v) (1 - cos(theta))``
    """
    c = float(np.cos(theta))
    s = float(np.sin(theta))
    kv = float(np.dot(k, v))
    return v * c + np.cross(k, v) * s + k * (kv * (1.0 - c))
