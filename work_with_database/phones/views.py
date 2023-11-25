from django.shortcuts import get_object_or_404, render, redirect

from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get('sort', '')
    phones = Phone.objects.all()
    sort_comands = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
        }
    if sort_pages:
        phones = phones.order_by(sort_comands[sort_pages])
        context = {
        'phones': phones
        }
        return render(request, template, context)
    else:
        context = {
        'phones': phones
        }
        return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {
       'phone': phone
    }
    print(context)
    return render(request, template, context)
