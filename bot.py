import nltk
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import random
import string
from datetime import datetime

dt = datetime(2020, 1, 1)

f=open('nlp python answer finals.txt','r',errors = 'ignore')
m=open('modules pythons.txt','r',errors = 'ignore')
checkpoint = "./chatbot_weights.ckpt"

raw=f.read()
rawone=m.read()
raw=raw.lower()
rawone=rawone.lower()
nltk.download('punkt')
nltk.download('wordnet')
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)
sent_tokensone = nltk.sent_tokenize(rawone)
word_tokensone = nltk.word_tokenize(rawone)


sent_tokens[:2]
sent_tokensone[:2]

word_tokens[:5]
word_tokensone[:5]

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

Introduce_Ans = ["My name is ChatBotX.","My name is ChatBotX you can called me pi.","Im ChatBotX :) ","My name is ChatBotX. and my nickname is pi and i am happy to solve your queries :) "]
GREETING_INPUTS = ("hello", "hi","hiii","hii","hiiii","hiiii", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hey, hi this is ChatBotX!", "Hi this is ChatBotX, how can I help?", "hii there", "hello", "I am glad! You are talking to me"]
Basic_Q = ("what is python ?","what is python","what is python?","what is python.")
Basic_Ans = "Python is a high-level, interpreted, interactive and object-oriented scripting programming language python is designed to be highly readable It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages."
Basic_Om = ("what is module","what is module.","what is module ","what is module ?","what is module?","what is module in python","what is module in python.","what is module in python?","what is module in python ?")
Basic_AnsM = ["Consider a module to be the same as a code library.","A file containing a set of functions you want to include in your application.","A module can define functions, classes and variables. A module can also include runnable code. Grouping related code into a module makes the code easier to understand and use."]
Abuse = ["stupid", "idiot", "asshole", "fucker", "ass"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def basic(sentence):
    for word in Basic_Q:
        if sentence.lower() == word:
            return Basic_Ans

def basicM(sentence):
    for word in Basic_Om:
        if sentence.lower() == word:
            return random.choice(Basic_AnsM)

def IntroduceMe(sentence):
    return random.choice(Introduce_Ans)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def additionalResp(user_response):
    for insult in Abuse:
        if(insult in user_response):
            return 'Please don\'t insult me'
    if('love' in user_response):
        return 'I love you too'
    elif('time' in user_response):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        return 'The current time is: '+current_time
    elif('name' in user_response):
        return 'My name is ChatBotX'
    elif('age' in user_response):
        return 'I\'m 5184000000 milliseconds old (2 months :D )'
    else:
        return False

def response(user_response):
    for insult in Abuse:
        if(insult in user_response):
            return 'Please don\'t insult me'
    if('love' in user_response):
        return 'What we call love is nothing but a chemical reaction happening inside our head'
    elif('time' in user_response):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        return 'The current time is: '+current_time
    elif('name' in user_response):
        return 'My name is ChatBotX'
    elif('age' in user_response):
        return 'I\'m 5184000000 milliseconds old (2 months :D )'
    elif('life' in user_response):
        return 'Life is a beautiful game'
    elif('death' in user_response):
        return 'I\'m not afraid of death'
    elif('like' in user_response):
        return 'Chatting and running (Since programs \'run\' :p)'
    elif('yeah' in user_response):
        return 'Cool'
    elif('yes' in user_response):
        return 'Nice'
    elif('sweet' in user_response):
        return 'Neat'
    elif('made' in user_response or 'create' in user_response or 'creator' in user_response or 'develop' in user_response):
        return 'ChatBotX Developers\n1.Rahul Sharma\n2.Samyak Pawar\n3.Ashray Parmar\n3.Shubhankar Pawar'
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

def responseone(user_response):
    for insult in Abuse:
        if(insult in user_response):
            return 'Please don\'t insult me'
    if('love' in user_response):
        return 'What we call love is nothing but a chemical reaction happening inside our head'
    elif('time' in user_response):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        return 'The current time is: '+current_time
    elif('name' in user_response):
        return 'My name is ChatBotX'
    elif('age' in user_response):
        return 'I\'m 5184000000 milliseconds old (2 months :D )'
    elif('life' in user_response):
        return 'Life is a beautiful game'
    elif('death' in user_response):
        return 'I\'m not afraid of death'
    elif('like' in user_response):
        return 'Chatting and running (Since programs \'run\' :p)'
    elif('yeah' in user_response):
        return 'Cool'
    elif('yes' in user_response):
        return 'Nice'
    elif('sweet' in user_response):
        return 'Neat'
    elif('made' in user_response or 'create' in user_response or 'creator' in user_response or 'develop' in user_response):
        return 'ChatBotX Developers\n1.Rahul Sharma\n2.Samyak Pawar\n3.Ashray Parmar\n3.Shubhankar Pawar'
    robo_response=''
    sent_tokensone.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensone)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokensone[idx]
        return robo_response


def chat(user_response):
    user_response=user_response.lower()
    keyword = " module "
    keywordone = " module"
    keywordsecond = "module "
    
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            return "You are welcome.."
        elif(basicM(user_response)!=None):
            return basicM(user_response)
        else:
            if(user_response.find(keyword) != -1 or user_response.find(keywordone) != -1 or user_response.find(keywordsecond) != -1):
                return responseone(user_response)
                sent_tokensone.remove(user_response)
            elif(greeting(user_response)!=None):
                return greeting(user_response)
            elif(user_response.find("your name") != -1 or user_response.find(" your name") != -1 or user_response.find("your name ") != -1 or user_response.find(" your name ") != -1):
                return IntroduceMe(user_response)
            elif(basic(user_response)!=None):
                return basic(user_response)
            else:
                return response(user_response)
                sent_tokens.remove(user_response)
                
    else:
        flag=False
        return "Bye! take care.."
        
        

