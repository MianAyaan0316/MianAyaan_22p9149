# yeh hamare poore project ki main URL file hai
# yahan se saari requests aati hain aur sahi jagah forward hoti hain


#yeh line hamare project ke admin panel ke URLs ko define karti hai, taki jab 
# user /admin/ URL par jaye, to usse Django ka built-in admin panel dikh
from django.contrib import admin

# path aur include import kar rahe hain
from django.urls import path, include

# Django ka built-in login aur logout system import kar rahe hain

from django.contrib.auth import views as auth_views


# yahan saari URLs define hoti hain project ki

urlpatterns = [

    # /admin/ — Django ka built-in admin panel
    path('admin/', admin.site.urls),

    # baaki saari URLs notes app ki urls.py file mein hain
 
    path('', include('notes.urls')),

    # /login/ — Django ka built-in login page

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # /logout/ — Django ka built-in logout

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]