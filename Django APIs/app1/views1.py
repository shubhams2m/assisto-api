from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
@csrf_protect
def myname(request):
    if request.method == "POST":
        name=request.POST['myname']
        
        if name:
            print "inside if "
            res=bot_script(name)
            return render(request, "abc.html" , {'res':res})
    elif request.method=="GET":
        return render(request, "abc.html")
    


def bot_script(name):
    
    from chatterbot import ChatBot
    c=ChatBot('jaanu123')    
    from chatterbot.trainers import ListTrainer
    conversation=['hi','hello...welcome','what is your name','i am chatbox']
    c.set_trainer(ListTrainer)
    c.train(conversation) 
    return c.get_response(name)
