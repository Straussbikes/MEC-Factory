import requests 
def getrab_info(ip,etsiID):
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/rni/v2/queries/rab_info"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.get(url)
  print(req.content)


def getplmn_info(ip,etsiID):
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/rni/v2/queries/plmn_info?app_ins_id=listofApp"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.get(url)
  print(req.content)

def getlayer2_meas(ip,etsiID):
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/rni/v2/queries/layer2_meas?app_ins_id=appID"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.get(url)
  print(req.content)

def getsubscriptions(ip,etsiID):
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/rni/v2/subscriptions"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.get(url)
  print(req.content)

def getsubscriptionsID(ip,etsiID,subscriptionID):
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/rni/v2/subscriptions/subcriptionID"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.get(url)
  print(req.content)



def postSubscriptions(ip,etsiID):
  f={
  "subscriptionType": "CellChangeSubscription",
  "callbackReference": "http://my.callback.com/rni-cell-change/some-id",
  "filterCriteriaAssocHo": {
    "appInstanceId": "myApp",
    "associateId": [
      {
        "type": 1,
        "value": "10.100.0.1"
      }
    ],
    "ecgi": [
      {
        "plmn": {
          "mnc": "01",
          "mcc": "001"
        },
        "cellId": "ACBDEFA"
      }
    ],
    "hoStatus": [
      1,
      2
    ]
  },
  "expiryDeadline": {
    "seconds": 1977836800,
    "nanoseconds": 0
  }
}
  url = "https://try-mec.etsi.org/"+etsiID+"/mep1/rni/v2/subscriptions"
  url=url.replace("try-mec.etsi.org",ip)
  x = requests.post(url, json = f)
  print(x.content)



def putSubscriptionsID(ip,etsiID,subscriptionID):
  f={
  "subscriptionType": "CellChangeSubscription",
  "callbackReference": "http://my.callback.com/rni-cell-change/some-id",
  "_links": {
    "self": {
      "href": "http://meAppServer.example.com/rni/v2/subscriptions/sub123"
    }
  },
  "filterCriteriaAssocHo": {
    "appInstanceId": "myApp",
    "associateId": [
      {
        "type": 1,
        "value": "10.100.0.1"
      }
    ],
    "ecgi": [
      {
        "plmn": {
          "mnc": "01",
          "mcc": "001"
        },
        "cellId": "ACBDEFA"
      }
    ],
    "hoStatus": [
      1,
      2
    ]
  },
  "expiryDeadline": {
    "seconds": 1977836800,
    "nanoseconds": 0
  }
}
  url = "https://try-mec.etsi.org/"+etsiID+"/mep1/rni/v2/subscriptions/subscriptionID"
  url=url.replace("try-mec.etsi.org",ip)
  x = requests.put(url, json = f)
  print(x.content)




def deletesubscriptionsID(ip,etsiID,subscriptionsID):
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/rni/v2/subscriptions/subscriptionsID"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.delete(url)
  print(req.content)
