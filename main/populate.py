import django
from main.database import *
from main.models import *


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
        zip_code = int(trimed[4].strip())
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


def populate_ratings(user, peripheral):
    print("Loading ratings...")
    Rating.objects.all().delete()

    res = []
    ratings = get_ratings()
    for rating in ratings:
        res.append(Rating(user=user, peripheral=peripheral, rating=rating))
    Rating.objects.bulk_create(res)

    print("Ratings inserted: " + str(Rating.objects.count()))
    print("---------------------------------------------------------")


def populate_db():
    delete_tables()
    u = populate_users()
    p = populate_peripherals()
    # populate_ratings(u, p)
    print("Finished database population")


if __name__ == '__main__':
    populate_db()
