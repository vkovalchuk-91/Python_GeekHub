from products.models import Product
from products.parser import sears_parser
from task_01.celery import celery_app as app


@app.task(name='run_products_scraping')
def run_scraping_task(**kwargs):
    print(f'Запущено Celery для скрапінгу даних')
    split_ids = kwargs.get("ids").split(',')
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
