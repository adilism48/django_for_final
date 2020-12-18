from django.test import TestCase


class SimpleTestCase(TestCase):
    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
