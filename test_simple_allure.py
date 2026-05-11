
import allure
import pytest


@allure.feature('示例测试')
class TestExample:
    """Allure 示例测试类"""

    @allure.story('基本功能')
    @allure.title('测试加法运算')
    @allure.description('验证基本的加法运算是否正确')
    def test_addition(self):
        with allure.step('执行加法运算'):
            result = 2 + 3
        with allure.step('验证结果'):
            assert result == 5, f'期望结果为 5,实际为 {result}'

    @allure.story('基本功能')
    @allure.title('测试字符串操作')
    @allure.description('验证字符串拼接功能')
    def test_string_concatenation(self):
        with allure.step('拼接字符串'):
            result = 'Hello' + ' ' + 'World'
        with allure.step('验证结果'):
            assert result == 'Hello World'

    @allure.story('异常处理')
    @allure.title('测试异常抛出')
    @allure.description('验证异常情况下的错误处理')
    def test_exception(self):
        with allure.step('触发异常'):
            with pytest.raises(ValueError):
                raise ValueError('这是一个测试异常')