from django.shortcuts import render

from . import forms


def home(request):
    return render(request, 'home.html')


def suggestion_view(request):
    form = forms.SuggestionForm()
    return render(request, 'suggestion_form.html', {'form': form})