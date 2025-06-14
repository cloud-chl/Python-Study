import logging
import traceback

logging.basicConfig(
    level=10,  # 设置日志级别
    format='%(asctime)s - %(name)s - %(levelname)s - %(modules)s: %(message)s',  # 设置日志格式
    datefmt='%m-%d-%Y %I:%M:%S',
    filename='app.log',  # 设置日志输出文件
    filemode='w'  # 设置文件模式，'w' 为覆盖写入，'a' 为追加写入
)

try:
    print(1/0)
except:
    print("error")
    logging.error(traceback.format_exc())