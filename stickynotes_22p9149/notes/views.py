# Django ke zaruri tools import kar rahe hain
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db import models
from .models import Note
from .forms import NoteForm


# VIEW 1: note_list logged in user ke saare notes dikhao
@login_required
def note_list(request):
    # search query URL se le rahe hain
    search_query = request.GET.get('search', '')

    # sirf is user ke notes fetch karo
    notes = Note.objects.filter(owner=request.user)

    # agar search query hai toh title ya content mein dhundo
    if search_query:
        notes = notes.filter(
            models.Q(title__icontains=search_query) |
            models.Q(content__icontains=search_query)
        )

    # pinned notes pehle dikhao phir baaki latest pehle
    notes = notes.order_by('-is_pinned', '-created_at')

    #  har page par 10 notes
    from django.core.paginator import Paginator
    paginator = Paginator(notes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'note_list.html', {
        'notes': page_obj,
        'search_query': search_query,
        'page_obj': page_obj,
    })


# VIEW 2: note_create — naya note banao
@login_required
def note_create(request):
    # agar user ne form submit kiya
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            # abhi save mat karo — pehle owner set karo
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'note_form.html', {'form': form, 'action': 'Create'})


# VIEW 3: note_edit — purana note edit karo
@login_required
def note_edit(request, pk):
    # sirf apna note edit kar sakta hai doosre ka nahi
    note = get_object_or_404(Note, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        # form mein purana data pehle se bhara hua dikhao
        form = NoteForm(instance=note)
    return render(request, 'note_form.html', {'form': form, 'action': 'Edit'})


# VIEW 4: note_delete note delete karo confirmation ke baad
@login_required
def note_delete(request, pk):
    # sirf apna note delete kar sakta hai
    note = get_object_or_404(Note, pk=pk, owner=request.user)
    if request.method == 'POST':
        # user ne confirm kar diya delete karo
        note.delete()
        return redirect('note_list')
    # pehle confirmation page dikhao
    return render(request, 'note_confirm_delete.html', {'note': note})


# VIEW 5: register_view naya user register karo
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # naya user save karo
            user = form.save()
            # register ke baad seedha login kar do
            login(request, user)
            return redirect('note_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
