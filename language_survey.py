''''
Изучаю pytest от Эльдара ч.5
Напишем программу, которая использует класс AnonymousSurvey:
'''

from survey import AnonymousSurvey

# Определение вопроса с созданием экземпляра AnonymousSurvey.
question = "What language did you first learn to speak\nНа каком языке вы впервые научились говорить?"
my_survey = AnonymousSurvey(question)

# Вывод вопроса и сохранение ответов.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Вывод результатов опроса.
print("\nThank you to everyone who participated in the survey!\nСпасибо всем, кто принял участие в опросе!")
my_survey.show_results()