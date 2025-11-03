from fastapi import FastAPI,Query, Body
import uvicorn

app = FastAPI()

hotels = [{'id': 1, 'title': 'Sochi', 'name': "Сочи Плаза"},
          {'id': 2, 'title': 'Dubai','name':'Дубай Гранд Отель'}
          ]



@app.get("/hotels")
def func(id:int| None = Query(default=None, description="Id отеля"),
    title:str| None = Query(default=None, description="Название отеля")
         ):

    hotels_ = []

    for hotel in hotels:
        if id and hotel['id'] != id:
            continue
        if title and hotel['title'] != title:
            continue

        hotels_.append(hotel)

    return(hotels_)



@app.delete("/hotels/{hotel_id}")
def delete_hotel(hotel_id:int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel['id'] != hotel_id]

    return {'Status': 'OK'}

@app.post("/hotels")
def add_hotel(hotel_title:str = Body(embed=True)):
    global hotels

    hotel = hotel_title
    id = hotels[-1]['id'] + 1


    hotels.append({'id' : id, 'title' : hotel})

    return {'Status': 'OK'}


if __name__ == '__main__':
    uvicorn.run(app="main:app",reload=True, port=8002)


