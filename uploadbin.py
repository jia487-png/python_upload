import urllib3    # 导入urllib3模块
with open('python.jpg','rb') as f:  # 打开图片文件
  data = f.read()                    # 读取文件
http = urllib3.PoolManager()    # 创建连接池管理对象
# 发送请求
r = http.request('POST','http://httpbin.org/post',body = data,headers={'Content-Type':'image/jpeg'})
print(r.data.decode())          # 打印返回结果
