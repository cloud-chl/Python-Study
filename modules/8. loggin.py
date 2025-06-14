import logging

# 配置日志
logging.basicConfig(
    level=10,  # 设置日志级别
    format='%(asctime)s - %(name)s - %(levelname)s - %(modules)s: %(message)s',  # 设置日志格式
    datefmt='%m-%d-%Y %I:%M:%S',
    filename='app.log',  # 设置日志输出文件
    filemode='w'  # 设置文件模式，'w' 为覆盖写入，'a' 为追加写入
)

# 记录日志
logging.debug('这是一个调试信息')
logging.info('这是一个普通信息')
logging.warning('这是一个警告信息')
logging.error('这是一个错误信息')
logging.critical('这是一个严重错误信息')

# 记录到不同文件
import logging

# 配置模块1的 Logger
logger_module1 = logging.getLogger('module1')
logger_module1.setLevel(logging.DEBUG)

# 为模块1创建 DEBUG 级别的处理器
module1_debug_handler = logging.FileHandler('module1_debug.log')
module1_debug_handler.setLevel(logging.DEBUG)

# 为模块1创建 ERROR 级别的处理器
module1_error_handler = logging.FileHandler('module1_error.log')
module1_error_handler.setLevel(logging.ERROR)

# 配置模块2的 Logger
logger_module2 = logging.getLogger('module2')
logger_module2.setLevel(logging.DEBUG)

# 为模块2创建 DEBUG 级别的处理器
module2_debug_handler = logging.FileHandler('module2_debug.log')
module2_debug_handler.setLevel(logging.DEBUG)

# 为模块2创建 ERROR 级别的处理器
module2_error_handler = logging.FileHandler('module2_error.log')
module2_error_handler.setLevel(logging.ERROR)

# 创建日志格式器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 将格式器添加到处理器
module1_debug_handler.setFormatter(formatter)
module1_error_handler.setFormatter(formatter)
module2_debug_handler.setFormatter(formatter)
module2_error_handler.setFormatter(formatter)

# 将处理器添加到各自的 Logger
logger_module1.addHandler(module1_debug_handler)
logger_module1.addHandler(module1_error_handler)
logger_module2.addHandler(module2_debug_handler)
logger_module2.addHandler(module2_error_handler)

# 记录日志
logger_module1.debug('这是模块1的调试信息')  # 记录到 module1_debug.log
logger_module1.error('这是模块1的错误信息')  # 记录到 module1_error.log
logger_module2.debug('这是模块2的调试信息')  # 记录到 module2_debug.log
logger_module2.error('这是模块2的错误信息')  # 记录到 module2_error.log