import ikfastpy


def test_version_is_present() -> None:
    assert isinstance(ikfastpy.__version__, str)
    assert ikfastpy.__version__
