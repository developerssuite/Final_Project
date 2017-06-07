from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from products.forms import ProductForm, NewsLetterForm, ContactUsForm
from products.models import Product, Categories
from watson import search as wat

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def home(request):
    template = 'products/home.html'
    products = Product.objects.all()
    topProducts = products.order_by("-hit_count_generic__hits")
    newProducts = products.order_by("-created_at")
    if not request.user.is_authenticated():
        extended_template = 'products/base_visitor.html'
    else:
        extended_template = 'products/base.html'
    return render(request, template,
                  {'extended_template': extended_template,
                   'products_list': products,
                   'top_products': topProducts,
                   'new_products': newProducts})


def detail(request, product_id):
    if not request.user.is_authenticated():
        extended_template = 'account/base.html'
        return render(request, 'account/login.html', {'extended_template': extended_template})
    else:
        extended_template = 'products/base.html'
        template = 'products/detail.html'
        product = Product.objects.get(pk=product_id)
        user = User.objects.get(pk=product.user_id)
        return render(request, template,
                      {'extended_template': extended_template, 'product': product, 'user': user, 'likes': "Yes"})


def about_us(request):
    if not request.user.is_authenticated():
        extended_template = 'products/base_visitor.html'
    else:
        extended_template = 'products/base.html'
    template = 'products/about_us.html'
    return render(request, template, {'extended_template': extended_template})


def submit_newsletter(request):
    products = Product.objects.all()
    topProducts = products.order_by("-hit_count_generic__hits")
    newProducts = products.order_by("-created_at")
    template = 'products/home.html'
    if not request.user.is_authenticated():
        extended_template = 'products/base_visitor.html'
    else:
        extended_template = 'products/base.html'

    form = NewsLetterForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        newsletter = form.save(commit=False)
        newsletter.save()
    return render(request, template,
                  {'extended_template': extended_template,
                   'products_list': products,
                   'top_products': topProducts,
                   'new_products': newProducts})


def contact_us(request):
    template = 'products/contact_us.html'
    if not request.user.is_authenticated():
        extended_template = 'products/base_visitor.html'
    else:
        extended_template = 'products/base.html'
    form = ContactUsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        contact = form.save(commit=False)
        contact.save()

    return render(request, template, {'extended_template': extended_template})


def categories(request):
    template = 'products/categories.html'
    products = Product.objects.all()
    topProducts = products.order_by("-hit_count_generic__hits")
    newProducts = products.order_by("-created_at")
    if not request.user.is_authenticated():
        extended_template = 'products/base_visitor.html'
    else:
        extended_template = 'products/base.html'
    return render(request, template,
                  {'extended_template': extended_template,
                   'products_list': products,
                   'top_products': topProducts,
                   'new_products': newProducts})


def create_product(request):
    if not request.user.is_authenticated():
        extended_template = 'account/base.html'
        return render(request, 'account/login.html', {'extended_template': extended_template})
    else:
        extended_template = 'products/base.html'
        form = ProductForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.product_logo = request.FILES['product_logo']
            file_type = product.product_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'product': product,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                    'extended_template': extended_template
                }
                return render(request, 'products/post_product.html', context)
            product.save()
            return render(request, 'products/detail.html',
                          {'product': product, 'extended_template': extended_template, 'likes': "No"})
        context = {
            'form': form,
            'extended_template': extended_template,
            'error_message':0
        }

        return render(request, 'products/post_product.html', context)


def post_product(request):
    if not request.user.is_authenticated():
        extended_template = 'products/base_visitor.html'
    else:
        extended_template = 'products/base.html'
    template = 'products/post_product.html'
    return render(request, template, {'extended_template': extended_template})


def profile(request, user_name):
    extended_template = 'products/base.html'
    template = 'products/profile.html'
    user = request.user
    user_profile = get_object_or_404(User, pk=user.pk)
    user_products = Product.objects.filter(user=request.user)
    return render(request, template,
                  {'user': user_profile, 'user_products': user_products, 'extended_template': extended_template})


