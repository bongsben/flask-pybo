from django.shortcuts import render
from django.http import HttpResponse
from ..models import Question, Answer, Comment
from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from ..forms import QuestionForm, AnswerForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.
def index(request):
    page = request.GET.get('page', '1')  # 페이지번호
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    #qusetion=Question.objects.get(id=question_id)
    content={'question':question}
    return render(request, 'pybo/question_detail.html', content)