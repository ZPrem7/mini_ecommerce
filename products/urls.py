from django.urls import path
from django.contrib.auth import views as auth_views
from  .views import home, ProductCreateView,CustomLoginView,UserRegisterView,UserProfileView,ProductListView,ProductDetailView,ProductUpdateView,ProductDeleteView,profile_update

urlpatterns = [
    path('',CustomLoginView.as_view(), name='login'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('profile/update/', profile_update, name='profile_update'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

]

