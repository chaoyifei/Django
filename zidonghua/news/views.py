from django.shortcuts import render
from .models import NewsBody

def index(request):
    news_body=NewsBody.objects.all()[:6]
    return render(request,'news_index.html',{'news_body':news_body})
def article(request, news_body_id=''):
    news_content = NewsBody.objects.get(id=news_body_id)
    return render(request, 'view.html', {'news_content': news_content})
