from __future__ import unicode_literals

from django.apps import AppConfig
from watson import search as watson


class ProductsConfig(AppConfig):
    name = 'products'

    def ready(self):
        YourModel = self.get_model("Product")
        watson.register(YourModel)

