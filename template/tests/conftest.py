import pytest


@pytest.fixture(scope="module")
def dummy_fixture():
    return dict(msg="This is the dummy fixture")
