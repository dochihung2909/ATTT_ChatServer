from django.contrib.auth import login # xác thực đăng nhập nguười dùng
from django.shortcuts import render, redirect
#render:dùng để tạo và trả về các templetaes có trong html, còn redirect là
#Redirect: dùng để cho user chuyển từ url này sang url khác

from .forms import SignUpForm

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})