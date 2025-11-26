import asyncio
import threading
import time

from fastapi import FastAPI
import uvicorn

app = FastAPI(docs_url=False)

@app.get('/sync/{id}')
def sinc_func(id:int):
    print("Активных потоков:", threading.active_count())
    print(f" sinc Функция {id} начала свою работу")
    time.sleep(3)
    print(f" sinc Функция {id} Завершила свою работу")

@app.get('/async/{id}')
async def async_func(id:int):
    print("Активных потоков:", threading.active_count())
    print(f" async Функция {id} начала свою работу")
    await asyncio.sleep(3)
    print(f" async Функция {id} Завершила свою работу")
    return {'Status':'OK'}

if __name__ == '__main__':
    uvicorn.run(app="main:app",reload=False, workers= 5, port=8002)
