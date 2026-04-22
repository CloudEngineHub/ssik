"""Stub contracts for the deferred :mod:`ssik.subproblems.sp5` and
:mod:`ssik.subproblems.sp6` solvers.

These subproblems require a polynomial-reduction derivation that is deferred
to a Phase B.2 follow-up (see umbrella #37). The modules exist and raise a
clear :exc:`NotImplementedError` so that dispatcher solvers that need them
fail loudly with a useful message rather than importing a missing symbol.
"""

from __future__ import annotations

import numpy as np
import pytest

from ssik.subproblems import sp5, sp6


def test_sp5_raises_not_implemented() -> None:
    p = np.array([0.0, 0.0, 0.0])
    k = np.array([0.0, 0.0, 1.0])
    with pytest.raises(NotImplementedError, match="SP5"):
        sp5.solve(p, p, p, p, k, k, k, p)


def test_sp6_raises_not_implemented() -> None:
    h = np.array([1.0, 0.0, 0.0])
    k = np.array([0.0, 0.0, 1.0])
    p = np.array([1.0, 0.0, 0.0])
    with pytest.raises(NotImplementedError, match="SP6"):
        sp6.solve(h, h, h, h, k, k, p, p, p, p, 0.0, 0.0)
