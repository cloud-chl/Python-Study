from fastapi import APIRouter
from typing import Union, Optional

app02 = APIRouter()

@app02.get('/jobs/{kd}')
# async def get_jobs(kd: str, xl: Union[str, None]=None, gj=None):
async def get_jobs(kd: str, xl: Optional[str], gj=None):
    # Union 是当有多种可能的数据类型时使用，比如函数有可能根据不同情况返回str或list，那么就可以写成Union[str, list]
    # Optional 是Union的一个简化，当数据类型中有可能是None时，比如有可能时str也有可能时None，则Optional[str]相当于Union[str, None]
    # 基于kd, xl, gj数据查询岗位信息
    return {
        "kd": "Software Engineer",
        "xl": "XYZ Corp.",
        "gj": "gj"
    }