from fastapi import FastAPI
from routes import user_routes
from db import Base, engine
import models  # ensure models are registered with Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_routes.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
