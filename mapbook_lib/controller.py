import folium


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
        if user["username"].lower() == name.lower():
            users_data.remove(user)
            print("Usunięto użytkownika.")
            return

    print("Nie znaleziono użytkownika.")


def update_user(users_data: list) -> None:
    name = input("Podaj imię użytkownika do zmiany: ")

    for user in users_data:
        if user["username"].lower() == name.lower():
            user["username"] = input("Podaj nowe imię: ")
            user["location"] = input("Podaj nową lokalizację: ")
            user["posts"] = int(input("Podaj liczbę postów: "))

            print("Zmieniono dane użytkownika.")
            return

    print("Nie znaleziono użytkownika.")


def get_coordinates(location: str) -> list | None:
    coordinates = {
        "łódź": [51.7592, 19.4560],
        "lodz": [51.7592, 19.4560],
        "ostróda": [53.6967, 19.9649],
        "ostroda": [53.6967, 19.9649],
        "radom": [51.4027, 21.1471],
        "dęblin": [51.5591, 21.8483],
        "deblin": [51.5591, 21.8483],
        "lublin": [51.2465, 22.5684],
        "warszawa": [52.2297, 21.0122],
        "gdynia": [54.5189, 18.5305],
        "konin": [52.2230, 18.2511],
    }

    location_key = location.strip().lower()

    return coordinates.get(location_key)


def get_mapa(users_data: list) -> None:
    mapa = folium.Map(location=[52.0, 19.0], zoom_start=6)

    for user in users_data:
        coordinates = get_coordinates(user["location"])

        if coordinates is None:
            print(f"Brak współrzędnych dla miejscowości: {user['location']}")
            continue

        folium.Marker(
            location=coordinates,
            tooltip="Kliknij mnie",
            popup=f"{user['username']} - {user['location']}",
            icon=folium.Icon(icon="cloud"),
        ).add_to(mapa)

    mapa.save("mapa.html")
    print("Mapa została zapisana jako mapa.html")