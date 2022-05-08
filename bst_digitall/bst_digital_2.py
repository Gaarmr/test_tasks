names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris", "Margo"]
birthday_years = [1962, 1995, 2000, None, None, None, None, 1998, 2001]
genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None]


def get_inductees(names_list: list, by_list: list, genders_list: list):
    valid_stud = []
    not_defind_stud = []

    for name, birthday, gender in zip(names_list, by_list, genders_list):
        if not birthday or not gender:
            not_defind_stud.append(name)
            continue
        if gender == 'Female':
            continue
        age = 2021 - birthday
        if 18 <= age <= 30:
            valid_stud.append(name)

    return valid_stud, not_defind_stud


print(get_inductees(names, birthday_years, genders))


# def get_inductees(names_list: list, by_list: list, genders_list: list):
#     valid_stud = []
#     not_defind_stud = []

#     for stud_index in range(len(names_list)):
#         if by_list[stud_index] == None or genders_list[stud_index] == None:
#             not_defind_stud.append((names_list[stud_index], by_list[stud_index], genders_list[stud_index]))
#         else:
#             if 2021 - birthday_years[stud_index] >= 18 and 2021 - birthday_years[stud_index] <= 30:
#                 valid_stud.append((names_list[stud_index], by_list[stud_index], genders_list[stud_index]))

#     return valid_stud, '|', not_defind_stud


# print(get_inductees(names, birthday_years, genders))
