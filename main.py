from mapbook_lib.model import users
from mapbook_lib.controller import read_data, add_user,remove_users, update_users

while True:
    print('0 - zakończ program')
    print('1 - wyświetl znajomych')
    print('2 - dodaj znajomego')
    print('3 - usuń znajomego')
    print('4 - zmodyfikuj dane znajomego')


    choose = input('wybierz opcję: ')
    if choose == '0':
        break
    if choose == '1':
        read_data(users[1:])
    if choose == '2':
        add_user(users)
    if choose == '3':
        remove_users(users)
    if choose == '4':
        update_users(users)