from fastapi import FastAPI

app = FastAPI(title="OweU")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}