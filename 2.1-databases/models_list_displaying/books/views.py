from django.shortcuts import render


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def books_list(request):
    template = 'books/books_list.html'
    with open("D:\Учеба в IT\Django/third_lesson\models_list_displaying/fixtures/books.json",
              'r', encoding='utf-8') as f:
        data = json.load(f)
    books = []
    for x in data:
        book = Book(name=x['fields']['name'],
                    author=x['fields']['author'],
                    pub_date=x['fields']['pub_date'])
        book.save()
        books.append(book)
    context = {'books': books}
    return render(request, template, context)


def books_list_in_date(request, pub_date):
    template = 'books/books_list_in_date.html'
    books = Book.objects.all().filter(pub_date=pub_date)
    all_books = Book.objects.all().order_by('pub_date')
    all_pub_dates = list(set([f'{x.pub_date}' for x in all_books]))
    if all_pub_dates.index(pub_date) != 0 and all_pub_dates.index(pub_date) != int(len(all_pub_dates) - 1):
        prev_page = str(all_pub_dates[int(all_pub_dates.index(pub_date) - 1)])
        next_page = str(all_pub_dates[int(all_pub_dates.index(pub_date) + 1)])
    elif all_pub_dates.index(pub_date) == 0:
        prev_page = str(all_pub_dates[int(len(all_pub_dates) - 1)])
        next_page = str(all_pub_dates[int(all_pub_dates.index(pub_date) + 1)])
    elif all_pub_dates.index(pub_date) == int(len(all_pub_dates) - 1):
        prev_page = str(all_pub_dates[int(all_pub_dates.index(pub_date) - 1)])
        next_page = str(all_pub_dates[0])
    paginator = Paginator(all_pub_dates, 1)
    page = paginator.page(int(all_pub_dates.index(pub_date) + 1))
    context = {'books': books,
               'page': page,
               'prev_page': prev_page,
               'next_page': next_page}
    return render(request, template, context)
