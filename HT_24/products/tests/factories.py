import factory
from django.contrib.auth.models import User

from products.models import Product, Category

TEST_PASSWORD = 'adminadmin'


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Faker('name')
    password = factory.PostGenerationMethodCall('set_password', TEST_PASSWORD)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: 'Category {}'.format(n))


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    product_id = factory.Sequence(lambda n: 'Product {}'.format(n))
    name = factory.Sequence(lambda n: 'Product Name {}'.format(n))
    price = factory.Faker('random_number', digits=2)
    short_description = factory.Sequence(lambda n: 'Product Description {}'.format(n))
    brand = factory.Faker('company')
    category = factory.SubFactory(CategoryFactory)
    link_to_product = factory.Faker('url')
    update_date = factory.Faker('past_date')
