from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Product, Category
from .forms import UserRegistrationForm, UserUpdateForm, ProductForm

class HomeViewTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class CustomLoginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('login')

    def test_login_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_templates/login.html')

    def test_login_view_post(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(self.url, data)
        self.assertRedirects(response, reverse('profile'))

class UserRegisterViewTest(TestCase):
    def setUp(self):
        self.url = reverse('register')

    def test_register_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_templates/register.html')

    def test_register_view_post(self):
        data = {
            'username': 'newuser',
            'password': 'newpassword',
            'email': 'newuser@example.com'
        }
        response = self.client.post(self.url, data)
        self.assertRedirects(response, reverse('profile'))

class UserProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('profile')

    def test_profile_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_templates/profile.html')

class ProductListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('product_list')

    def test_product_list_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_templates/product_list.html')

class ProductDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name="TestCategory", description="Test Description")
        self.product = Product.objects.create(
            categories=self.category,
            title='Test Product',
            description='Test Description',
            price=100.00,
            stock_quantity=10
        )
        self.client.login(username='testuser', password='testpassword')

    def test_product_detail_view_get(self):
        url = reverse('product_detail', kwargs={'pk': self.category.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_templates/product_detail.html')

class ProductUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name="TestCategory", description="Test Description")
        self.product = Product.objects.create(
            categories=self.category,
            title='Test Product',
            description='Test Description',
            price=100.00,
            stock_quantity=10
        )
        self.client.login(username='testuser', password='testpassword')

    def test_product_update_view_get(self):
        url = reverse('product_update', kwargs={'pk': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_templates/product_form.html')

    def test_product_update_view_post(self):
        url = reverse('product_update', kwargs={'pk': self.product.pk})
        data = {
            'categories': self.category.pk,
            'title': 'Updated Product',
            'description': 'Updated Description',
            'price': 150.00,
            'stock_quantity': 5
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('product_list'))

class ProductDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name="TestCategory", description="Test Description")
        self.product = Product.objects.create(
            categories=self.category,
            title='Test Product',
            description='Test Description',
            price=100.00,
            stock_quantity=10
        )
        self.client.login(username='testuser', password='testpassword')

    def test_product_delete_view(self):
        url = reverse('product_delete', kwargs={'pk': self.product.pk})
        response = self.client.post(url)
        self.assertRedirects(response, reverse('product_list'))
        self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())

class ProfileUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('profile_update')

    def test_profile_update_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_templates/profile_update.html')

    def test_profile_update_view_post(self):
        data = {
            'username': 'updateduser',
            'email': 'updateduser@example.com'
        }
        response = self.client.post(self.url, data)
        self.assertRedirects(response, reverse('profile'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')
        self.assertEqual(self.user.email, 'updateduser@example.com')