def load_more_user_products(request, user_name):
    extended_template = 'products/base.html'
    template = 'products/load_more_profile.html'
    user = request.user
    user_profile = get_object_or_404(User, pk=user.pk)
    user_products = Product.objects.filter(user=request.user)
    return render(request, template,
                  {'user': user_profile, 'user_products': user_products, 'extended_template': extended_template})


def delete_product(request, product_id):
    if not request.user.is_authenticated():
        extended_template = 'products/base_visitor.html'
    else:
        extended_template = 'products/base.html'
    template = 'products/load_more_profile.html'
    product = Product.objects.get(pk=product_id)
    product.delete()
    user = request.user
    user_profile = get_object_or_404(User, pk=user.pk)
    user_products = Product.objects.filter(user=request.user)
    return render(request, template,
                  {'user': user_profile, 'user_products': user_products, 'extended_template': extended_template})


def edit_product_page(request, product_id):
    extended_template = 'products/base.html'
    template = 'products/edit_product.html'
    product = Product.objects.get(pk=product_id)
    return render(request, template, {'product': product, 'extended_template': extended_template,
                                      'error_message':0 })


def edit_product(request, product_id):
    extended_template = 'products/base.html'
    form = ProductForm(request.POST or None, request.FILES or None)
    product = Product.objects.get(pk=product_id)
    product.title = request.POST.get('title',product.title)
    product.url = request.POST.get('url',product.url)
    product.category = request.POST.get('category', product.category)
    product.description = request.POST.get('description', product.description)
    product.product_logo = request.FILES.get('product_logo',product.product_logo)
    file_type = product.product_logo.url.split('.')[-1]
    file_type = file_type.lower()
    if file_type not in IMAGE_FILE_TYPES:
        context = {
            'product': product,
            'form': form,
            'error_message': 'Image file must be PNG, JPG, or JPEG',
            'extended_template': extended_template
        }
        return render(request, 'products/edit_product.html', context)
    product.save()
    return render(request, 'products/detail.html',
                  {'product': product, 'extended_template': extended_template, 'likes': "No"})


def search(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            search_text = request.POST['search_text']
            categories = Categories.objects.filter(category__contains=search_text)
        else:
            categories = []

    return render(request, 'products/ajax_search.html', {'categories': categories})


def search_result(request):
    if not request.user.is_authenticated():
        extended_template = 'products/base_visitor.html'
    else:
        extended_template = 'products/base.html'
    template = 'products/search_result.html'
    category = request.POST['search']
    if category == "All":
        category_products = Product.objects.all()
    else:
        category_products = Product.objects.filter(category__contains=category)
    return render(request, template, {'extended_template': extended_template, 'query': category,
                                      'category_products': category_products})


def main_search(request):
    if not request.user.is_authenticated():
        extended_template = 'products/base_visitor.html'
    else:
        extended_template = 'products/base.html'
    template = 'products/search_result.html'
    searchQuery = request.GET.get('q')
    products_list = wat.search(searchQuery)
    products = list()
    i = 0
    for product in products_list:
        productId = str(product.title).partition("- ")[2]
        object = Product.objects.get(pk=productId)
        products.insert(int(i), object)
        i += 1
    return render(request, template, {'extended_template': extended_template, 'query': searchQuery,
                                      'category_products': products})


def load_more(request, category):
    if not request.user.is_authenticated():
        extended_template = 'products/base_visitor.html'
    else:
        extended_template = 'products/base.html'
    template = 'products/search_result.html'
    products = Product.objects.all()
    if category == "New":
        newproducts = products.order_by("-created_at")
    else:
        newproducts = products.order_by("-hit_count_generic__hits")
    return render(request, template, {'extended_template': extended_template, 'query': category,
                                      'category_products': newproducts})
