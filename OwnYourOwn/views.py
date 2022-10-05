from django.shortcuts import render
from django.core.mail import send_mail

def homepage(request):

    if request.method == 'POST':
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message_project = request.POST['message_project']
        message_budget = request.POST['message_budget']
        message_details = request.POST['message_details']


        #SEND EMAIL
        send_mail(
            'OWN YOUR OWN - NEW CONTRACT: ',
            'Hi, my name is ' 
            + message_name +
            '. I want to work on a '
            + message_project + 
            ' website . My budget is '
            + message_budget + 
            '. Here is more details: ' 
            + message_details,
            message_email,
            ['a-s.augustin@hotmail.com'],
        )

 
        context = { 'message_name':message_name
            }
        return render(request, 'homepage.html', context)
    else:
        context = {
            }
        return render(request, 'homepage.html', context)
        


