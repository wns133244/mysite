
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]

#  mysite urls에서 polls url을 모두 포함해서 가져왔고 polls라고 입력할때 polls.url을 불러옴.

