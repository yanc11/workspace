# -*- encoding: utf-8 -*-
import urllib2, re, base64, json
from urlparse import urlparse 

theurl = 'http://api.weibo.com/2/place/nearby_timeline.json?source=76764149&lat=40&long=116.328&count=3' 

username = '18810311482'
password = 'yanchen1995'

base64string = base64.encodestring('%s:%s' % (username, password))[:-1] #注意哦，这里最后会自动添加一个\n
authheader =  "Basic %s" % base64string
req = urllib2.Request(theurl)
req.add_header("Authorization", authheader)
try:
    handle = urllib2.urlopen(req)
except IOError, e:
    # here we shouldn't fail if the username/password is right
    print "It looks like the username or password is wrong."
    exit()
thepage = handle.read()
print json.dumps(json.loads(thepage), indent=4, ensure_ascii = False)