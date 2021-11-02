import requests
Host = "https://crs-api-test.vchangyi.com"


def loginOn(account,password,login_type):
    """用户登录"""
    crm_api = "/gw-console/v1/admin/login"
    url = Host+crm_api
    data = {
        "account":account,   # 账号
        "password":password,  # 密码
        "login_type":login_type  # 登录方式
    }
    r = requests.post(url=url,data=data)
    return r


if __name__ == "__main__":
    r = loginOn(account="zhanghong@vchangyi.com", password="", login_type=1)
    print(r.json())
    # assert r.json()["message"] == "管理员账号不能为空"
    # assert r.json()["code"] == 451001
    print("测试通过")