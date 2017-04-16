from sys import stdout
from os import system as term

uname = raw_input("USERNAME: ") # read input from stdin until [Enter] in 2
stdout.write("PASSWORD: ")
term("stty -echo") # turn echo off
try:
    passwd = raw_input()
except KeyboardInterrupt: # ctrl+c pressed
    raise SystemExit("Password attempt interrupted")
except EOFError: # ctrl+d pressed
    raise SystemExit("Password attempt interrupted")
finally:
    term("stty echo") # turn echo on again

print "username:", uname
print "password:", "*" * len(passwd)
