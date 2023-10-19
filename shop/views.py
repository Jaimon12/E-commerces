from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Product,ContactMessage
from .forms import ContactForm
from django.core.paginator import Paginator,EmptyPage,InvalidPage
def allProdCat(request, c_slug=None):
    c_page = None
    products_list = None
    
    if c_slug:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(category=c_page, available=True)
    else:
        products_list = Product.objects.filter(available=True)
    pageinator=Paginator(products_list,5)
    try:
        page=int(request.GET.get('page',1))
    except:
        page=1
    try:
        products=pageinator.page(page)
    except (EmptyPage,InvalidPage):
        products=pageinator.page(pageinator.num_pages)
    return render(request, 'category.html', {'category': c_page, 'products': products})
def proDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'product.html', {'product': product})

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        connect=ContactMessage(name=name,email=email,message=message)
        connect.save()
        form = ContactForm(request.POST)
        if form.is_valid():
            print('Name:', form.cleaned_data['name'])
            print('Email:', form.cleaned_data['email'])
            print('Message:', form.cleaned_data['message'])
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})