from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import requests
import datetime

router = Router()
    # Вариант через API Openweathermap
app_id = "f38b5807d4c9ff42c108f66d7fdb6633"
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.reply("Здравствуйте!\nОтправьте название города для получения текущей погоды")

@router.message()
async def get_weather(message: Message):
    city_to_find = message.text
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'q': city_to_find, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
    data = res.json()
    weather_in_city = (f"Сейчас в г.{city_to_find} {data['weather'][0]['description']}"
                       + '\n' + f"Температура: {int(data['main']['temp'])}°C")
    await message.reply(f"{datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}\n"+weather_in_city
    )

'''
    # Вариант через API Weatherstack
@router.message(Command("weather"))
async def cmd_start(message: Message):
    await message.reply("Здравствуйте!\nОтправьте название города на английском для получения текущей погоды")

@router.message()
async def get_weather(message: Message):
    #try:
    city_to_find = message.text
    url = "https://api.weatherstack.com/current?access_key=c000181d4b32272255eb67e584abeec5"
    querystring = {"query": f"{city_to_find}"}
    response = requests.get(url, params=querystring)
    data = response.json()

    await message.reply(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        f"Сейчас в городе {data['location']['name']} {data['current']['weather_descriptions'][0]}"
        f"\nТемпература: {data['current']['temperature']}°C"
    )
'''