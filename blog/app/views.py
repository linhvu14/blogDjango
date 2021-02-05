from django.shortcuts import render


def indexView(request):
    template = 'index.html'
    return render(request, template_name=template)

def registerView(request):
    template = 'register.html'
    return render(request, template_name=template)

def loginView(request):
    template = 'login.html'
    return render(request, template_name=template)