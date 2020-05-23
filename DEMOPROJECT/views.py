from django.shortcuts import redirect

#to make login page as the homepage
def login_redirect(request):
    return redirect('/accounts/login/')