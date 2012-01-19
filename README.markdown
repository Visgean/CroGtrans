	  ____            ____ _                       
	 / ___|_ __ ___  / ___| |_ _ __ __ _ _ __  ___ 
	| |   | '__/ _ \| |  _| __| '__/ _` | '_ \/ __|
	| |___| | | (_) | |_| | |_| | | (_| | | | \__ \
	 \____|_|  \___/ \____|\__|_|  \__,_|_| |_|___/
	                                               
Purpose:
========
This is python library for google translation, 
advantage is that is based on jabber so google 
wlil not block you for having too many requests...

What language can I use?
========================
Those which are supported by google bot service
see the list at [google list of translation bots](http://goo.gl/UYPNB)
	
Usage:
===== 
```python
>>>from croGtrans import *
>>>from getpass import getpass
>>>trans = Translate(login=raw_input("Your jid: "), password=getpass(), languageFrom="cs", languageTo="en")
>>>print trans.translate("Hovno kleslo")
Shit fell
>>>trans.setLanguage("es", "en")
>>>print trans.translate("Buenos tardes")
Good afternoon
```


Requirements:
=============

- xmpppy|xmpp|pyxmpp - install by sudo apt-get install python-xmpp
- jabber account
- access to internet :)

License
=======
Licensed under http://creativecommons.org/licenses/by/3.0/

