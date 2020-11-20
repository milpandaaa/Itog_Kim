from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .models import *
from .forms import *


class MyRegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/accounts/login/"

    template_name = "index.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


def newBook(request):
    context = {}
    form = BookForm(request.POST or None)
    context['data'] = Book.objects.all()
    if form.is_valid():
        form.save()
        context = {'data': Book.objects.order_by("name")}
        return render(request, 'books.html', context)
    context['form'] = form
    return render(request, "newBook.html", context)


def newReader(request):
    context = {}
    form = ReaderForm(request.POST or None)
    context['data'] = Reader.objects.all()
    print(form.is_valid())
    print(form)
    if form.is_valid():
        form.save()
        context = {'data': Reader.objects.order_by("name")}
        return render(request, 'menu.html', context)
    context['form'] = form
    return render(request, "newReader.html", context)


def menu(request):
    context = {'data': Reader.objects.order_by("name")}
    return render(request, 'menu.html', context)


def books(request):
    context = {'data': Book.objects.order_by("name")}
    return render(request, 'books.html', context)


def reader(request, reader_id):
    try:
        context = {'data_r': Reader.objects.get(pk=reader_id), 'data_b': Book.objects.all(),
                   'data_c': Card.objects.all()}
    except User.DoesNotExist:
        raise Http404("Пользователя не сущетсвует")
    return render(request, 'account.html', context)


def card(request, reader_id):
    context = {}
    form = CardForm(request.POST or None)
    context = {'data_r': Reader.objects.get(pk=reader_id), 'data_b': Book.objects.all(),
               'data_c': Card.objects.all()}
    if form.is_valid():
        form.save()
        text = {'data_r': Reader.objects.get(pk=reader_id), 'data_b': Book.objects.all(),
                   'data_c': Card.objects.all()}
        return render(request, 'account.html', text)
    context['form'] = form
    return render(request, "card.html", context)


def delete(request, book_id):
    try:
        c = Book.objects.get(id=book_id)
        c.delete()
        context = {'data': Book.objects.order_by("name")}
        return render(request, 'books.html', context)
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>Book not found</h2>")
# Create your views here.
