from django.shortcuts import render, get_object_or_404, redirect
from .models import Books, Categoey
from .forms import BookForm, CatForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()

        add_cat = CatForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()

    context = {
        'books': Books.objects.all(),
        'category': Categoey.objects.all(),
        'form': BookForm(),
        'formcat': CatForm(),
        'all_books': Books.objects.filter(active=True).count(),
        'sold_books': Books.objects.filter(status='sold').count(),
        'rent_books': Books.objects.filter(status='rental').count(),
        'availabe_books': Books.objects.filter(status='availabe').count(),

    }
    return render(request, 'pages/index.html', context)


def books(request):
    search = Books.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)

    context = {
        'category': Categoey.objects.all(),
        'books': search,
    }

    return render(request, 'pages/books.html', context)


def update(request, id):
    instance = Books.objects.get(id=id)
    if request.method == 'POST':
        instance = BookForm(request.POST, request.FILES, instance=instance)
        if instance.is_valid():
            instance.save()
            return redirect('/')
    else:
        instance = BookForm(instance=instance)
    
    return render (request, 'pages/update.html', {'form': instance})


def delete(request, id):
    delete_book = get_object_or_404(Books, id=id)
    if request.method == 'POST':
        delete_book.delete()
        return redirect ('/')
    
    return render(request, 'pages/delete.html')


