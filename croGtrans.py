#! /usr/bin/python
# -*- coding: UTF-8 -*-

# @author: 	Visgean Skeloru 
# email: 	<visgean@gmail.com>
# jabber: 	<visgean@jabber.org>
# github: 	http://github.com/Visgean


import xmpp


class Translate:
    "Main class for translating, probably udes "
    def __init__(self, login, password, languageFrom="cs", languageTo="en", server = None, debug = False):
        """{Login: jid@server, language.*: code name for language(cs,en,ru), 
        server:(adress, ip), debug:sets xmpp debuging mode}"""
        
        self.debug = debug
        
        self.setLanguage(languageFrom, languageTo)
        
        self._login(login, password, server)
        
        self.client.sendInitPresence()
        self.client.RegisterHandler("message", self._newMsg)
        
        self.messageAccepted = 0 # if we have accepted translation
        self.translation = "" # Variable to store translation - changed by _newMsg and returned by translation

    def _login(self, login, password, server):
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

    def _language2jid(self, original, new):
        "Determines google bot from given languages: example: es2en@bot.talk.google.com"
        return "%s2%s@bot.talk.google.com" % (original, new)
        
    
    def _sentTrans(self, text):
        "Sents text to translate to google bot"
        self.client.send( xmpp.Message(self.googleBot, body = text, typ="chat" ) )
        
    def _waitForMessage(self):
        "Waits for exactly one message"
        while not self.messageAccepted:
            self.client.Process(2) # wait 1s between checking
            
        
    def _newMsg(self, conn, msg):
        "New message handler"
        
        self.messageAccepted = True # Translation was accepted, don´t check anymore
        text = msg.getBody()     # get main text of the message
        self.translation = text
        
    def setLanguage(self, languageFrom, languageTo): 
        "Public method for language settings of instance."
        self.googleBot = self._language2jid(languageFrom, languageTo)
    
    
    def translate(self, text):
        "Translate given text"
        self.messageAccepted = False  # we are waiting for new translation
        self._sentTrans(text)  # send  text to google
        self._waitForMessage() # waits for translation
        return self.translation # self.translation was set by _newMsg, now we have to return it


