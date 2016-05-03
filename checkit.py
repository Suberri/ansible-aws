import httplib
import os
import sys
import json
import pdb


connTimeout=3
elbInfoFileName="./elb-info"

def checkResult(rcvCode, expectedCode,errorMsg):
    try:
        assert rcvCode==expectedCode
        print "  SUCCESS"
    except:
        print "   test failed"
        print errorMsg

def testConn(expectedCode):
    try:
        conn.request("GET", "/")
        r1 = conn.getresponse()
        checkResult(r1.status,expectedCode, r1.reason)
    except Exception as e:
        print e
        print "     Test failed"    
 
 
 
 
#
# gwet the system url 
#
with open(elbInfoFileName) as dFile:    
    elbInfo = json.load(dFile)
#
# Check the https url
#
print "Testing https"
conn = httplib.HTTPSConnection(elbInfo["dns_name"],timeout=connTimeout)
testConn(200)


#
# Check the http url
#
print "Testing http redirect"
conn = httplib.HTTPConnection(elbInfo["dns_name"],timeout=connTimeout)
testConn(301)




