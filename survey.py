''''
Изучаю pytest от Эльдара ч.4

'''

class AnonymousSurvey():
    """Сбор анонимных ответов на опросы."""

    def __init__(self, question):
        """Сохраняет вопрос и готовится к сохранению ответов."""
        self.question = question  # вопрос к респонденту
        self.responses = []  # пустой список для хранения ответов

    def show_question(self):  # метод вывода вопроса
        """Выводит вопрос."""
        print(self.question)

    def store_response(self, new_response):  # метод добавления нового ответа в список ответов
        """Сохраняет один ответ на опрос."""
        self.responses.append(new_response)

    def show_results(self):  # метод вывода всех ответов, хранящихся в списке
        """Выводит все полученные ответы."""
        print("Survey results\nРезультаты опроса:")
        for response in self.responses:
            print(f"- {response}")

