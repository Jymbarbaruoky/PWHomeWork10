from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import TagForm, AuthorForm, QuoteForm
from .models import Author, Quote


def main(request):
    quotes = Quote.objects.all().order_by('-id')
    paginator = Paginator(quotes, 10)
    return render(request, 'quotes_app/index.html', context={'page_obj': paginator.get_page(request.GET.get('page')), "title": "Quotes"})


@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes_app:main")
    return render(request, 'quotes_app/add_author.html', {"form": AuthorForm()})


def author(request, author: str):
    return render(request, 'quotes_app/author.html', context={"author": Author.objects.get(fullname=author)})


@login_required
def quote(request):

    if request.method == 'POST':
        form = QuoteForm(request.POST)

        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.save()
            form.save_m2m()
            return redirect(to='quotes_app:main')
        else:
            return render(request, 'quotes_app/add_quote.html', {'form': form})
    return render(request, 'quotes_app/add_quote.html', {"form": QuoteForm()})


@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes_app:main')
        else:
            return render(request, 'quotes_app/add_tag.html', {'form': form})

    return render(request, 'quotes_app/add_tag.html', {'form': TagForm()})
