from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def counter_view(request):
    # ----- SESSION -----
    # Get the current count from session, default = 0
    count = request.session.get('count', 0)

    # If button is clicked (POST), increase the counter
    if request.method == "POST":
        count += 1
        request.session['count'] = count  # Save back to session

    username = request.COOKIES.get('username', 'Kalpana')

    response = render(request, "sessiondemo/counter.html", {
        'count': count, 'username': username,  })

    # Set a cookie if not already set
    if 'username' not in request.COOKIES:
        response.set_cookie('username', 'Kalpana')

    return response
    
