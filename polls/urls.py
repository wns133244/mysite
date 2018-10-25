from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('result/<int:id>', views.result),
    path('data', views.data),
    path('<int:id>', views.detail, name='detail22'),
    path('vote/', views.vote, name='vote'),
    # vote뒤에 /를 붙혀서 검색하면 /가 출력됨.
    path('input', views.input, name='input'),
    # 뒤에 /를 안 붙히면 input 까지가 아닌 그 앞경로까지를 의미.
    path('add_question', views.add_question, name='add_question'),
]

# views에 생성한 index 함수를 위처럼 아무것도 입력 안했을때 불러오도록 설정했고 그걸 mysite.url이 포함해버림


