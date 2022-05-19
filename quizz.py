import random

geography_points = 0
mathematics_points = 0
literature_points = 0
total_points = 0
i = 0

question_type = ["География", "Математика", "Литература"]
choose = input(f"Изберете направление: {question_type} - ")
choose_o = []

geo_q = ['Как се казва морето, на което България има излас ?:','Столицата на България се казва ?:',
         'Най-високия връх в България е ?:']

math_q = ['Колко е 1 + 1 ?:','Колко страни има квадрата ?:','Колко е 2 х 1 ?:','Колко е 5 - 2 ?:']
math_q_a = ['2','4','2','3']

lit_q = ["Кой е автора на 'Бай Ганьо ?:","Кой е автора на 'То' ?:"]

past_questions_m = []
past_questions_g = []
past_questions_l = []


while True:
    if choose not in question_type:
        print("Моля въведете валидно направление !:")
        choose = input()
    else:
        break

print("Вие избрахте:", choose)

if choose == "Математика":
    while i < len(math_q):
        math = random.choice(math_q)
        if len(math_q) == len(past_questions_m):
            break
        if math in past_questions_m:
            continue
        else:
            past_questions_m.append(math)
            print(math)
            print("Вашият отговор: ")
            answer = input()
            if answer not in math_q_a:
                print("Не е вярно")
            else:
                print("Вярно")
                mathematics_points += 1

        i += 1
    print("Искате ли да продължите ?\nНапишете 'Yes' - за да, или 'No' - за не")

    next = input()
    if next == "No":
        print(f"Верните ти отговори по {choose} са {mathematics_points}")
        exit()
    elif next == "Yes":
        pass

print("Изберете следващо направление !")
choose = input()

if choose == "География":
    while i < len(geo_q):
        geo = random.choice(geo_q)
        if len(geo_q) == len(past_questions_g):
            break
        if geo in past_questions_g:
            continue
        else:
            past_questions_g.append(geo)
            print(geo)
        i += 1

if choose == "Литература":
    while i < len(lit_q):
        lit = random.choice(lit_q)
        if len(lit_q) == len(past_questions_l):
            break
        if lit in past_questions_l:
            continue
        else:
            past_questions_l.append(lit)
            print(lit)
        i += 1