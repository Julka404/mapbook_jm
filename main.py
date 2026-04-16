users: list = [
    {'username': 'oliwia', 'location': 'łódź', 'posts': 1,
     'usermessage': ['życzenia1', 'kocham legie', 'sprzedam opla', 'kiwi']},
    {'username': 'paweł', 'location': 'ostróda', 'posts': 2,
     'usermessage': ['życzenia2', 'kocham legie', 'sprzedam opla']},
    {'username': 'eliza', 'location': 'radom', 'posts': 3, 'usermessage': ['życzenia3', 'kocham legie']},
    {'username': 'filip', 'location': 'dęblin', 'posts': 4,
     'usermessage': ['życzenia4', 'kocham legie', 'sprzedam opla', 'kiwi3']}
]


def read_data(users_data: list) -> None:
    for user in users_data:
        print(
            f'twój znajowmy {user['username']} z miejscowości {user["location"]} opublikował {user['posts']} wiadomości. Ostatnia wiadomość {user['usermessage'][-1]}')



read_data(users[1:])