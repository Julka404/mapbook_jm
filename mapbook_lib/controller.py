def read_data(users_data: list) -> None:
    for user in users_data:
        print(
            f'twój znajowmy {user['username']} z miejscowości {user["location"]} opublikował {user['posts']} wiadomości. Ostatnia wiadomość {user['usermessage'][-1]}')


def add_user(users_data: list) -> None:
    name = input('podaj imię: ')
    location = input('Podaj lokalizację: ')
    posts = int(input('Podaj liczbe postów: '))
    usermessage = ['']
    users_data.append({'username': name, 'location': location, 'posts': posts,
                       'usermessage': usermessage}, )

def remove_users(users_data: list) -> None:
    name = input('Podaj imie uzytkownika do usuniecie: ')

    for user in users_data:
        if user['username'] == name:
            users_data.remove(user)
