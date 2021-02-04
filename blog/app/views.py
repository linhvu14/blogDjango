from django.shortcuts import render


def newView(request):
    template = 'index.html'





    
    return render(request, template_name=template)
