from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from LedApp import utilities
def loginView(request):
    if request.user.is_authenticated:
        return redirect('mainView')
    else:
        if request.method == "GET":
            return render(request, 'login.html')
        else:
            if request.POST.get("auth"):
                user =  authenticate(request, username = request.POST['login'], password = request.POST['password'])
                if user is None:
                    return render(request,'login.html', {'error': 'Username or password did not match'})
                else:
                    try:
                        login(request, user)
                        return redirect('mainView')
                    except:
                        return render(request,'login.html', {'error': 'Something goes wrong !'})
            else:
                return render(request, 'login.html')
            

def mainView(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request,'main.html')
        else:
            if request.POST.get('act'):
                color = request.POST['color']
                brightness = request.POST['brightness']

                h_col = color.lstrip('#')
                rgb_col = tuple(int(h_col[i:i+2], 16) for i in (0, 2, 4))
                set_color = utilities.setColor(rgb_col,brightness)
                print(set_color)
                return render(request,'main.html')
            
            elif request.POST.get('mode1'):
                brightness = 0.5
                utilities.trainstion(brightness,20)
                return render(request,'main.html')
            
            elif request.POST.get('mode2'):
                brightness = 0.5
                utilities.rainbow_cycle(0.001,brightness)
                return render(request,'main.html')

                
    else:
        return redirect('loginView')