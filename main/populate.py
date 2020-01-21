from main.database import *
from main.models import *

import random


def delete_tables():
    # Rating.objects.all().delete()
    User.objects.all().delete()
    Peripheral.objects.all().delete()


def populate_users():
    print("Loading users...")

    res = []
    dict = {}
    users = open("users.txt", "r")
    for user in users.readlines():
        trimed = user.split(';')
        if len(trimed) != 5:
            continue
        id_user = int(trimed[0].strip())
        username = str(trimed[1].strip())
        age = int(trimed[2].strip())
        gender = str(trimed[3].strip())
        zip_code = str(trimed[4].strip())
        u = User(id=id_user, username=username, age=age, gender=gender, zipCode=zip_code)
        res.append(u)
        dict[id_user] = u
    users.close()
    User.objects.bulk_create(res)

    print("Users inserted: " + str(User.objects.count()))
    print("---------------------------------------------------------")
    return dict


def populate_peripherals():
    print("Loading peripherals...")
    res = []
    peripherals = get_peripherals()
    for peripheral in peripherals:
        for item in peripheral:
            res.append(
                Peripheral(name=item[0], brand=item[1], image=item[2], price=item[3],
                           type_db=item[5], stars=item[4])

            )

    Peripheral.objects.bulk_create(res)

    print("Peripherals inserted: " + str(Peripheral.objects.count()))
    print("---------------------------------------------------------")

    return res


def populate_ratings(number_ratings):
    print("Loading ratings...")
    Rating.objects.all().delete()

    res = []
    i = 0
    while i < number_ratings:
        random_user = User.objects.get(id=random.randint(1, User.objects.count()))
        peripherals = Peripheral.objects.all()
        peripherals_id = []
        for peripheral in peripherals:
            peripherals_id.append(peripheral.pk)
        random_score = random.randint(1, 5)
        random_peripheral = Peripheral.objects.get(id=peripherals_id[random.randint(1, len(peripherals_id)-1)])
        res.append(Rating(user=random_user, peripheral=random_peripheral, rating=random_score))
        i += 1
    Rating.objects.bulk_create(res)
    print("Ratings inserted: " + str(Rating.objects.count()))
    print("---------------------------------------------------------")


def populate_db():
    delete_tables()
    populate_users()
    populate_peripherals()
    populate_ratings(9999)
    print("Finished database population")


if __name__ == '__main__':
    populate_db()
