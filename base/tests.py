from unittest import skip

from django.test import TestCase, Client

from base.factory import ProductListFactory


class ProductTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_empty_product_list(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.json(), [])

    @skip("List of all products")
    def test_product_list(self):
        response = self.client.get('/products/')
        products = ProductListFactory
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.json, [products])



