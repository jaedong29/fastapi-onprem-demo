# FastAPI Onprem Demo

Python 3.12로 실행하는 작은 FastAPI 샘플입니다. DB나 외부 API 없이 동작합니다.

## 로컬 실행

```sh
git clone https://github.com/jaedong29/fastapi-onprem-demo.git
cd fastapi-onprem-demo
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m app.main
```

브라우저에서 http://localhost:8000 에 접속합니다. 종료는 Ctrl+C입니다.

- `/`: 실행 확인 화면
- `/healthz`: 상태 확인 JSON
- `/api/hello`: 인사 JSON
- `/docs`: API 문서

앱 진입점은 `app.main:app`입니다.
