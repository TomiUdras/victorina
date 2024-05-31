import random

global_variable = 0
global_variable_n = 0

def ask_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            user_answer = int(input("Выберите номер правильного ответа: "))
            global global_variable
            global_variable = user_answer
            if 1 <= user_answer <= len(options):
                break
            else:
                print(f"Пожалуйста, выберите номер от 1 до {len(options)}")
        except ValueError:
            print("Введите целое число.")

    if user_answer == correct_option:
      print("Правильно!\n")
      return 1
    else:
      global global_variable_n
      global_variable_n += 1
      if global_variable_n > 5:
        print("К сожалению, вы не угадали\n")
        return 0
      else:
        if do_it_a_second_time(question, options, correct_option) == 0:
          return 0
        

def do_it_a_second_time(question, options, correct_option):
    print("\nНеправильно( \nПопробуем еще раз?")
    while True:
      try:
        yesORno = int(input("1. ДА \n2. НЕТ \nВаш ответ: "))
        print("\n")
        if 1 <= yesORno <= 2:
            break
        else:
            print(f"Пожалуйста, выберите номер от 1 до 2")
      except ValueError:
        print("Введите целое число.")
    if yesORno == 1:
        ask_question(question, options, correct_option)
    else:
        return 0

def write_results_to_file(results, filename):
    with open(filename, "w") as file:
        file.write("Вопросы, ответы пользователя и правильные ответы:\n\n")
        for result in results:
            file.write(f"Вопрос: {result['question']}\n")
            file.write(f"Ответ пользователя: {result['user_answer']}\n")
            file.write(f"Правильный ответ: {result['correct_answer']}\n\n")

        file.write(f"Итоговый счет: {sum(result['score'] for result in results)}/{len(results)}\n")
        file.write("Результат: Хороший результат" if sum(result['score'] for result in results) >= len(results) / 2 else "Результат: Плохой результат")

def main():
    score = 0
    results = []

    questions = [
        {
          "question": "Какие пруды несколько столетий именовались Погаными?",
          "options": ["Патриаршие пруды", "Чистые пруды", "Новодевичьи пруды", "Царицынские пруды"],
          "correct_option": 2
        },

        {
          "question": "Площадь, где на протяжении многих лет лучше было на появляться людям, дорожащим своей жизнью. Площадь с ночлежными домами, в которых творили разгул и беззаконие",
          "options": ["Манежная площадь", "Красная площадь", "Хитровская площадь", "Манежная площадь"],
          "correct_option": 3
        },

        {
          "question": "В XVIII столетии в этих местах, представлявших собой городскую окраину, было организовано кладбище, на котором хоронили неопознанных покойников, самоубийц и всех тех. чьи родные просто не могли оплатить захоронение где-то в приличном месте.",
          "options": ["Марьина Роща", "Северное Бутово", "Южное Тушино", "Печатники"],
          "correct_option": 1
        },

        {
          "question": "При царе Алексее Михайловиче, который серьезно вознамерился устроить в этом месте земной рай, здесь начали применять передовые средства земледелия и разводить различные экзотические для средней полосы фрукты и деревья. Выращивали шелковицу, арбузы, дыни, финики, виноград!",
          "options": ["Усадьба Лефортово", "Усадьба Коломенское", "Усадьба Алтуфьево", "Усадьба Измайлово"],
          "correct_option": 4
        },

        {
          "question": "В этом месте торговали чаем с XVII столетия! Здание вскоре стало известно в Москве как «китайская шкатулка». Там не только продавали сотни сортов чая - в магазине был дегустационный зал и располагалась небольшая коллекция произведений восточного искусства.",
          "options": ["Доходный дом Торлецкого", "Доходный дом Перлова", "Доходный дом Н. Г. Тарховой", "Доходный дом Третьяковых"],
          "correct_option": 2
        },

        {
          "question": "В 1990 году эта церковь была представлена на золотой памятной монете номиналом 50 рублей из серии «500-летие единого Русского государства»",
          "options": ["Церковь Архангела Гавриила", "Церковь Вознесения Господня в Коломенском", "Церковь Георгия Победоносца на Псковской Горке", "Церковь Варвары Великомученицы на Варварке"],
          "correct_option": 1
        },

        {
          "question": "Этот храм изначально строился в память о победе России в Отечественной войне 1812 года. В декабре 1931 года, согласно принятому решению ЦИК СССР, храм был снесен, и на его месте планировалось построить грандиозный Дворец Советов. Фундамент будущего Дворца постоянно либо заливало водой, либо он просто проваливался в землю. Пришлось делать на этом месте бассейн под открытым небом.",
          "options": ["Храм Христа Спасителя", "Храм Василия Блаженного", "Храм Живоначальной Троицы на Борисовских прудах", "Храм Воскресения Христова в Сокольниках"],
          "correct_option": 1
        },

        {
          "question": "В СССР была выпущена серия марок, посвященная этим зданиям, причем на марках были представлены как осуществленные проекты, так и неосуществленные.",
          "options": ["Доходные дома", "Дома-кольца", "Сталинские Высотки", "Дома авиаторы"],
          "correct_option": 3
        },

        {
          "question": "Самое высокое сооружение в Европе. Его высота (со шпилем) - более 540 метров. На высоте около 340 метров находится смотровая площадка.",
          "options": ["Дом на Мосфильмовской", "Останкинская телебашня", "Башня Федерация", "Главное здание МГУ"],
          "correct_option": 2
        },

        {
          "question": "По этому мосту на прием в Кремль ехал Гагарин после своего полета в космос в 1061 году.",
          "options": ["Большой Каменный мост", "Парящий мост", "Крымский мост", "Живописный мост"],
          "correct_option": 1
        },

    ]

    random.shuffle(questions)

    for q in questions:
        score = ask_question(q["question"], q["options"], q["correct_option"])
        if score == None:
          score = 0
        user_answer = global_variable 
        user_answer = q["options"][user_answer - 1]
        results.append({
            "question": q["question"],
            "user_answer": user_answer,
            "correct_answer": q["options"][q["correct_option"] - 1],
            "score": score
        })

    write_results_to_file(results, "results.txt")

if __name__ == "__main__":
    main()
