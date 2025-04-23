from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post("/bmicheck", response_class=HTMLResponse)
def bmi_show(name: str = Form(...), height: float = Form(...), weight: float = Form(...)):
    # BMI 계산
    bmi = weight / (height ** 2)

    # HTML 생성
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>bmi 측정하기</title>
        <link rel="stylesheet" href="bmi.css">
        <link href="https://fonts.googleapis.com/css2?family=Jua&display=swap" rel="stylesheet">
    </head>
    <body align="center">
    <table border="3" class="bmifont">
        <tr><td>이름</td><td>{name}</td></tr>
        <tr><td>키</td><td>{height} cm</td></tr>
        <tr><td>몸무게</td><td>{weight} kg</td></tr>
        <tr><td>BMI</td><td>{bmi:.2f}</td></tr>
        <tr><td>Profile</td><td>프로필 정보</td></tr>
    </table>
    </body>
    </html>
    '''
    return HTMLResponse(content=html)
