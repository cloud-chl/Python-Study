from typing import List
from fastapi import APIRouter, File, UploadFile
import os

app05 = APIRouter()

@app05.post("/file")
async def get_file(file: bytes = File()):
    # 适合小文件上传
    print("file",file)
    return {
        "file": len(file)
        }

@app05.post("/files")
async def get_files(files: List[bytes] = File()):
    # 适合小文件上传
    for file in files:
        print(len(file))

    return {
        "files": len(files)
    }

@app05.post("/uploadFile")
async def get_files(file: UploadFile):
    # 适合小文件上传
    print("file", file)
    path = os.path.join("img", file.filename)

    with open(path, 'wb') as f:
        for line in f:
            f.write(line)

    return {
        "files": file.filename
    }


@app05.post("/getuploadFile")
async def getUploadFiles(files: List[UploadFile]):
    print("files", files)

    return {
       "names": [ file.filename for file in files ]
    }