from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import pandas as pd
import os
df = pd.read_excel(os.getenv('sheet'))

df.fillna('', inplace=True)

for i in df.columns:
    df[i] = df[i].apply(lambda x: str(x).replace('\n', '<br>'))

# 4. FastAPI 앱 생성
app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get("/")
def index(request: Request):
    table_html = df.to_html(escape=False, index=False, border=1)
    return templates.TemplateResponse("index.html", {"request": request, "table": table_html})
