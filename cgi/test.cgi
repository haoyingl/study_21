#!/usr/bin/python3

import cgitb
import cgi
cgitb.enable()

print("Content-Type: text/html")    # HTML is following
print()

form = cgi.FieldStorage()
if "name" not in form or "addr" not in form:
    print("<H1>Error</H1>")
    print("Please fill in the name and addr fields.")
else :
    print("<p>name:", form["name"].value)
    print("<p>addr:", form["addr"].value)



