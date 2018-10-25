
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from polls.models import Question

def data(request):
    value = request.GET['user_name']
    return HttpResponse(value)

def vote(request):
    choice = request.POST['choice']
    print(choice)
    # 서버에서 투표를 완료하면 CMD 화면에서 on이라고 출력됨.
    return render(request, 'polls/vote.html', {})

def input(request):
    return render(request, 'polls/input.html', {})

def result(request, id):
    question = Question.objects.get(pk=id)
    return render(request, 'polls/result.html', {'question': question})

def detail(request, id):
    question = Question.objects.get(id=id)
    return render(request, 'polls/detail.html', {'item':question})

from django.utils import timezone
def add_question(request):
    text = request.POST['text']
    # q = Question(
    #     question_text=text,
    #     pub_date=timezone.now()
    # )
    # q.save()
    return HttpResponse('입력완료')

def index(request):
    list = Question.objects.all()
    return render(request, 'polls/index.html', {'question': list})
# list를 html에 넘길때 부여해주는 이름이 question !! 이해하기 어려운 부분.
