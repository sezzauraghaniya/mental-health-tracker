from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2306207291',
        'name': 'Sezza Auraghaniya Winanda',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
