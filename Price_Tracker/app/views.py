from django.shortcuts import render
from .price_checker import Price as p
from .form import LinkForm
from .models import Product
from django.shortcuts import redirect

# Create your views here.
def home(request):
    form = LinkForm()
    error = None
    if request.method == "POST":
        form = LinkForm(request.POST)
        try:
            if form.is_valid():
                form.save()
        except:
            error = "Error! Please enter a valid URL."
    products = Product.objects.all()
    
    context = {
        'form':form,
        'error':error,
        'product':products
    }
    return render(request, 'home.html', context)

def pdelete(request,pk):
    product=Product.objects.get(id=pk)
    product.delete()
    return redirect ('home')
def update_price(request):
    product = Product.objects.all()
    for item in product:
        item.save()
    return redirect('home')