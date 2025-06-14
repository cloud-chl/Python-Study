
# 常用的颜色代码
BLACK = "30"
RED = "31"
GREEN = "32"
YELLOW = "33"
BLUE = "34"
MAGENTA = "35"
CYAN = "36"
WHITE = "37"

def print_color_text(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")