from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


#Most common types are GET requests, there are also POST requests. We are adding a conditional where if it is a POST 
#request, we will validate the form data.
#We are adding a flashed message, which only shows up once, when a account is created. Then it will redirect us to home page

def register(request):
    if request.method== 'POST':
        form = UserRegisterForm(request.POST)
        #we could user UserCreationForm but we created our own UserRegisterForm
        if form.is_valid():
            form.save()
            #saves the user, password will be hashed and secure
            username=form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

'''
Many different types of messages:
messages.debug   
messages.info
messages.warning
messages.error
'''

@login_required
#imported a decorated, adds functionality to our profile view where the user needs to be logged in to see profile page
#pass in info in the forms with instances
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
            #we are redirecting instead of letting it render, called post get redirect pattern
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
