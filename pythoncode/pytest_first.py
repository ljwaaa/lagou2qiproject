import pytest
import yaml


@pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("./datadriver.yml")))
class Testcal:
    def test_caseadd(self, start, a, b):
        assert a + b == start.add(a, b)

    def test_caseasub(self, start, a, b):
        assert a - b == start.sub(a, b)

    def test_caseamul(self, start, a, b):
        assert a * b == start.mul(a, b)

    def test_casediv(self, start, a, b):
        assert a / b == start.div(a, b)
