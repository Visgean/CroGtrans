#! /usr/bin/python
# -*- coding: UTF-8 -*-

# @author: 	Visgean Skeloru 
# email: 	<visgean@gmail.com>
# jabber: 	<visgean@jabber.org>
# github: 	http://github.com/Visgean


import xmpp
import random
import re

class __Translation__:
    translated = False
    id = random.randint(4444, 7777)
    translatedVersion = ""
    
    def __init__(self, text):
        self.original = text
        
    def getMessage(self):
        "This method returns text created from translation and id which can be send to google translate"
        return "<%s>%s<%s>" % (self.id, self.original, self.id) 
        
    def setTranlation(self, translation):
        "If translation is related to original text it returns True and sets translation to object"
        reg = re.compile(r"\<(?P<id>\d*)\>(?P<text>.*)\<(\d*)\>", re.DOTALL)
        assert re.match(reg, "<33>hoven<33>") # tests regexp
        
        match = re.match(reg, translation)
        
        if not match:
            return False
                
        if int(match.group("id")) == self.id:
            self.translatedVersion = match.group("text")
            self.translated = True
            
        return self.translated
        
class Translate:
    "Main class for translating, probably udes "
    def __init__(self, login, password, languageFrom="cs", languageTo="en", server = None, debug = False):
        """{Login: jid@server, language.*: code name for language(cs,en,ru), 
        server:(adress, ip), debug:sets xmpp debuging mode}"""
        
        self.debug = debug
        
        self.setLanguage(languageFrom, languageTo)
        
        self.__login__(login, password, server)
        
        self.client.sendInitPresence()
        self.client.RegisterHandler("message", self.__newMsg__)
        
        self.translation = "" # Variable to store translation - changed by _newMsg and returned by translation

    def __login__(self, login, password, server):
        "Login to jabber account"
        jid = xmpp.JID(login)
        domain = jid.getDomain()
        
        if domain == "gmail.com" and not server: # gtalk requires special settings
            server=('talk.google.com',5223)
        
        if not self.debug: # if debug is not set
            self.client = xmpp.Client(domain, debug=[])
        else:
            self.client = xmpp.Client(domain)

        if server: # if there is special settings for connecting to server
            conn = self.client.connect( server=server)
        else:
            conn = self.client.connect()
        if not conn:
            raise xmpp.HostUnknown # unable to connect to server

        auth = self.client.auth(jid.getNode(), password, 'croGtrans')
        
        if not auth:
            raise xmpp.NotAuthorized

    def __language2jid__(self, original, new):
        "Determines google bot from given languages: example: es2en@bot.talk.google.com"
        return "%s2%s@bot.talk.google.com" % (original, new)
        
    
    def __sentTrans__(self, text):
        "Sents text to translate to google bot"
        self.client.send( xmpp.Message(self.googleBot, body = text, typ="chat" ) )
        
    def __getMessage__(self):
        "Waits for exactly one message"
        while not self.messageAccepted:
            self.client.Process(2) # wait 1s between checking
        return self.newMessage # handler was called and  set this variable...
            
        
    def __newMsg__(self, conn, msg):
        "New message handler"
        if msg.getFrom() == self.googleBot:
            self.messageAccepted = True # Translation was accepted, don´t check anymore
            self.newMessage = msg.getBody() 
        
    def setLanguage(self, languageFrom, languageTo): 
        "Public method for language settings of instance."
        self.googleBot = self.__language2jid__(languageFrom, languageTo)
       
    def translate(self, text):
        "Translate given text"
        translation = __Translation__(text)
        
        numberOfAttepts = 0
        while numberOfAttepts < 10:            
            self.messageAccepted = False  # we are waiting for new translation
            self.__sentTrans__(translation.getMessage())  # send  text to google
            trans = self.__getMessage__() # waits for translation
            
            if translation.setTranlation(trans):
                return translation.translatedVersion
            else:
                numberOfAttepts += 1
        
        if numberOfAttepts >= 10:
            raise LookupError


