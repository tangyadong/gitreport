# -*- coding:utf-8 -*-
import unittest
import HTMLTestReportCN
import apiList
import datetime
import apiResult


# 测试用例
class login(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 账号名为空登录
    def testLoginon01(self):
        r = apiList.loginOn(account="", password="ad3b697fbe36b598f42a21b11c4255ff", login_type=1)
        apiResult.api_returnAll(r)
        assert r.json()["message"] == "管理员账号不能为空"
        assert r.json()["code"] == 451001

    # 密码为空登录
    def testLoginon02(self):
        r = apiList.loginOn(account="zhanghong@vchangyi.com", password="", login_type=1)
        apiResult.api_returnAll(r)
        assert r.json()["message"] == "管理员密码不能为空"
        assert r.json()["code"] == 451002


# class APITestCase(unittest.TestCase):
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass
#
#     def testCase1(self):
#         pass


# 添加Suite
def Suite():
    # 定义一个单元测试容器
    suiteTest = unittest.TestSuite()
    # 将测试用例加入到容器
    suiteTest.addTest(login("testLoginon01"))
    suiteTest.addTest(login("testLoginon02"))
    return suiteTest


if __name__ == "__main__":
    # 确定生成报告的路径
    dt1 = datetime.datetime.now().date()
    filePath = 'C:\\Users\\tangyadong\\Desktop\\work\\gitreport\\test01\\gitreport\\Domo\\report\\'+str(dt1)+'login_case''.html'
    print(filePath)
    fp = open(filePath, 'wb+')
    # 生成报告的Title,描述
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='自动化测试报告',
        # description='详细测试用例结果',
        tester='useName'
    )
    # 运行测试用例
    runner.run(Suite())
    # 关闭文件，否则会无法生成文件
    fp.close()
