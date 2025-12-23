# Trade Opportunities API

## Setup
```bash
pip install fastapi uvicorn httpx
```

## Run
```bash
uvicorn app.main:app --reload
```

## Authentication
Send header:
X-API-Key: CHANGE_ME

## Endpoint
GET /analyze/{sector}

pharmaceuticals
my_secret_key_123