import pymysql

# 环境
urlList = {
    "qa" : "www.qa-baidu.com",
    "prod":"www.prod-baidu.com"
}

# 数据库
sqlList01 = {
    "host" : "127.0.0.1",
    "username" : "root",
    "password" : "qwer1234",
    "db_name":"python_sql"
}
sqlList02 = {
    "host" : "127.0.0.2",
    "username" : "root",
    "password" : "qwer1234",
    "db_name":"python_sql"
}

# sql = sqlList01  # 切换数据库
# host = sql["host"]
# username = sql["username"]
# password = sql["password"]
# db_name = sql["db_name"]
# connect = pymysql.connect(host=host,user=username,password=password,db=db_name) # 配置信息
# cursor = connect.cursor() # 链接数据库
# 查询所有数据
# sql2 = "SELECT * FROM staff"
# cursor.execute(sql2)  # 执行sql
# connect.commit()  # 提交到数据库中执行
