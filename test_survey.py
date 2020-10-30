
import unittest                    # импортированиt модуля unittest
from survey import AnonymousSurvey # импортирование тестируемого класса

''''
Изучаю pytest от Эльдара ч.6
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
        '''' Проверяет, что три ответа были сохранены правильно. '''
        question = "What language did you first learn to speak?"
        my_syrvey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_syrvey.store_response(response)
        for response in responses:
            self.assertIn(response, my_syrvey.responses)



    ''''
    
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

'''
if __name__ == '__main__':
    unittest.main()

''''ПОКА ТЕСТ НЕ ИДЕТ!!!!!          '''