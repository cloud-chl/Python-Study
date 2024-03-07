from flask import Flask, render_template, redirect, url_for
from werkzeug.routing import BaseConverter


app = Flask(__name__)


class RegexConverter(BaseConverter):
    """
    自定义URL匹配正则表达式
    """

    def __init__(self, map, regex):
        super(RegexConverter, self).__init__(map)
        self.regex = regex

    def to_python(self, value):
        """
        路由匹配时，匹配成功后传递给视图函数中参数的值
        :param value:
        :return:
        """
        return int(value)

    def to_url(self, value):
        """
        使用url_for反向生成URL时，传递的参数经过该方法处理，返回的值用于生成URL中的参数
        :param value:
        :return:
        """
        val = super(RegexConverter, self).to_url(value)
        return val


# 添加到flask中
app.url_map.converters["xxx"] = RegexConverter


@app.route('/index/<xxx("\d+"):nid>', methods=["GET", "POST"])
def index(nid):
    print(nid, type(nid))
    v=url_for("index", nid=999)
    print(v)
    return "Index"


if __name__ == "__main__":
    app.run()
