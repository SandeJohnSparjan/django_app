#creating class based views
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from home.forms import HomeForm
from home.models import Post, Friend
from django.urls import reverse
from django.contrib.auth.models import User


class HomeView(TemplateView):
    template_name ='home/home.html'
    #defining a form to render it in template
    def get(self, request):
        form = HomeForm()
        #retrieving info from DB
        posts = Post.objects.all().order_by('-created')

        #excluding the user who is requesting
        users = User.objects.exclude(id=request.user.id)

        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()

        args = {'form':form, 'posts':posts, 'users':users, 'friends': friends}
        return render(request, self.template_name, args )

    def post(self,request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            #make form empty again
            form = HomeForm()
            return redirect(reverse('home:accounty'))

        args =  {'form':form, 'text':text}
        return render(request, self.template_name, args)


def friendship(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation=='add':
        Friend.make_friend(request.user,friend)
    elif operation=='remove':
        Friend.un_friend(request.user,friend)

    return redirect(reverse('home:accounty'))