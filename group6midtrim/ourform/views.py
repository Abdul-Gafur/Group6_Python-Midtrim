from django.shortcuts import render

from ourform.models import Message

# Create your views here.
def index(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        save_data = Message.objects.create(name=name,email=email,subject=subject,message=message)
    return render(request, 'start_wacitc/message.html')