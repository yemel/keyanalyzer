import json
from django.shortcuts import render
from django.http import HttpResponse

from core.engine import KeywordAnalyzer


def home(request):
    return render(request, 'index.html')


def analyze(request):
    keyword = request.POST['keyword']
    language = request.POST['language']

    analyzer = KeywordAnalyzer(keyword, language).run()

    response = json.dumps(analyzer.suggestions)
    return HttpResponse(response, content_type="application/json")
