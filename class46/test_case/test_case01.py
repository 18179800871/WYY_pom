
from class46.data_driver import yaml_driver
import pytest
# 需要数据的测试用例
@pytest.mark.parametrize(['user', 'password'], [('admin', '1234'), ('admin1')])
def test_login(user, password):
    if user and password:
        return '登录成功'
    return '登录失败'

# @pytest.mark.parametrize(['参数名', '参数名'], [('参数', '参数'), ('参数1', '参数1')])
# def test_login(参数名, 参数名):
#     if user and password:
#         return '登录成功'
#     return '登录失败'
# 装饰器的参数名需要与函数的参数名一致

if __name__ == '__main__':
    pytest.main(['-s'])



