
from django.shortcuts import render
from .forms import ContactForm
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            #mail = form.cleaned_data['email']
            password = form.cleaned_data['password'] 
            return render(request, "success.html", {"username": username})
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})
