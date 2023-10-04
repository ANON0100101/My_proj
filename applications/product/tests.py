from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from applications.product.models import Category, Product
from applications.product.views import CategoryModelViewSet, ProductModelViewSet
from applications.account.models import CustomUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# Create your tests here.


class CategoryTest(APITestCase):
    """
    Теты на модель категории
    """
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = CustomUser.objects.create_user('test@gmail.com', '1', is_active=True)

    def test_get_category(self):
        request = self.factory.get('api/v1/product/category')
        view = CategoryModelViewSet.as_view({'get': 'list'})
        response = view(request)
        print(response)
        assert response.status_code == 200
        assert Category.objects.count() == 0

    def test_post_category(self):

        data = {
            'name': 'Test',
        }
        request = self.factory.post('api/v1/product/category', data)
        force_authenticate(request, self.user)
        view = CategoryModelViewSet.as_view({'post': 'create'})
        response = view(request)
        assert response.status_code == 201
        assert Category.objects.count() == 1



class ProductTest(APITestCase):
    """
        тесты на продукты
    """
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = CustomUser.objects.create_user('test@gmail.com', '1', is_active=True)
        self.set_up_category()
        self.access_token = self.set_up_token()


    def set_up_token(self):
        data = {
            'email': 'test@gmail.com',
            'password': '1'
        }
        request = self.factory.post('api/v1/account/login', data)
        view = TokenObtainPairView.as_view()
        response = view(request)
        return response.data.get('access')

    @staticmethod
    def set_up_category():
        Category.objects.create(name='test')

    def test_get_product(self):
        request = self.factory.get('api/v1/product/', HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        # force_authenticate(request, self.user)
        view = ProductModelViewSet.as_view({'get': 'list'})
        response = view(request)
        print(response.data)
        assert response.status_code == 200
        assert len(response.data) == 0

    def test_post_product(self):
        image = open('images/Снимок_экрана_2023-09-18_в_18.27.14.png', 'rb')
        data = {
            'owner': self.user.id,
            'category': Category.objects.first().name,
            'title': 'test product',
            'price': 100,
            'image': image
        }
        request = self.factory.post('api/v1/product/', data=data, HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        image.close()
        view = ProductModelViewSet.as_view({'post': 'create'})
        response = view(request)
        assert response.status_code == 201
        assert response.data.get('title') == 'test product'
        assert Product.objects.count() == 1


