import random


def write_users_txt(file_name, users_number):
    users_txt = open(file_name, "w")
    for i in range(users_number):
        id_user = i + 1
        age = 10 + random.randint(1, 18)
        gender = "M" if id_user % 2 is 0 else "F"
        zip_code = 40000 + id_user
        users_txt.write("{};user{};{};{};{}\n".format(id_user, id_user, age, gender, zip_code))
    users_txt.close()
    return "users.txt"


write_users_txt("users.txt", 10000)
