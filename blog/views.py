from django.http import HttpResponse 
# Create your views here.
def blog(request):
    return HttpResponse("Blog Page 1")