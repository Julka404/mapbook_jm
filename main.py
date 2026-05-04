from mapbook_lib.model import users
from mapbook_lib.controller import read_data, add_user, remove_user, update_user, get_mapa

while True:
    print("\n0 - zakończ program")
    print("1 - wyświetl znajomych")
    print("2 - dodaj znajomego")
    print("3 - usuń znajomego")
    print("4 - zmodyfikuj dane znajomego")
    print("5 - mapa znajomych")

    choose = input("Wybierz opcję: ")

    if choose == "0":
        break
    elif choose == "1":
        read_data(users)
    elif choose == "2":
        add_user(users)
    elif choose == "3":
        remove_user(users)
    elif choose == "4":
        update_user(users)
    elif choose == "5":
        get_mapa(users)
    else:
        print("Nie ma takiej opcji.")