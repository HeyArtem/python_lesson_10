import unittest                    # импортированиt модуля unittest
from survey import AnonymousSurvey # импортирование тестируемого класса

''''
Изучаю pytest от Эльдара ч.7

Здесь я пишу такие же теств, как на странице test_survey
 но я применю метод setUp
 он позволит сразу создать экземпляр  AnonymousSurvey (my_survey = AnonymousSurvey(question))
и так же создать набор ответов которые дальше будут использоваться в методах  test_store_single_response() и test_store_three_responses().

Т.е. мне не нужно будет писать (создавать) в начале каждого метода my_survey = AnonymousSurvey(question)
и писать вопрос и варианты ответов


Теория:
Класс unittest.TestCase содержит метод setUp(), который позволяет создать эти объекты один раз, 
а затем использовать их в каждом из тестовых методов. 
Если в класс TestCase включается метод setUp(), 
Python выполняет метод setUp() перед запуском каждого метода, имя которого начинается с test_. 

Все объекты, созданные методом setUp(), становятся доступными во всех тестовых методах.

Применим метод setUp() для создания экземпляра AnonymousSurvey и набора ответов, 
которые могут использоваться в test_store_single_response() и test_store_three_responses(). 
Заменим содержимое файла test_survey.py следующим кодом:
'''

class TestAnonmyousSurvey(unittest.TestCase):  # сценарий наследуется от unittest.TestCase
    """Тесты для класса AnonymousSurvey"""
    def setUp(self):
        ''''Создание опроса и набора ответов для всех тестовых методов.'''

        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        ''''создает экземпляр опроса; self позволяет использовать в любом месте класса'''

        self.responses = ['English', 'Spanish', 'Mandarin']
        ''''создает список ответов; self позволяет использовать в любом месте класса'''


    def test_store_single_response(self):  # проверяет, что сохраненный ответ действительно попадает в список ответов опроса; имя начиниется с test_
        """
        Проверяет, что один ответ сохранен правильно.
        Больше НЕ СОЗДАЕМ ЭКЗЕМПЛЯР опроса и ОТВЕТЫ

        т.е. не пишем
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)  # создаем экземпляр тестируемого класса

        """

        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        """"
        Убеждаемся в том, что первый ответ в self.responses -> self.responses[0]
        сохранен приавильно
        """

    '''
    Метод, который будет проверять несколько имен
    '''

    def test_store_three_responses(self):
        """
        Так же не создаем экземпляр опроса и варианты ответов
        не пишем:
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        """
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            """"
            Убеждаемся в том, что все три ответа были правильно сохранены
            в self.responses
            """
            self.assertIn(response, self.my_survey.responses)





if __name__ == '__main__':
    unittest.main()

""""
Итоги
При работе над проектами, требующими значительных затрат ресурсов на разработку, 
необходимо обеспечить тестирование критических аспектов поведения функций и классов. 
С эффективными тестами можно быть уверенным в том, что изменения в проекте не повредят тому, 
что уже работает; позволит совершенствовать код дальше. 
О нарушении существующей функциональности всегда сообщит сбойный тест, что позволит быстро исправить проблему.
"""