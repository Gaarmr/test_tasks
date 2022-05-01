import csv


students_avg_scores = {'Max': 4.964, 'Eric': 4.962, 'Peter': 4.923, 'Mark': 4.957, 'Julie': 4.95, 'Jimmy': 4.973, 'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936, 'Zoi': 4.937}


def make_report_about_top3(students_avg_scores: dict):
    stud_list = []
    for key, value in students_avg_scores.items():
        stud_list.append((value, key))

    stud_list = sorted(stud_list, reverse=True)

    with open('stud_list.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';',
        quotechar='|', quoting=csv.QUOTE_MINIMAL)

        filewriter.writerow(['Student', 'Score'])
        
        for value, key in stud_list[:3]:
            filewriter.writerow([key, value])




make_report_about_top3(students_avg_scores)