from unittest import TestCase, mock

import apis.controllers.GetStatusAsset.GetStatusAsset as controller_get_status_asset


from django.db import connection

class TestGetStatusAsset(TestCase):

    cursor = None

    def setUp(self):

        self.controller = controller_get_status_asset.controller_get_status_asset()

    def test_get_status_asset(self):

        result = self.controller.get_status_asset()

        print(result)

        # self.assertEqual(result, True)

    def test_telegram_send(self):

        result = self.controller.telegram_send("test")

        print(result)
