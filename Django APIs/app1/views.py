from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import imdb
#import pandas as pd
#from sklearn.linear_model import LogisticRegression
#X=pd.read_csv('gen.csv')
#y=X['hit']
#X=X.drop('hit','reviews')
@csrf_exempt
def myname(request):
    if request.method == "GET":
        name=request.GET["name"]
        if name:
##            if "should_i_watch" in name:
##                x1=name[15:]
##                ia1=imdb.IMDb()
##                s_result1=ia1.search_movie(x1)
##                the_unt1=s_result1[0]
##                ia1.update(the_unt1)
##                a,b=str(the_unt1['rating']),str(the_unt1['genres'])
##                result1= "aagya bc"
##                data1 = {'response': str(result1)}
##                return HttpResponse(json.dumps(data1), content_type='application/json')
    
            if "movie_details" in name:
                
                x=name[15:]
                
                ia = imdb.IMDb() # by default access the web.
                s_result = ia.search_movie(x)
                the_unt = s_result[0]
                ia.update(the_unt)
                a,b= str(the_unt['rating']),str(the_unt['genres'])

                #result=x
                result = "rating is " + a + " and " + "genre of movie is " + b+" .To book a movie type movie_book"
                data = {'response': str(result)}
                return HttpResponse(json.dumps(data), content_type='application/json')


            
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
    c=ChatBot('Assisto', read_only=True)    
    from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
    conversation=['hi','hello...welcome','what is your name','i am chatbox']
    c.set_trainer(ChatterBotCorpusTrainer)
    c.train("chatterbot.corpus.english") 
    return c.get_response(name)
