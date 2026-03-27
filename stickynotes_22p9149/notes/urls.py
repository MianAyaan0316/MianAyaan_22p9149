# ye file asaan lafzon me hamare notes app ke URLs ko define karti hai, yani ke hamare app ke 
# andar kaun kaun se pages honge aur unka URL kya hoga.


# Django ka path function import kar rahe hain — URLs define karne ke liye
# asaan lafzon me, path function hamare URLs ko define karne ke liye use hota hai, taki ham 
# apne app ke andar alag alag pages bana sakein, jaise ke note list page, note create page, etc.
from django.urls import path

# apne saare views import kar rahe hain notes app se
# asaan lafzon me, yeh line hamare notes app ke saare views ko import kar rahi hai, taki ham 
# unhe apne URLs mein use kar sakein, jaise ke note_list, note_create,
from . import views

# yahan saari URLs define hoti hain notes app ki
# asaan lafzon me, yeh urlpatterns list hamare notes app ke URLs ko define karti hai, yani ke 
# hamare app ke
urlpatterns = [

    # /notes/ — logged in user ke saare notes dikhao
    # asaan lafzon me, yeh line hamare notes app ke note_list view ko /notes/ URL se connect 
    # karti hai, taki jab user /notes/ URL par jaye, to usse apne saare notes dikhai den.
    path('notes/', views.note_list, name='note_list'),

    # /notes/new/ — naya note banane ka form dikhao
    # asaan lafzon me, yeh line hamare notes app ke note_create view ko /notes/new/ URL se connect 
    # karti hai, taki jab user /notes/new/ URL par jaye, to usse ek form dikhe jisme wo apne 
    # note ka title, content, aur color fill kar sakta hai, aur naya note bana sakta hai.
    path('notes/new/', views.note_create, name='note_create'),

    # /notes/3/edit/ — note number 3 ko edit karo (pk koi bhi number ho sakta hai)
    # asaan lafzon me, yeh line hamare notes app ke note_edit view ko /notes/<int:pk>/edit/ URL se connect 
    # karti hai, taki jab user /notes/3/edit/ URL par jaye
    path('notes/<int:pk>/edit/', views.note_edit, name='note_edit'),

    # /notes/3/delete/ — note number 3 ko delete karo
    # asaan lafzon me, yeh line hamare notes app ke note_delete view ko /notes/<int:pk>/delete/ URL se connect 
    # karti hai, taki jab user /notes/3/delete/ URL par jaye
    path('notes/<int:pk>/delete/', views.note_delete, name='note_delete'),

    # /register/ — naya user register karne ka page
    # asaan lafzon me, yeh line hamare notes app ke register_view view ko /register/ URL se connect 
    # karti hai, taki jab user /register/ URL par jaye, to usse ek registration form dikhe 
    # jisme wo apna username aur password fill karke naya account bana sakta hai.
    path('register/', views.register_view, name='register'),
]