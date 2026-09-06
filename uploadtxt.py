import urllib3    # 导入urllib3模块
import json       # 导入json模块
with open('test.txt', 'r', encoding='utf-8') as f:    # 打开文本文件
  data = f.read()               # 读取文件
http = urllib3.PoolManager()    # 创建连接池管理对象
# 发送网络请求
r = http.request( 'POST','http://httpbin.org/post',fields={'filefield': ('example.txt', data),})
files = json.loads(r.data.decode('utf-8'))['files']  # 获取上传文件内容
print(files)                                         # 打印上传文本信息
