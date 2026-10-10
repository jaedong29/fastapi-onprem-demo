import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Bronze Onprem Demo")


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Bronze Onprem Demo</title>
  <style>
    body { font-family: system-ui, sans-serif; background: #f4f6f8;
           color: #16202c; margin: 0; padding: 48px 24px; }
    main { max-width: 560px; margin: 0 auto; padding: 32px;
           background: white; border-radius: 16px; }
    a { color: #165bd8; }
  </style>
</head>
<body>
  <main>
    <h1>Bronze Onprem Demo</h1>
    <p>FastAPI 앱이 실행 중입니다.</p>
    <p><a href="/healthz">상태 확인</a> · <a href="/docs">API 문서</a></p>
  </main>
</body>
</html>"""


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/hello")
def hello() -> dict[str, str]:
    return {"message": "Hello from FastAPI!"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
