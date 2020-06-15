import pytest

from pythoncode.cal import calc


@pytest.fixture(scope='function')
def start():
    calc1 = calc()
    print("开始计算")
    yield calc1
    print("计算结束")
