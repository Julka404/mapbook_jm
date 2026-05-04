import requests
from bs4 import BeautifulSoup
import folium
from urllib.parse import quote


def read_data(users_data: list) -> None:
    for user in users_data:
        print(
            f"Twój znajomy {user['username']} z miejscowości {user['location']} "
            f"opublikował {user['posts']} wiadomości. "
            f"Ostatnia wiadomość: {user['usermessage'][-1]}"
        )


def add_user(users_data: list) -> None:
    name = input("Podaj imię: ")
    location = input("Podaj lokalizację: ")
    posts = int(input("Podaj liczbę postów: "))

    usermessage = [""]

    users_data.append({
        "username": name,
        "location": location,
        "posts": posts,
        "usermessage": usermessage
    })

    print("Dodano użytkownika.")


def remove_user(users_data: list) -> None:
    name = input("Podaj imię użytkownika do usunięcia: ")

    for user in users_data:
        if user["username"] == name:
            users_data.remove(user)
            print("Usunięto użytkownika.")
            return

    print("Nie znaleziono użytkownika.")


def update_user(users_data: list) -> None:
    name = input("Podaj imię użytkownika do zmiany: ")

    for user in users_data:
        if user["username"] == name:
            user["username"] = input("Podaj nowe imię: ")
            user["location"] = input("Podaj nową lokalizację: ")
            user["posts"] = int(input("Podaj liczbę postów: "))

            print("Zmieniono dane użytkownika.")
            return

    print("Nie znaleziono użytkownika.")


def get_coordinates(location: str) -> list:
    location_url = quote(location.replace(" ", "_"))
    url = f"https://pl.wikipedia.org/wiki/{location_url}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    response_html = BeautifulSoup(response.text, "html.parser")

    latitude = response_html.select(".latitude")
    longitude = response_html.select(".longitude")

    if len(latitude) < 1 or len(longitude) < 1:
        raise ValueError(f"Nie znaleziono współrzędnych dla lokalizacji: {location}")

    latitude_value = float(latitude[0].text.replace(",", "."))
    longitude_value = float(longitude[0].text.replace(",", "."))

    return [latitude_value, longitude_value]


def get_mapa(users_data: list) -> None:
    mapa = folium.Map(location=[52, 19], zoom_start=6)

    for user in users_data:
        try:
            coordinates = get_coordinates(user["location"])

            folium.Marker(
                location=coordinates,
                tooltip="Kliknij mnie",
                popup=user["username"],
                icon=folium.Icon(icon="cloud"),
            ).add_to(mapa)

        except Exception as error:
            print(f"Nie udało się pobrać współrzędnych dla: {user['location']}")
            print(f"Błąd: {error}")

    mapa.save("mapa.html")
    print("Mapa została zapisana jako mapa.html")