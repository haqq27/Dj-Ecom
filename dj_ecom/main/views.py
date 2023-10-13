from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView, View
from .models import Product, Customer
from .forms import CustomerRegForm, UserUpdateForm, CustomerProfileForm
from django.contrib import messages

# Create your views here.

def home(request):

    return render(request, 'main/home.html', )

def about(request):

    return render(request, 'main/about.html', )

def contact(request):

    return render(request, 'main/contact.html', )

class CategoryView(View):

    def get(self, request, val):

        product = Product.objects.filter(category = val)
        # title
        return render(request, 'main/category.html', locals()) 
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'

class CustomerRegView(View):
   
    def get(self, *args, **kwargs):
        form = CustomerRegForm()
        return render(self.request, 'main/customer-reg.html', locals()) 

    def post(self, *args, **kwargs):
        form = CustomerRegForm(self.request.POST)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Congratulations! User registered successfully.')
        else:
            messages.warning(self.request, 'Invalid Input Data')
        return render(self.request, 'main/customer-reg.html', locals()) 
    
class ProfileView(View):
    def get(self, *args, **kwargs):
        u_form = UserUpdateForm(instance=self.request.user)
        c_form = CustomerProfileForm(instance=self.request.user)
        return render(self.request, 'main/profile.html', locals()) 

    def post(self, *args, **kwargs):
        u_form = UserUpdateForm(self.request.POST, instance=self.request.user)
        c_form = CustomerProfileForm(self.request.POST, instance=self.request.user.customer)
        if u_form.is_valid() and c_form.is_valid():
            u_form.save()
            user = self.request.user
            mobile = c_form.cleaned_data['mobile']
            state = c_form.cleaned_data['state']
            zipcode = c_form.cleaned_data['zipcode']
            reg = Customer(user = user, mobile = mobile, state=state, zipcode = zipcode)
            reg.save()
            messages.success(self.request, f'Congratulations! Profile updated successfully')
        else:
            messages.warning(self.request, 'Invalid Input Data')
        return render(self.request, 'main/profile.html', locals()) 
