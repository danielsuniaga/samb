from unittest import TestCase, mock

from apis.repositories.iq.iq import repositories_iq

class TestRepositoriesIq(TestCase):

    def setUp(self):

        self.mock_cursor = mock.MagicMock()
        
        self.repo = repositories_iq(self.mock_cursor)

        self.new_value = "some_result"

        self.expected_value = "some_result"

        self.new_date = "2024-06-01"

    def test_set_result_entry(self):

        new_value = self.new_value

        result = self.repo.set_result_entry(new_value)
        
        self.assertEqual(self.repo.result_entry, new_value)
        
        self.assertTrue(result)

    def test_get_result_entry(self):

        expected_value = self.expected_value

        self.repo.result_entry = expected_value
        
        result = self.repo.get_result_entry()
        
        self.assertEqual(result, expected_value)

    def test_get_result_entry(self):

        expected_value = self.expected_value

        self.repo.id_entry = expected_value
        
        result = self.repo.get_id_entry()
        
        self.assertEqual(result, expected_value)

    def test_set_id_entry(self):

        new_value = self.new_value

        result = self.repo.set_id_entry(new_value)
        
        self.assertEqual(self.repo.id_entry, new_value)
        
        self.assertTrue(result)

    def test_set_complement_start_date(self):

        initial_start_date = self.repo.start_date 
        
        new_date = self.new_date
        
        result = self.repo.set_complement_start_date(new_date)
        
        self.assertTrue(result)

        self.assertEqual(self.repo.start_date, new_date + initial_start_date)

    def test_set_complement_end_date(self):

        initial_end_date = self.repo.end_date 
        
        new_date = self.new_date
        
        result = self.repo.set_complement_end_date(new_date)
        
        self.assertTrue(result)

        self.assertEqual(self.repo.end_date, new_date + initial_end_date)

    def test_seteo_count(self):

        result = self.repo.seteo_count()
                
        self.assertTrue(result)

    def test_get_current_entrys(self):

        new_date = self.new_date

        self.mock_cursor.execute.return_value = 1
        
        result = self.repo.get_current_entrys(new_date)

        self.assertEqual(result, {'status': True, 'msj': 'Success'})

    def test_get_current_entrys_min(self):

        date = self.new_date

        candles = 5

        self.mock_cursor.execute.return_value = [(1,)] 

        result = self.repo.get_current_entrys_min(date, candles)

        self.assertEqual(result, {'status': True, 'msj': 'Success'})

    def test_add_entrys_success(self):

        result = self.repo.add_entrys('TEST', 'TEST','TEST','TEST')

        self.assertEqual(result, {'status': True, 'msj': 'Success'})

    def test_add_entrys_result_success(self):

        result = self.repo.add_entrys_result('TEST', 'TEST')

        self.assertEqual(result, {'status': True, 'msj': 'Success'})

    def test_add_indicators_success(self):

        result = self.repo.add_indicators('TEST','TEST','TEST','TEST')

        self.assertEqual(result, {'status': True, 'msj': 'Success'})

    def test_add_movements(self):
       
        candles = [
            (1, '2024-06-01', '2024-06-01', 'condition', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
            (2, '2024-06-02', '2024-06-02', 'condition', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),
            (3, '2024-06-01', '2024-06-01', 'condition', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
            (4, '2024-06-02', '2024-06-02', 'condition', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),
            (5, '2024-06-01', '2024-06-01', 'condition', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
            (6, '2024-06-02', '2024-06-02', 'condition', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
        ]

        self.mock_cursor.executemany.return_value = None

        result = self.repo.add_movements(candles)

        self.assertEqual(result, {'status': True, 'msj': 'Success'})

    def test_get_sum_entrys_date(self):

        date = self.new_date

        self.mock_cursor.fetchone.return_value = (10,)  

        result = self.repo.get_sum_entrys_date(date)

        self.assertEqual(result, {'status': True, 'data': 10, 'msj': 'Success'})

