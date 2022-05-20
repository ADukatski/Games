import random

geography_points = 0
mathematics_points = 0
literature_points = 0
total_points = 0

question_type = ["География", "Математика", "Литература"]
choose = input(f"Изберете направление: {question_type} - ")
choose_o = []

geo_q = ['С кое море граничи България ?:','Столицата на България е ?:',
         'Най-високият връх в България е ?:']
geo_q_a = ['Черно море','София','Мусала']

math_q = ['Колко е 1 + 1 ?:','Колко страни има квадрата ?:','Колко е 2 х 1 ?:','Колко е 5 - 2 ?:']
math_q_a = ['2','4','2','3']

lit_q = ["Кой е автора на 'Бай Ганьо ?:","Кой е автора на 'Две хубави очи' ?:","Кой е автора на 'Под игото' ?:"]
lit_q_a = ["Алеко Константинов","Пейо Яворов","Иван Вазов"]

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

while True:
    if choose == "Математика":
        i = 0
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
            if i == len(math_q):
                print("Искате ли да продължите ?\nНапишете 'Yes' - за да, или 'No' - за не")

                next = input()
                while True:
                    if next == "No":
                        print(f"Верните ти отговори по {choose} са {mathematics_points}")
                        exit()
                    elif next == "Yes":
                        choose = input("Изберете следващо направление !")
                        break
                    next = input("Изберете 'Yes' или 'No':")

    elif choose == "География":
        i = 0
        while i < len(geo_q):
            geo = random.choice(geo_q)
            if len(geo_q) == len(past_questions_g):
                break
            if geo in past_questions_g:
                continue
            else:
                past_questions_g.append(geo)
                print(geo)
                print("Вашият отговор: ")
                answer = input()
                if answer not in geo_q_a:
                    print("Не е вярно")
                else:
                    print("Вярно")
                    geography_points += 1

            i += 1
            if i == len(geo_q):
                print("Искате ли да продължите ?\nНапишете 'Yes' - за да, или 'No' - за не")

                next = input()
                while True:
                    if next == "No":
                        print(f"Верните ти отговори по {choose} са {geography_points}")
                        exit()
                    elif next == "Yes":
                        choose = input("Изберете следващо направление !")
                        break
                    next = input("Изберете 'Yes' или 'No':")

    elif choose == "Литература":
        i = 0
        while i < len(lit_q):
            lit = random.choice(lit_q)
            if len(lit_q) == len(past_questions_l):
                break
            if lit in past_questions_l:
                continue
            else:
                past_questions_l.append(lit)
                print(lit)
                print("Вашият отговор: ")
                answer = input()
                if answer not in lit_q_a:
                    print("Не е вярно")
                else:
                    print("Вярно")
                    literature_points += 1

            i += 1
            if i == len(lit_q):
                print("Искате ли да продължите ?\nНапишете 'Yes' - за да, или 'No' - за не")

                next = input()
                while True:
                    if next == "No":
                        print(f"Верните ти отговори по {choose} са {mathematics_points}")
                        exit()
                    elif next == "Yes":
                        choose = input("Изберете следващо направление !")
                        break
                    next = input("Изберете 'Yes' или 'No':")

        if len(lit_q) == len(lit_q_a) and len(geo_q) == len(geo_q_a) and len(math_q) == len(math_q_a):
            print("Твоята игра приключи !\nТи отговори на вички възможни въпроси !")
            print(f"Твойте точки по География: {geography_points}")
            print(f"Твойте точки по Литература: {literature_points}")
            print(f"Твойте точки по Математика: {mathematics_points}")
            break
