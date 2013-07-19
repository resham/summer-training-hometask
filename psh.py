from cmd2 import Cmd
from getpass import getuser
import requests
import sys

__version__ = '0.1'

class Application(Cmd):
    """
    The main Application class
     
    """

    def __init__(self):
            Cmd.__init__(self)

    def do_hello(self, line):
            print "Hello:", line

    def do_sayit(self,line):
        print "Python Rocks!"

    def do_greet(self,line):
         print "hi,%s" % (getuser())

    def do_stockGOOG(self,line):
        r = requests.get("http://download.finance.yahoo.com/d/quotes.csv?s=GOOG&f=l1")
        data=r.text
        value=float(data)
        print value

if __name__ == '__main__':
        app = Application()
        app.cmdloop()

