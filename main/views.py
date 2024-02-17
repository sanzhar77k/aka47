from django.shortcuts import render, get_object_or_404, redirect
from .models import MyBlogs
from .models import Interiors
from .models import Exteriors
from .forms import CommentForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.conf import settings
import requests
from django.views.decorators.csrf import csrf_exempt




def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def services(request):
    return render(request, 'main/services.html')


def contact(request):
    return render(request, 'main/contact.html')


# def interior(request):
#     return render(request, 'main/projects.html')


def exterior(request):
    return render(request, 'main/exterior.html')


def blog_page(request):
    blog_entries = MyBlogs.objects.all()
    return render(request, 'main/blog.html', {'blog_entries': blog_entries})


def blog_detail(request, blog_id):
    blog = get_object_or_404(MyBlogs, pk=blog_id)
    comments = blog.comments.all()
    return render(request, 'main/eachBlog.html', {'blog': blog, 'comments': comments})



def add_comment(request, blog_id):
    blog = get_object_or_404(MyBlogs, pk=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('blog_detail', blog_id=blog_id)
    else:
        form = CommentForm()
    
    return render(request, 'main/eachBlog.html', {'blog': blog, 'form': form})


def interior_page(request):
    interior_entries = Interiors.objects.all()
    return render(request, 'main/projects.html', {'interior_entries': interior_entries})



def interior_detail(request, interior_id):
    interior = get_object_or_404(Interiors, pk=interior_id)
    return render(request, 'main/projectSignle.html', {'interior': interior, 'interior_id': interior_id})


def exterior_page(request):
    exterior_entries = Exteriors.objects.all()
    return render(request, 'main/exterior.html', {'exterior_entries': exterior_entries})


def exterior_detail(request, exterior_id):
    exterior = get_object_or_404(Exteriors, pk=exterior_id)
    return render(request, 'main/projectExterior.html', {'exterior': exterior, 'exterior_id': exterior_id})


# @csrf_exempt
# def contact_form(request):
#     if request.method == 'POST':
#         name = request.POST.get('Name')
#         phone_number = request.POST.get('PhoneNumber')
#         message = request.POST.get('Message')

#         # Словарь с данными, которые вы хотите отправить в Google Forms
#         form_data = {
#             'Имя': name,
#             'Номер': phone_number,
#             'Вопрос': message
#         }

#         print(form_data)  # Отладочный вывод

#         # URL вашей Google Forms
#         google_forms_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfF7QyxMNwVMx8J7tBeO_JhjXrX-KD9rqonmbL9qgnj3cQH-A/viewform?usp=sf_link'

#         # Отправка данных в Google Forms
#         response = requests.post(google_forms_url, data=form_data)

#         # Перенаправление на страницу с благодарностью после успешной отправки формы
#         if response.status_code == 200:
#             print(response.text)
#             return render(request, 'main/contact.html')
#         else:
#             print(response.text)
#             return render(request, 'main/services.html')

#     return render(request, 'main/contact.html')