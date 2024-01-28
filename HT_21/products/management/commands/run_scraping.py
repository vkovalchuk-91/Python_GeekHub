from django.core.management import BaseCommand

from products.models import Product
from products.parser import sears_parser


class Command(BaseCommand):
    help = "Start scraping products"

    def add_arguments(self, parser):
        parser.add_argument('ids', nargs="+", type=str)

    def handle(self, *args, **options):
        split_ids = options['ids'][0].split(',')
        exist_ids = []
        print(f"Додано в чергу на оновлення {len(split_ids)} потенційних ID продуктів")
        for product_id in split_ids:
            product = sears_parser.get_parsed_data(product_id)
            if product is not None:
                exist_ids.append(product_id)
                Product.objects.update_or_create(product_id=product_id, defaults=product)
                print(f"Успішний запит. Додано/оновлено дані продукта з {product_id=}")
        if exist_ids:
            print(f"Завершено оновлення даних для {len(exist_ids)} продуктів з кодами {exist_ids}")
        else:
            print(f"Завершено оновлення даних, продуктів з product_id: {split_ids} не існує")
