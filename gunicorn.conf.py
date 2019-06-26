import multiprocessing

bind = "127.0.0.1:8000"  # 绑定的ip与端口
workers = 2  # 核心数
errorlog = '/pycharm/DJANGOAPI/gunicorn.error.log'  # 发生错误时log的路径
accesslog = '/pycharm/DJANGOAPI/gunicorn.access.log'  # 正常时的log路径
# loglevel = 'debug'   #日志等级
proc_name = 'DJANGOAPI_gun'  # 进程名
