from utils.arrs import my_slice, get
import pytest


@pytest.fixture
def coll1():
    return [1, 2, 3], 1, "test"


@pytest.fixture
def coll2():
    return [], -1, "test"


def test_get_first(coll1):
    assert get(coll1[0], coll1[1], coll1[2]) == 2


def test_get_second(coll2):
    assert get(coll2[0], coll2[1], coll2[2]) == "test"


@pytest.fixture
def coll3():
    return [1, 2, 3, 4], 1, 3


@pytest.fixture
def coll4():
    return [1, 2, 3], 1


@pytest.fixture
def coll5():
    return [], 1, 4


@pytest.fixture
def coll6():
    return [1, 2, 3], -4


@pytest.fixture
def coll7():
    return [1, 2, 3], -1


def test_my_slice_first(coll3):
    assert my_slice(coll3[0], coll3[1], coll3[2]) == [2, 3]


def test_my_slice_second(coll4):
    assert my_slice(coll4[0], coll4[1]) == [2, 3]


def test_my_slice_third(coll5):
    assert my_slice(coll5[0], coll5[1], coll5[2]) == []


def test_my_slice_fourth(coll6):
    assert my_slice(coll6[0], coll6[1]) == [1, 2, 3]


def test_my_slice_fifth(coll7):
    assert my_slice(coll7[0], coll7[1]) == [3]
