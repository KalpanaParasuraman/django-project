from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import DocumentForm

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = DocumentForm()
    return render(request, 'fileupload/upload.html', {'form': form})

def success(request):
    return render(request, 'fileupload/success.html')