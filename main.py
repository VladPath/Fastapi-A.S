from fastapi import FastAPI
import uvicorn

from hotels import router as hotel_router

app = FastAPI()

app.include_router(hotel_router)


if __name__ == '__main__':
    uvicorn.run(app="main:app",reload=True, port=8002)