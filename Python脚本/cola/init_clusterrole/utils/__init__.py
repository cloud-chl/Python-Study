import pkgutil
import importlib
import os

# 获取当前包路径
package_path = os.path.dirname(__file__)
package_name = __name__

# 动态导入 utils 下的所有模块
__all__ = []
for _, module_name, _ in pkgutil.iter_modules([package_path]):
    # 动态导入模块
    module = importlib.import_module(f".{module_name}", package=package_name)

    # 将模块中的所有公共成员（非以下划线开头）添加到 __all__
    for attr_name in dir(module):
        if not attr_name.startswith("_"):
            globals()[attr_name] = getattr(module, attr_name)
            __all__.append(attr_name)

# 去重
__all__ = list(set(__all__))
