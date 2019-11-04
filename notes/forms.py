from django import forms
from notes.models import Notes, NotesItem


class NotesForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ['title', 'body']

# class NotesItemForm(forms.ModelForm):

    # class Meta:
    #     model = NotesItem
    #     fields = ['body']
