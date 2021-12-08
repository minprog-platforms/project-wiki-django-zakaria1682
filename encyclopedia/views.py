from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


from . import util

from django import forms

class NameForm(forms.Form):
    title = forms.CharField(label='title')
    content = forms.CharField(label='content')


def index(request):
    return render(request, "encyclopedia/wiki.html", {
        "entries": util.list_entries(),
    })



def entry(request, title):
    return render(request, "encyclopedia/all.html", {
        "entry": util.get_entry(title),
    })



def search(request):
    input = request.GET.get('search')
    if input in util.list_entries():   
        return render(request, 'encyclopedia/search.html', {
            "Entry": util.get_entry(input),
        }) 
    else:
        return redirect('/wiki')
         



def create(request):
    if request.method == 'POST':
        form =NameForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            util.save_entry(title, content)
            return redirect("entry", title)

    return render(request, "encyclopedia/create.html", {
        "form": NameForm()
    })
        


