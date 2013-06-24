import json
from django.shortcuts import render
from django.http import HttpResponse
from django import forms

from core.engine import KeywordAnalyzer
from core.models import Keyword


class SearchForm(forms.Form):
    keyword = forms.CharField()
    language = forms.CharField()

    def clean_keyword(self):
        return self.cleaned_data['keyword'].lower()

    def process(self):
        keyword = self.cleaned_data['keyword']
        language = self.cleaned_data['language']

        search = Keyword.objects.filter(keyword=keyword)
        search = search[0] if search.exists() else Keyword.objects.create(keyword=keyword, hits=0)

        search.hits += 1
        search.save()

        return KeywordAnalyzer(keyword, language).run()


def home(request):
    ideas = Keyword.objects.order_by('hits')[:7]
    return render(request, 'index.html', {'ideas': ideas})


def analyze(request):
    form = SearchForm(request.POST)
    if form.is_valid():
        analyzer = form.process()
        response = json.dumps(analyzer.suggestions)
        return HttpResponse(response, content_type="application/json")

    return HttpResponse("[]", content_type="application/json")
