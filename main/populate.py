from datetime import datetime
from main.database import *
from main.models import *


def delete_tables():
    Rating.objects.all().delete()
    User.objects.all().delete()
    Peripheral.objects.all().delete()
    Category.objects.all().delete()
    Type.objects.all().delete()


def populate_categories():
    print("Loading categories...")

    categories = get_categories()
    res = []
    for category in categories:
        res.append(Category(id=int(category[0]), categoryName=str(category[1])))
    Category.objects.bulk_create(res)  # bulk_create hace la carga masiva para acelerar el proceso

    print("Categories inserted: " + str(Category.objects.count()))
    print("---------------------------------------------------------")


def populate_types():
    print("Loading peripherals types...")

    types = get_categories()
    res = []
    for type_db in types:
        res.append(Type(id=int(type_db[0], typeName=type[1])))
    Type.objects.bulk_create(res)

    print("Genres inserted: " + str(Type.objects.count()))
    print("---------------------------------------------------------")


# TODO: poblar usuarios a mansalva en algún momento
def populate_users():
    print("Loading users...")

    lista = []
    dict = {}
    fileobj = open(path + "\\u.user", "r")
    for line in fileobj.readlines():
        rip = line.split('|')
        if len(rip) != 5:
            continue
        id_u = int(rip[0].strip())
        u = UserInformation(id=id_u, age=rip[1].strip(), gender=rip[2].strip(),
                            occupation=Occupation.objects.get(occupationName=rip[3].strip()), zipCode=rip[4].strip())
        lista.append(u)
        dict[id_u] = u
    fileobj.close()
    UserInformation.objects.bulk_create(lista)

    print("Users inserted: " + str(UserInformation.objects.count()))
    print("---------------------------------------------------------")
    return (dict)


def populate_peripherals():
    print("Loading peripherals...")

    res = []
    peripherals = get_peripherals()
    for peripheral in peripherals:
        res.append(
            Peripheral(id=peripheral.id, brand=peripheral.brand, price=peripheral.price,
                       category=peripheral.category, types=peripheral.types, ratings=peripheral.ratings)
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
    populate_categories()
    u = populate_users()
    p = populate_peripherals()
    populate_ratings(u, p)
    print("Finished database population")


if __name__ == '__main__':
    populate_db()
