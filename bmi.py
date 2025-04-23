from uuid import uuid4
from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import FileResponse, HTMLResponse
import os

from fastapi.staticfiles import StaticFiles

app = FastAPI()
# css파일을 html에 써둬도 정적 파일 처리를 안해두면 테마가 적용되지 않음
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/bmicheck", response_class=HTMLResponse)
# 비동기 함수 정의 
async def bmi_show(psa: UploadFile, name: str = Form(...), height: float = Form(...), weight: float = Form(...)):
    # 저장할 폴더 이름 설정
    folder = "./user_image/" 
    # 업로드된 파일 내용 읽기
    content = await psa.read() 
    # 확장자만 추출
    fileName = psa.filename
    type = fileName[-4:]
    fileName = fileName.replace(type, "") 
    # 파일 고유 이름 만들어주기
    fileName = fileName + str(uuid4()) + type
    # 바이너리 쓰기모드로 파일열기
    f = open(folder + fileName, "wb")
    # 파일 저장
    f.write(content)
    f.close()

    # bmi 계산
    h = height / 100
    bmi = weight / (h * h)
    result = "ㅋ"
    if bmi >= 39:
        result = "고도 비만"
    elif bmi >= 32:
        result = "중도 비만"

    # HTML 생성
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>bmi 측정하기</title>
        <link rel="stylesheet" href="/static/bmi.css">
        <link href="https://fonts.googleapis.com/css2?family=Jua&display=swap" rel="stylesheet">
    </head>
    <body align="center">
    
    <table border="3" class="bmifont" align="center">
        <tr><td>이름</td><td>{name}</td></tr>
        <tr><td>키</td><td>{height} cm</td></tr>
        <tr><td>몸무게</td><td>{weight} kg</td></tr>
        <tr><td>BMI</td><td>{bmi:.2f}</td></tr>'''
    
    html+="<tr><td>Profile</td><td><img src=\"file.get?fname=%s\"><br></td></tr>"% fileName
    html+="</table></body></html>"
    
    return HTMLResponse(content=html)

# 서버에서 데이터를 불러오는거는 get함수사용
@app.get("/file.get")
async def fileGet(fname: str):
    folder = "./user_image/"
    # 파일에 들어가서 내가 방금 저장한 사진 찾고
    file_path = os.path.join(folder, fname)
    # 브라우저에 해당 파일 불러오기
    return FileResponse(file_path, filename=fname)