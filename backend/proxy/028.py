import requests

def getapp_information(ip,etsiID):
  url="https://try-mec.etsi.org/"+etsiID+"mep1/wai/v2/queries/ap/ap_information"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.get(url)
  print(req)
  print(req.content)


def getsta_information(ip,etsiID):
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/wai/v2/queries/sta/sta_information"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.get(url)
  print(req)
  print(req.content)

def getSubscriptions(ip,etsiID):
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/wai/v2/subscriptions"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.get(url)
  print(req)
  print(req.content)

def getSubscriptionsID(ip,etsiID):
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/wai/v2/subscriptions/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.get(url)
  print(req)
  print(req.content)

def deletesubscriptionsID(ip,etsiID):
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/wai/v2/subscriptions/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.delete(url)
  print(req)
  print(req.content)

def postSubscriptions(ip,etsiID):
  f={
  "subscriptionType": "AssocStaSubscription",
  "callbackReference": "http://meAppClient.example.com/wai/v2/notifications/1",
  "apId": {
    "bssid": "005C0A0A0A0A"
  },
  "notificationEvent": {
    "threshold": 1,
    "trigger": 1
  }
}
  url = "https://try-mec.etsi.org/"+etsiID+"/mep1/wai/v2/subscriptions"
  url=url.replace("try-mec.etsi.org",ip)
  x = requests.post(url, json = f)
  print(x.content)



def putSubscriptionsID(ip,etsiID):
  f={
  "subscriptionType": "AssocStaSubscription",
  "callbackReference": "http://meAppClient.example.com/wai/v2/notifications/1",
  "_links": {
    "self": {
      "href": "http://meAppServer.example.com/wai/v2/subscriptions/sub123"
    }
  },
  "apId": {
    "bssid": "005C0A0A0A0A"
  },
  "notificationEvent": {
    "threshold": 1,
    "trigger": 1
  }
}
  url = "https://try-mec.etsi.org/"+etsiID+"/mep1/wai/v2/subscriptions/subscriptionID"
  url=url.replace("try-mec.etsi.org",ip)
  x = requests.put(url, json = f)
  
  print(x.content)