import pytest

from pythoncode.cal import calc


@pytest.fixture(scope='function')
def start():
    calc1 = calc()
    print("开始计算")
    yield calc1
    print("计算结束")
# --------------------------------------------------------------------------------------------------------------\
import yaml

# def pytest_addoption(parser):
#     mygroup = parser.getgroup("myconfig")
#     mygroup.addoption("--env",
#                       default='test',
#                       dest='env',
#                       help='run env'
#
#                       )


# @pytest.fixture(scope='session')
# def cmdoption(request):
#     myenv = request.config.getoption("--env", default='test')
#     if myenv == 'test':
#         with open("datas/test/test.yml") as f:
#             datas1 = yaml.safe_load(f)
#     elif myenv == 'dev':
#         with open("datas/dev/dev.yml") as f:
#             datas1 = yaml.safe_load(f)
#     elif myenv == 'st':
#         with open("datas/st/st.yml") as f:
#             datas1 = yaml.safe_load(f)
#     return datas1
