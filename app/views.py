from django.shortcuts import render
from .models import Project,Languages,Profile
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect
from django.conf import settings
from .forms import ContactForm
# Create your views here.

def index(request):
    projects = Project.objects.all()
    all_languages = Languages.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            email_message = form.cleaned_data['message']
            print(name)
            print(email)
            print(email_message)
            # try:
            #     send_mail(name, #subject
            #     email_message, #message
            #     email, #form email
            #     ['unknownknowns32@gmail.com'] #To email 
            #     )
            #     print(name)
            #     print(email)
            #     print(email_message)
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')
        return HttpResponseRedirect(request.path_info)
    else:    
        form = ContactForm()
    context = {
        "form": form,
        "projects":projects,
        "all_languages":all_languages,
    }
    
    return render(request,"index.html",context)








