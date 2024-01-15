import subprocess
from pathlib import Path
from sys import stdin, stderr, stdout

from .models import Product
from .parser import sears_parser


def get_product_data(ids):
    exist_ids = []
    for product_id in ids:
        product = sears_parser.get_parsed_data(product_id)
        if product is not None:
            exist_ids.append(product_id)
            Product.objects.update_or_create(product_id=product_id, defaults=product)
            print(f"Успішний запит. Додано/оновлено дані продукта з {product_id=}")
    if exist_ids:
        print(f"Завершено оновлення даних для {exist_ids}")
    else:
        print(f"Завершено оновлення даних, продуктів з product_id: {ids} не існує")


def handle_valid_data(data):
    split_ids = data['ids_raw_data'].split(',')
    root_dir = Path(__file__).parent.parent
    command = (f'python {root_dir}/manage.py shell --command="from products.services import get_product_data; '
               f'get_product_data({split_ids})"')
    sub_process = subprocess.Popen(command, shell=True, stdin=stdin, stdout=stdout, stderr=stderr)
    print(f'Запущено SubProcess id:{sub_process.pid} для скрапінгу даних')
