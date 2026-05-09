import pytest


@pytest.fixture
def login_token():
    """模拟登录，返回token"""
    user_id = 1001
    token = "fake_token_" + str(user_id)
    return token


def test_with_token(login_token):
    """测试带token的请求"""
    assert login_token is not None
    assert "fake_token_" in login_token


def test_api_response_format():
    """测试API响应格式"""
    mock_response = {
        "code": 200,
        "message": "success",
        "data": {"user_id": 1001}
    }

    assert mock_response["code"] == 200
    assert mock_response["message"] == "success"
    assert "user_id" in mock_response["data"]


def test_api_error_handling():
    """测试API错误处理"""
    mock_error_response = {
        "code": 401,
        "message": "未授权"
    }

    assert mock_error_response["code"] != 200
    assert "未授权" in mock_error_response["message"]
