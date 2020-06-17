import pytest
import yaml

from pythoncode.cal import calc


@pytest.mark.parametrize('a,b', yaml.safe_load(open("./datadriver.yml")))
class Testcheck:
    @pytest.mark.dependency()
    @pytest.mark.run(order=1)
    def check_a(self, start, a, b):
        assert a + b == start.add(a, b)

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=["check_a"])
    def check_b(self, start, a, b):
        assert a - b == start.sub(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.dependency()
    def test_a(self, start, a, b):
        assert a * b == start.mul(a, b)

    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=["test_a"])
    def test_b(self, start, a, b):
        assert a / b == start.div(a, b)
