from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.views import View
from .forms import UserRegistrationForm ,ProductForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from .models import Product,Category,Tag
from django.views.generic import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request,"home.html")

class CustomLoginView(LoginView):
    template_name = 'product_templates/login.html'

    def get_success_url(self):
        return reverse_lazy('profile')


class UserRegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'product_templates/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('profile')
        return render(request, 'product_templates/register.html', {'form': form})    

class ProductCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'product_templates/product_form.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        return render(request, 'product_templates/product_form.html', {'form': form})


class UserProfileView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'product_templates/profile.html', {'user': request.user})
    

class ProductListView(LoginRequiredMixin,View):
    def get(self, request):
        category = Category.objects.all()
        return render(request, 'product_templates/product_list.html', {'category': category})

class ProductDetailView(LoginRequiredMixin,View):
    def get(self, request, pk):
        category_data=Category.objects.filter(id=pk)
        product = Product.objects.filter(categories__id=pk)
        category_name =category_data.values_list('name', flat=True)[0]
        return render(request, 'product_templates/product_detail.html', {'product': product,'category_name': category_name})    
    

class ProductUpdateView(LoginRequiredMixin,View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'product_templates/product_form.html', {'form': form})

    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        return render(request, 'product_templates/product_form.html', {'form': form})

class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    template_name = 'product_templates/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data.get('password')
            if password:
                user.set_password(password)
            user.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
    context = {
        'user_form': user_form
    }
    return render(request, 'product_templates/profile_update.html', context)