import requests 



def getuu_unicast(ip,etsiID,subscriptionsID):
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/vis/v2/queries/uu_unicast_provisioning_info?location_info=%5Blocation1%2Clocation2%5D"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.delete(url)
  print(req.content)

def getSubscriptions(ip,etsiID,subscriptionsID):
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/vis/v2/subscriptions"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.delete(url)
  print(req.content)

def getSubscriptionsID(ip,etsiID,subscriptionsID):
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/vis/v2/subscriptions/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.delete(url)
  print(req.content)

def deletesubscriptionsID(ip,etsiID,subscriptionsID):
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/vis/v2/subscriptions/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.delete(url)
  print(req.content)

def postprovided_predicted(ip,etsiID,subscriptionsID):
  f={
  "locationGranularity": "string",
  "routes": [
    {
      "routeInfo": [
        {
          "location": {
            "ecgi": {
              "cellId": {
                "cellId": "string"
              },
              "plmn": {
                "mcc": "string",
                "mnc": "string"
              }
            },
            "geoArea": {
              "latitude": 0,
              "longitude": 0
            }
          },
          "rsrp": 0,
          "rsrq": 0,
          "time": {
            "nanoSeconds": 0,
            "seconds": 0
          }
        }
      ]
    }
  ],
  "timeGranularity": {
    "nanoSeconds": 0,
    "seconds": 0
  }
}
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/vis/v2/provide_predicted_qos"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.delete(url)
  print(req.content)


def post_v2x_message(ip,etsiID,subscriptionsID):
  f={
  "msgContent": "Hello World",
  "msgEncodeFormat": "base64",
  "msgType": 1,
  "stdOrganization": "ETSI"
}
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/vis/v2/publish_v2x_message"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.delete(url)
  print(req.content)

def postSubscriptions(ip,etsiID,subscriptionsID):
  f={
  "subscriptionType": "V2xMsgSubscription",
  "callbackReference": "http://my.callback.com/vis-v2x-msg/some-id",
  "filterCriteria": {
    "stdOrganization": "ETSI",
    "msgType": [
      1,
      2
    ]
  },
  "expiryDeadline": {
    "seconds": 1977836800,
    "nanoseconds": 0
  }
}
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/vis/v2/subscriptions"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.delete(url)
  print(req.content)

def putsubscriptionsID(ip,etsiID,subscriptionsID):
  f={
  "subscriptionType": "V2xMsgSubscription",
  "callbackReference": "http://my.callback.com/vis-v2x-msg/some-id",
  "_links": {
    "self": {
      "href": "http://meAppServer.example.com/vis/v2/subscriptions/123"
    }
  },
  "filterCriteria": {
    "stdOrganization": "ETSI",
    "msgType": [
      3,
      4
    ]
  },
  "expiryDeadline": {
    "seconds": 1977836800,
    "nanoseconds": 0
  }
}
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/vis/v2/subscriptions/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.delete(url)
  print(req.content)