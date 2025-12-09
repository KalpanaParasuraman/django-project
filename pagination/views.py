from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Student

def student_list(request):
    data = Student.objects.all()

    paginator = Paginator(data, 5)   # show 5 records per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pagination/student_list.html', {'page_obj': page_obj})
