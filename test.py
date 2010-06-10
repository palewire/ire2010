import sys, urllib2, urllib

url = 'http://localhost:8000/polls/1/vote/'

recommend = "1"
data = urllib.urlencode([('data', recommend)])
req = urllib2.Request(url)
fd = urllib2.urlopen(req, data)
while 1:
    data = fd.read(1024)
    if not len(data):
        break
    sys.stdout.write(data)
