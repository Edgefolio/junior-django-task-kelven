from django.test import TestCase

class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'funds/home.html')

    def test_get_funds_page(self):
        response = self.client.get('/view_funds/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'funds/funds.html')

    def test_get_upload_page(self):
        response = self.client.get('/upload/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'funds/upload.html')
