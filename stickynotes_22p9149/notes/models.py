# yahan ham apne app ke models banayenge, jisme ham apne database ke tables ko define karenge. 


# is line me ham django ke models module ko import kar rahe hain, jisme ham apne models ko define karenge.
from django.db import models

#User model hamare users ke data ko store karne ke liye use hota hai, jaise username, password, email, etc. 
from django.contrib.auth.models import User



# is line me ham apne Note model ko define kar rahe hain, jisme ham apne notes ke data ko store karenge. 
# Note model — yeh batata hai ke ek sticky note mein kya kya hoga

class Note(models.Model):

    # title field : yeh hamare note ka title hoga, jisme ham apne note ka naam denge
    # max_length=100 ka matlab hai ke hamare note ka title maximum 100 characters ka ho sakta hai
    title = models.CharField(max_length=200)

    # content field : yeh hamare note ka content hoga, jisme ham apne note ka main text likhenge
    # max_length=500 ka matlab hai ke hamare note ka content maximum 500 characters ka ho sakta hai
    content = models.TextField()

    # note ka background color
    color = models.CharField(max_length=7, default="#e8daef")

    # created_at field : yeh hamare note ke banne ki date aur time ko store karega
    # auto_now_add=True ka matlab hai ke jab bhi ham ek naya note banayenge, to yeh field 
    # automatically us date aur time ko store kar lega
    created_at = models.DateTimeField(auto_now_add=True)

    # updated_at field : yeh hamare note ke update hone ki date aur time ko store karega
    updated_at = models.DateTimeField(auto_now=True)

    # user field : yeh hamare note ke owner ko store karega, jisme ham User model ka use karenge
    # CASCADE ka matlab: agar user delete hua toh uske sab notes bhi delete ho jayenge
  
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_pinned = models.BooleanField(default=False)
    
    

    # __str__ method hamare note ka title return karega, taki jab ham apne notes ko
    # admin panel mein dekhenge, to hame apne notes ke titles dikhai denge, na ke unke IDs ya kuch aur.
    def __str__(self):
        return self.title


