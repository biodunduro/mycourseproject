from django import forms

from .models import PublicNotice, Entry


class PublicNoticeForm(forms.ModelForm):
	class Meta:
		model = PublicNotice
		fields = ['title', 'body']
		labels = {'title': 'Title', 'body': 'Body Text'}


class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		label = {'text': ''}
