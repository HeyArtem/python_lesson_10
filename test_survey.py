
import unittest                    # импортированиt модуля unittest
from survey import AnonymousSurvey # импортирование тестируемого класса

''''
Изучаю pytest от Эльдара ч.6
Напишем тест, который проверяет всего один аспект поведения AnonymousSurvey: 
 один ответ на опрос сохраняется правильно. Сохраним в файл test_survey.py следующий код:
'''

class TestAnonmyousSurvey(unittest.TestCase):  # сценарий наследуется от unittest.TestCase
    """Тесты для класса AnonymousSurvey"""


    def test_store_single_response(self):  # проверяет, что сохраненный ответ действительно попадает в список ответов опроса; имя начиниется с test_
        """Проверяет, что один ответ сохранен правильно."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)  # создаем экземпляр тестируемого класса
        my_survey.store_response('English')  # сохраняем один ответ (English)
        self.assertIn('English', my_survey.responses)  # проверяет наличие тестового значения в списке ответов.

    '''
    Тест проверяет электронный опрос только на одно имя.
    Допишем метод, который будет проверять несколько имен
    '''

    def test_store_three_responses(self):
        """Проверяет, что три ответа были сохранены правильно."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)





if __name__ == '__main__':
    unittest.main()

''''
Дальше я создам страницу test_2_survey,
в котрой буду использовать метод seUp
он позволит сразу создать экземпляр  AnonymousSurvey (my_survey = AnonymousSurvey(question))
и так же создать набор ответов которые дальше будут использоваться в методах  test_store_single_response() и test_store_three_responses().

Т.е. мне не нужно будет писать (создавать) в начале каждого метода my_survey = AnonymousSurvey(question)
и писать вопрос и варианты ответов
'''

