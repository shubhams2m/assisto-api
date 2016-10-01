from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def myname(request):
    if request.method == "GET":
        name=request.GET["name"]
        if name:
            
            result=bot_script(name)
            data = {'response' : str(result)}
####            json_data = json.dumps(dict1)
            return HttpResponse(json.dumps(data), content_type='application/json')
##    elif request.method=="GET":
##        data = {'response' : ""}
####        json_data = json.dumps(dict1)
##        return HttpResponse(json.dumps(data), content_type='application/json')
    


def bot_script(name):
    
    from chatterbot import ChatBot
    c=ChatBot('jaanu123')    
    from chatterbot.trainers import ListTrainer
    conversation=['hi','hello...welcome','what is your name','i am chatbox']
    c.set_trainer(ListTrainer)
    c.train(conversation) 
    return c.get_response(name)
