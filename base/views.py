from django.shortcuts import render,redirect
from base.models import Comments

# Create your views here.
def home(request):
    comments=Comments.objects.all()
   
    return render(request,'base/index.html',{"cmt":comments})

def addcomment(request):
    if request.method== 'POST':
        text= request.POST['cmt']
        email = request.POST['email']
        user= Comments.objects.create(text=text,email=email)
        user.save()
        return redirect('/')

        
