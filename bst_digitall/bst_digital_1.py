candidates = [
 {"name": "Vasya",  "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya",  "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  "extra_scores":2},
 {"name": "Petya",  "scores": {"math": 92, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "1",  "scores": {"math": 100, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "2",  "scores": {"math": 34, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "3",  "scores": {"math": 65, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "4",  "scores": {"math": 7, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "5",  "scores": {"math": 1, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "6",  "scores": {"math": 0, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "7",  "scores": {"math": 40, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "8",  "scores": {"math": 67, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "9",  "scores": {"math": 78, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "10",  "scores": {"math": 87, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "11",  "scores": {"math": 100, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "12",  "scores": {"math": 34, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "13",  "scores": {"math": 65, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "14",  "scores": {"math": 7, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "15",  "scores": {"math": 2, "russian_language": 29, "computer_science": 37},  "extra_scores":1},
 {"name": "16",  "scores": {"math": 0, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "17",  "scores": {"math": 40, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "18",  "scores": {"math": 67, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "19",  "scores": {"math": 78, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "20",  "scores": {"math": 87, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
]


def find_top_20(candidates: list):
    
    score_list = []
    stud_list = ''

    for stud in candidates:
        stud_name = stud.get('name')
        stud_score = stud.get('scores')
        extra_scores = stud.get('extra_scores')
        total_score = sum(stud_score.values()) + extra_scores
        total_score_prof = stud_score["math"] + stud_score["computer_science"] + extra_scores

        score_list.append((total_score, stud_name, total_score_prof))

    top_20_stud = sorted(score_list, reverse=True)

    if top_20_stud[19][0] == top_20_stud[20][0] and top_20_stud[19][2] < top_20_stud[20][2]:
        top_20_stud.pop(19)
        
    i=1
    for stud in top_20_stud[:25]:
        stud_list += f'{i} {stud}\n'
        i+=1

    return stud_list

print(find_top_20(candidates))
