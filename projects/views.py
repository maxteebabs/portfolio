from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from . import models
# Create your views here.
def index(request):
    projects = models.Project.objects
    return render(request, 'projects/index.html', {'projects':projects})
def details(request, slug):
    project = models.Project.objects.get(slug=slug)
    # project = get_object_or_404(models.Project, pk=slug)
    return render(request, 'projects/details.html', {'project': project})
def contact(request):
    if(request.method == 'POST'):
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        message = request.POST.get("message","")
        body = "<p>Hello Admin,</p><p>Name: {}</p><p>Email {}</p>,<p>body {}</p><p>Regards</p>".format(name,email,message)
        # send email to owner
        if name and email and message:
            try:
                status = send_mail(
                    'Porfolio Platform', body, email,
                    ["maxteetechnologies@gmail.com"],
                    fail_silently=False, html_message=body,  
                    auth_user="muyiwa32145@gmail.com",
                    auth_password="muyiwa@321"
                )
                if(status):
                    messages.success(request, 'Email successfully saved.')
            except BadHeaderError:
                return HttpResponse("Invalid Header Found")
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
    return redirect('/')
