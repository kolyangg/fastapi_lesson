from fastapi import FastAPI, Path
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse

app = FastAPI()

@app.get("/")
def root():
    #return "Hello, student!"
    return {"message": "Hello, student!"}

@app.get("/add")
def add(x: int, y: int) -> int:
    return x + y

@app.get("/double/{number}")
def double(number: int) -> int:
    return number * 2

@app.get("/welcome/{name}")
def welcome(name: str = Path(min_length=2, max_length=20)) -> str:
    return f"Welcome, {name}!"

@app.get("phone/{number}")
def phone_number(number: str = Path(regex = "")):
    return {"phone": number}

@app.get("/text")
def get_text():
    content = "wfwfwfd fqwfw fwf we ggg"
    return PlainTextResponse(content = content)

'''
@app.get("/html")
def get_html():
    content = "<!DOCTYPE html> <html> <head> <meta charset='UTF-8'> <title> Document </title> </head> <body> <h1>Helloff!</h1> </body> </html>"
    return HTMLResponse(content)
'''

@app.get(path = "/html", response_class=HTMLResponse)
def get_html():
    content = "<!DOCTYPE html> <html> <head> <meta charset='UTF-8'> <title> Document </title> </head> <body> <h1>Helloff!</h1> </body> </html>"
    return HTMLResponse(content)




@app.get("/file")
def get_file():
    content = "index.html"
    return FileResponse(
        content, 
        media_type="application/octer-stream",
        filename="index.html"
    )