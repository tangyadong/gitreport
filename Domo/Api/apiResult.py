"""计数"""
count = 0
def api_return(value):
    global count
    count += 1
    print("执行数:"+str(count))
    print("接口地址:"+str(value.url))
    print("返回code:"+str(value.status_code))
    print("返回json:"+str(value.json()))
    print("返回ID:"+str(value.json()["request_id"]))
    # assert value.status_code == 200
    if value.status_code == 200:
        print("测试通过")
    else:
        print("测试未通过")
    print("-"*200)