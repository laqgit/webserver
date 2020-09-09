#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb, os , subprocess
cgitb.enable()
# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
link = form.getvalue('link')
filename = form.getvalue('filename')
type = form.getvalue('type')
# stream = os.popen('echo Returned output')
# output = stream.read()
os.system("echo Hello from the other side!")
if(type=="wget"):
    ls = os.system("echo wget -c -o " + filename + " " + link + ">> downloads/wget/dl-wget.txt")
elif (type=="axel"):
    ls = os.system("echo axel -o " + filename + " " + link + ">> downloads/axel/dl-axel.txt")
elif (type == "youtube"):
    ls = os.system("echo youtube "  + link +" >> downloads/youtube/dl-youtube.txt")
elif (type == "m3u8"):
    ls = os.system("echo ffmpeg -i "+ link +" -c copy -bsf:a aac_adtstoasc " + filename  ">> downloads/m3u8/dl-m3u8.txt")



print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>WEBSERVER 2</title>"
print "</head>"
print "<body>"
print "<h1>WEBSERVER 2</h1>"
print "<h2>getting %s </h2>" %link
print "<h2>ls= %s </h2>" %ls
if (ls == 0):
    print "<h2>link is added  %s</h2>" %link
else:
    print "<h2>false</h2>"

print "</body>"
print "</html>"
