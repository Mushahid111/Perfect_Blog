from django.shortcuts import render,redirect,HttpResponse
from authentication.models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import FeedbackForm


def BASE(request):
    return render(request,'main/base.html')

def INDEX(request):

   latest_post =Post.objects.order_by('-id')[0:12]
   
   
   context = {
        
        'latest_post':latest_post,
        
        
    }
       
   return render(request,'main/index.html',context)

def BLOG(request):
   popular_post =Post.objects.order_by('-id')[0:40]
   editorpick_post =Post.objects.filter(section='Editor_Pick').order_by('-id')[0:9]
   recent_post =Post.objects.filter(section='Recent').order_by('-id')[0:9]
   trending_post =Post.objects.filter(section='Trending').order_by('-id')[0:9]
   inspirational_post =Post.objects.filter(section='Inspiration').order_by('-id')[0:9]
   latest_post =Post.objects.filter(section='Latest Posts').order_by('-id')[0:9]
   main_post =Post.objects.filter(main_post=True)[0:40]
   
   context = {
        'popular_post':popular_post,
        'editorpick_post':editorpick_post,
        'recent_post':recent_post,
        'trending_post':trending_post,
        'inspirational_post':inspirational_post,
        'latest_post':latest_post,
        'main_post':main_post,
        
    }
    
   return render(request,'main/blog.html',context)






def SINGLE_BLOG(request,id):
    post = Post.objects.filter(id=id)
    
    context = {
         'post':post,
    }

    return render(request,'main/single_blog.html',context)

def About(request):
    return render(request,'main/about_us.html')

# blogms/views.py



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base')  # Redirect to your home page or another destination
    else:
        form = UserCreationForm()

    return render(request, 'main/single_blog.html', context)

    # return render(request, 'signup.html', {'form': form})


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Save the feedback to the database
            feedback = form.save()

            # You can perform additional actions here, such as sending emails, etc.

            return redirect('home') # Redirect to a thank you page or home page

    else:
        form = FeedbackForm()

    return render(request, 'main/feedback.html', {'form': form})


