import requests
from bs4 import BeautifulSoup
import folium


def read_data(users_data: list) -> None:
    for user in users_data:
        print(
            f'twój znajomy {user['username']} z miejscowości {user['location']} opubikował {user['posts']} wiadomości. Ostatnia wiadomość {user['usermessage'][-1]}')


def add_user(users_data: list) -> None:
    name = input('Podaj imie: ')
    location = input('Podaj lokalizację: ')
    posts = int(input('Podaj liczbę postów: '))
    usermessage = ['']
    users_data.append({'username': name, 'location': location, 'posts': posts,
                       'usermessage': usermessage})


def remove_user(users_data: list) -> None:
    name = input('Podaj imie użytownika do usunięcia: ')

    for user in users_data:
        if user['username'] == name:
            users_data.remove(user)


def update_user(users_data: list) -> None:
    name = input('Podaj imie użytkownika do zmiany: ')

    for user in users_data:
        if user['username'] == name:
            user['username'] = input('Podaj nowe imie: ')
            user['location'] = input('Podaj nową lokalizację: ')
            user['posts'] = int(input('Podaj liczbę postów: '))


def get_coordinates(location: str) -> list:
    url = f"https://pl.wikipedia.org/wiki/{location}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers=headers)
    response_html = BeautifulSoup(response.text, 'html.parser')
    response_html_latitude = float(response_html.select('.latitude')[1].text.replace(",", "."))
    response_html_longitude = float(response_html.select('.longitude')[1].text.replace(",", "."))
    return [response_html_latitude, response_html_longitude]


users: list = [
    {"username": "oliwia", "location": "łódź", "posts": "1", "usermessage": ["kocham legie", "sprzedam opla", "kiwi"]},
    {"username": "paweł", "location": "ostróda", "posts": "2", "usermessage": ["kocham legie1", "sprzedam opla1", ]},
    {"username": "eliza", "location": "radom", "posts": "3", "usermessage": ["kocham legie2", ]},
    {"username": "filip", "location": "dęblin", "posts": "4",
     "usermessage": ["kocham legie3", "sprzedam opla3", "kiwi3"]},
]


def get_mapa(users_data: list) -> None:
    m = folium.Map([52, 21], zoom_start=12)
    for user in users:
        folium.Marker(
            location=get_coordinates(user["location"]),
            tooltip="Click me!",
            popup=user['username'],
            icon=folium.Icon(icon="cloud"),
        ).add_to(m)

    m.save("mapa.html")
