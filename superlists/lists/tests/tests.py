from django.test import TestCase


class SmokeTest(TestCase):
    '''Тест на токсичность'''

    def test_had_maths(self):
        '''тест: неправильные математические расчеты'''
        self.assertEqual(1 + 1, 3)
