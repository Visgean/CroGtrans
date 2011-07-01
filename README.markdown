	  ____            ____ _                       
	 / ___|_ __ ___  / ___| |_ _ __ __ _ _ __  ___ 
	| |   | '__/ _ \| |  _| __| '__/ _` | '_ \/ __|
	| |___| | | (_) | |_| | |_| | | (_| | | | \__ \
	 \____|_|  \___/ \____|\__|_|  \__,_|_| |_|___/
	                                               
Purpose:
========
	This is python library for google translation, advantage is that is baed on jabber so google will not block you for having too many requests...

What language can I use?
========================
	Those which are supported by google bot service - see the list at http://www.google.com/support/talk/bin/answer.py?hl=en&answer=89921

Usage:
===== 
'''python
	>>>from croGtrans import *
	>>>from getpass import getpass
	>>>trans = Translate(login=raw_input("Your jid: "), password=getpass(), languageFrom="cs", languageTo="en")
	>>>print trans.translate("Hovno kleslo")
	Shit fell
	>>>trans.setLanguage("es", "en")
	>>>print trans.translate("Buenos tardes")
	Good afternoon
'''

Requirements:
=============
	- xmpppy|xmpp|pyxmpp - install by sudo apt-get install python-pyxmpp
	- jabber account
	- access to internet
