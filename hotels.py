from fastapi import Body, Query, APIRouter
from schemas.hotels import Hotels, HotelsPutch

router = APIRouter(prefix='/hotels', tags=["Отели"])


hotels_data_base = [{'id': 1, 'title': 'Sochi', 'name': "Сочи Плаза"},
          {'id': 2, 'title': 'Dubai','name':'Дубай Гранд Отель'},
          {'id': 3, 'title': 'Sochi', 'name': "Сочи Плаза"},
          {'id': 4, 'title': 'Sochi', 'name': "Сочи Плаза"},
          {'id': 5, 'title': 'Dubai','name':'Дубай Гранд Отель'},
          {'id': 6, 'title': 'Sochi', 'name': "Сочи Плаза"},
          {'id': 7, 'title': 'Sochi', 'name': "Сочи Плаза"},
          {'id': 8, 'title': 'Dubai','name':'Дубай Гранд Отель'},
          {'id': 9, 'title': 'Sochi', 'name': "Сочи Плаза"},
          {'id': 10, 'title': 'Sochi', 'name': "Сочи Плаза"},
          {'id': 11, 'title': 'Dubai','name':'Дубай Гранд Отель'},
          {'id': 12, 'title': 'Sochi', 'name': "Сочи Плаза"},
          ]


@router.get("/")
def func(id:int| None = Query(default=None, description="Id отеля"),
    title:str| None = Query(default=None, description="Название отеля"),
    page_size:int | None = Query(default=6, description="Размер пагинации для страницы"),
    page:int | None = Query(default=1, description="Нумерация страницы")
         ):

    hotels_ = []
    start_pagination, end_pagination = page_size*(page-1), page_size*page

    for hotel in hotels_data_base:
        if id and hotel['id'] != id:
            continue
        if title and hotel['title'] != title:
            continue

        hotels_.append(hotel)

    return(hotels_[start_pagination:end_pagination])

@router.post("/")
def add_hotel(hotel_data:Hotels = Body(openapi_examples={
    "1":{"summary":'Сочи',"value":{"title":"Сочи отель у моря", "name":"Sochi"}},
    "2":{"summary":'Дубай',"value":{"title":"Дубай отель у моря", "name":"Dubai"}},
    })):

    global hotels_data

    hotel = hotel_data.title
    id = hotels_data_base[-1]['id'] + 1


    hotels_data_base.append({'id' : id, 'title' : hotel})

    return {'Status': 'OK'}

@router.put("/{hotel_id}")
def put_hotels(hotel_id:int,hotel_data:Hotels):

    global hotels_data_base
    for i,hotel in enumerate(hotels_data_base):
        if hotel_id == hotel['id']:
            hotels_data_base[i] = {'id':hotel_id, 'title': hotel_data.title,
                         'name': hotel_data.name}
    return {'Status': 'OK'}

@router.patch("/{hotel_id}")
def patch_hotels(hotel_id:int,hotel_data:HotelsPutch):

    global hotels

    for i, hotel in enumerate(hotels_data_base):
        if hotel['id'] == hotel_id:
            if hotel_data.title: hotels[i]['title'] = hotel_data.title
            if hotel_data.name: hotels[i]['name'] = hotel_data.name

    return {'Status': 'OK'}


@router.delete("/{hotel_id}")
def delete_hotel(hotel_id:int):
    global hotels
    hotels = [hotel for hotel in hotels_data if hotel['id'] != hotel_id]

    return {'Status': 'OK'}


