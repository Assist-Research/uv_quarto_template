import pytest  # noqa: F401


def test_dummy(dummy_fixture):
    assert dummy_fixture["msg"] == "This is the dummy fixture"
