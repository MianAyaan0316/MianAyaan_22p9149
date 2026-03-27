# Django ke forms module ko import kar rahe hain
# forms module hamare liye forms banane ka kaam karta hai, taki ham apne users 
# se data le sakein, jaise ki note ka title, content, aur color.
from django import forms

# Note model hamare notes ke data ko store karta hai, jaise ki title, content, color, aur owner
from .models import Note


# NoteForm — yeh woh form hai jo user ko dikhega jab woh note banayega ya edit karega
# ModelForm ka matlab hai yeh form seedha hamare Note model se connected hai
# taki user apne note ka title, content, aur color fill kar sake.
class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        
        # sirf yeh teen fields user ko dikhenge

        fields = ['title', 'content', 'color','is_pinned']

        #CSS classes aur placeholders add kar rahe hain taki form zyada user friendly lage
        widgets = {
            # title ke liye ek simple text input
 
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter note title...',
            }),

            # content ke liye ek bara text area

            'content': forms.Textarea(attrs={
                'placeholder': 'Enter note content...',
                'rows': 5,
            }),

            # color ke liye ek color picker — user click karega aur color choose karega

            'color': forms.TextInput(attrs={
                'type': 'color',
            }),
        }