from django.contrib import messages
from django.shortcuts import render, redirect


from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Web, App, Card, testimony, ContactModel
from  .  import forms
from .forms import CONTACTFORM
"""
class BlogView(generic.ListView):
    template_name ='mainweb/blog.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.order_by('-date_added')[:10]
        
        


def sample(request):
    rooms = Room.objects.all()
    
    context = {'rooms': rooms}
    return render(request, "base\sample.html", context)
    
    class indexView(generic.ListView):
    template_name ='index.html'
    context_object_name = 'pro'
    def get_queryset(self):
        return Project.objects.order_by('-start_date')[:10]"""

# Create your views here.



def indexView(request):
    webs = Web.objects.order_by('-start_date')[:100]
    #card= Card.objects.order_by('-start_date')[:100]
    apps = App.objects.order_by('-start_date')[:100]
    testimonys = testimony.objects.order_by('-created')[:100]
    form = CONTACTFORM()
    if request.method =='POST':
        form = CONTACTFORM(request.POST, request.FILES )
        if form.is_valid():
            #form= form.save(commit=False)
            form.save()
            messages.success(request, ('thank for contact us'))
        else:
            messages.error(request, ' an error occur in the submitions ')
        return redirect('index')


    context = {'webs': webs,
               'form': form,
               'apps': apps,
               'testimonys':testimonys}
    return render(request, "index.html", context)
def blogdetail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context ={'post' : post}
    return render(request, "portfolio-detail.html", context)
