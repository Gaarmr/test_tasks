know_english = ["Vasya","Jimmy","Max","Peter","Eric","Zoi","Felix"]
sportsmen = ["Don","Peter","Eric","Jimmy","Mark"]
more_than_20_years = ["Peter","Julie","Jimmy","Mark","Max"]


def find_athlets(know_english_list, sportsmen_list, more_than_20_years_list):
    athlets_list = []
    all_stud = know_english_list + sportsmen_list + more_than_20_years_list


    for stud in all_stud:
        if stud in know_english_list and stud in sportsmen_list and stud in more_than_20_years_list:
            if stud not in athlets_list:
                athlets_list.append(stud)

    return athlets_list

print(find_athlets(know_english, sportsmen, more_than_20_years))