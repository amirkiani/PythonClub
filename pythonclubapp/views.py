from django.shortcuts import render
from .models import ProductType, Product, Review
from .forms import ProductForm


# Create your views here.
def index (request):
    return render(request, 'pythonclubapp/index.html')

def gettypes(request):
    type_list=ProductType.objects.all()
    return render(request, 'pythonclubapp/types.html' ,{'type_list' : type_list})

def getproducts(request):
    products_list=Product.objects.all()
    return render(request, 'pythonclubapp/products.html', {'products_list': products_list})

def productdetails(request, id):
    reviews=Review.objects.filter(product=id).count()
    context={
        'reviews' : reviews,
    }
    return render(request, 'pythonclubapp/productdetails.html', context=context)

def newProduct(request):
     form=ProductForm
     if request.method=='POST':
          form=ProductForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ProductForm()
     else:
          form=ProductForm()
     return render(request, 'pythonclubapp/newproduct.html', {'form': form})