from django.db import models


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
# question을 shell에서 호출하면 실제 데이터 값을 출력하도록 설정한 것.


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # ForeignKey로 위의 Q테이블과 C테이블을 연결시킴. 그렇기 때문에 c.question 입력하면 연결된 데이터 조회 가능.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
