from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.all().prefetch_related('scope').order_by(ordering)
    context = {'object_list': articles}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
