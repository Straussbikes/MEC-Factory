import socket
import pickle
from time import sleep
import requests


#analisar semantica do pedido 

#application Suport
#pedidos Get

def getservices():
  req=requests.get("http://0.0.0.0:8000/mac_service_mgmt/v1/services")
  print(req)
  print(req.content)


#Application Suport confirmTermination

#                                                   MEC APP SUPORT

#appTrafficRules
# asd=Mec app instance
def getTraffic_rules(ip,appinstance):
  url="http://0.0.0.0:8000/mec_app_support/v1/applications/asd/traffic_rules"
  url=url.replace("asd",appinstance)
  url=url.replace("0.0.0.0:8000",ip)
  req=requests.get(url)
  print(req)
  print(req.content)

def getTraffic_rulesID(ip,appinstance,trafficinstance,email):
  url="http://0.0.0.0:8000/"+email+"/mec_app_support/v1/applications/asd/traffic_rules"
  url=url.replace("asd",appinstance)
  url=url.replace("rule",trafficinstance)
  url=url.replace("0.0.0.0:8000",ip)
  req=requests.get(url)
  print(req)
  print(req.content)

def putTraffic_rulesID(ip,appinstance,trafficinstance,email):
  f={
 "trafficRuleId": "string",
  "filterType": "FLOW",
  "priority": 0,
  "trafficFilter": [
    {
      "srcAddress": [
        "string"
      ],
      "dstAddress": [
        "string"
      ],
      "srcPort": [
        "string"
      ],
      "dstPort": [
        "string"
      ],
      "protocol": [
        "string"
      ],
      "token": [
        "string"
      ],
      "srcTunnelAddress": [
        "string"
      ],
      "tgtTunnelAddress": [
        "string"
      ],
      "srcTunnelPort": [
        "string"
      ],
      "dstTunnelPort": [
        "string"
      ],
      "qCI": 0,
      "dSCP": 0,
      "tC": 0
    }
  ],
  "action": "DROP",
  "dstInterface": [
    {
      "interfaceType": "TUNNEL",
      "tunnelInfo": {
        "tunnelType": "GTP_U",
        "tunnelDstAddress": "string",
        "tunnelSrcAddress": "string"
      },
      "srcMacAddress": "string",
      "dstMacAddress": "string",
      "dstIpAddress": "string"
    }
  ],
  "state": "ACTIVE"
}
  url = "http://0.0.0.0:8000/"+email+"/mec_app_support/v1/applications/asd/traffic_rules/rule"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("rule",trafficinstance)
  url=url.replace("asd",appinstance)
  x = requests.put(url, json = f)
  print(x.content)


def getDNS_rules(ip,appinstance,email):
  url="http://0.0.0.0:8000/"+email+"/mec_app_support/v1/applications/asd/dns_rules"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  req=requests.get(url)
  print(req)
  print(req.content)

def getDNS_rulesID(ip,appinstance,email):
  url="http://0.0.0.0:8000/"+email+"/mec_app_support/v1/applications/asd/dns_rules/dns"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  req=requests.get(url)
  print(req)
  print(req.content)

def putDNS_rulesID(ip,appinstance,json,rule,email):
  f={
  "dnsRuleId": "string",
  "domainName": "string",
  "ipAddressType": "IP_V6",
  "ipAddress": "string",
  "ttl": 0,
  "state": "ACTIVE"
} 
  url = "http://0.0.0.0:8000/"+email+"/mec_app_support/v1/applications/asd/dns_rules/rule"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  url=url.replace("rule",rule)
  x = requests.put(url, json = f)
  print(x.content)




def getSubscriptions(ip,appinstance,email):
  url="http://0.0.0.0:8000/"+email+"/mec_app_support/v1/applications/asd/subscriptions"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  req=requests.get(url)
  print(req)
  print(req.content)

def postSubscriptions(ip,appinstance,email):
  f={
  
  "subscriptionType": "string",
  "callbackReference": "string",
  "_links": {
    "self": {
      "href": "string"
    }
  },
  "appInstanceId": "string"

}
  url = "http://0.0.0.0:8000/"+email+"/mec_app_support/v1/applications/asd/subscriptions"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  x = requests.post(url, json = f)
  #print(x)
  print(x.content)


def getSubscriptionsID(ip,appinstance,subs,email):
  url="http://0.0.0.0:8000/"+email+"/mec_app_support/v1/applications/asd/subscriptions/subscription"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  url=url.replace("subscription",subs)
  req=requests.get(url)
  print(req)
  print(req.content)

def delSubscriptions(ip,appinstance,subs,email):
  url="http://0.0.0.0:8000/"+email+"/mec_app_support/v1/applications/asd/subscriptions/a"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  url=url.replace("a",subs)
  req=requests.delete(url)
  print(req)
  print(req.content)

def postConfirmT(ip,appinstance,json,email):
  f={
  "operationAction": "TERMINATING"
}
  url = "http://0.0.0.0:8000/"+email+"/mec_app_support/v1/applications/asd/confirm_termination"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  x = requests.post(url, json = f)
  print(x.content)




def postconfirmR(ip,appinstance,json,email):
  f={
    "indication": "READY"
  } 
  url = "http://0.0.0.0:8000/"+email+"/mec_app_support/v1/applications/asd/confirm_ready"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  x = requests.post(url, json = f)
  print(x.content)



def getTiming_caps(ip,email):
  url="http://0.0.0.0:8000/"+email+"/mec_app_support/v1/timing/timing_caps"
  url=url.replace("0.0.0.0:8000",ip)
  req=requests.get(url)
  print(req)
  print(req.content)

def getCurrent_Time(ip,email):
  url="http://0.0.0.0:8000/"+email+"/mec_app_support/v1/timing/current_time"
  url=url.replace("0.0.0.0:8000",ip)
  req=requests.get(url)
  print(req)
  print(req.content)


                            #  MEC SERVICE MANAGEMENT



def getSubscriptionsserv(ip,appinstance,email):
  url="http://0.0.0.0:8000/"+email+"/mec_service_mgmt/v1/applications/asd/subscriptions"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  req=requests.get(url)
  print(req)
  print(req.content)

def getSubscriptionsIDserv(ip,appinstance,subs,eamil):
  url="http://0.0.0.0:8000/"+email+"/mec_service_mgmt/v1/applications/asd/subscriptions/subs"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  url=url.replace("subs",subs)
  req=requests.get(url)
  print(req)
  print(req.content)

def postSubscriptions(ip,appinstance,email):
  url = "http://0.0.0.0:8000/"+email+"/mec_service_mgmt/v1/applications/11/subscriptions"
  f={
      "subscriptionType": "string",
      "callbackReference": "string",
      "_links": {
        "self": {
          "href": "string"
        }
      },
      "filteringCriteria": {
        "serInstanceIds": [
          "string"
        ],
        "serNames": [
          "string"
        ],
        "serCategories": [
          {
            "href": "string",
            "id": "string",
            "name": "string",
            "version": "string"
          }
        ],
        "states": [
          "ACTIVE"
        ],
        "isLocal": True
      }
    }
    
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("11",appinstance)
  x = requests.post(url, json = f)
  print(x)
  print(x.content)


def delSubscriptionsId(ip,appinstance,subs,email):
  url="http://0.0.0.0:8000/"+email+"/mec_app_support/v1/applications/asd/subscriptions/123"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  url=url.replace("123",subs)
  x= requests.delete(url)
  print(x)
  print(x.content)





def postService(ip,appinstance,email):
   f={
   
   }
    
   url = "http://0.0.0.0:8000/"+email+"/mec_service_mgmt/v1/applications/asd/services"
   url=url.replace("0.0.0.0:8000",ip)
   url=url.replace("asd",appinstance)
   x = requests.post(url, json = f)
   print(x)
   print(x.content)

def getServiceID(ip,appinstance,service,email):
  url="http://0.0.0.0:8000/"+email+"/mec_service_mgmt/v1/applications/asd/services/123"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  url=url.replace("123",service)
  req=requests.get(url)
  print(req)
  print(req.content)



def putServiceID(ip,appinstance,service,email):
   f={
  "serInstanceId": "string",
  "serName": "string",
  "serCategory": {
    "href": "string",
    "id": "string",
    "name": "string",
    "version": "string"
  },
  "version": "string",
  "state": "ACTIVE",
  "transportInfo": {
    "id": "string",
    "name": "string",
    "description": "string",
    "type": "REST_HTTP",
    "protocol": "string",
    "version": "string",
    "security": {
      "oAuth2Info": {
        "grantTypes": [
          "OAUTH2_AUTHORIZATION_CODE"
        ],
        "tokenEndpoint": "string"
      }
    },
    "implSpecificInfo": {}
  },
  "serializer": "JSON",
  "scopeOfLocality": "MEC_SYSTEM",
  "consumedLocalOnly": true,
  "isLocal": true,
  "livenessInterval": 0,
  "_links": {
    "self": {
      "href": "string"
    },
    "liveness": {
      "href": "string"
    }
  }
}
   url = "http://0.0.0.0:8000/"+email+"/mec_service_mgmt/v1/applications/asd/services/123"
   url=url.replace("0.0.0.0:8000",ip)
   url=url.replace("asd",appinstance)
   url=url.replace("123",service)
   x = requests.post(url, json = f)
   print(x)
   print(x.content)


def delServiceID(ip,appinstance,service,email):
  url="http://0.0.0.0:8000/"+email+"/mec_service_mgmt/v1/applications/asd/services/123"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  url=url.replace("123",service)
  req=requests.delete(url)
  print(req)
  print(req.content)





def getServices(ip,email):
  url="http://0.0.0.0:8000/"+email+"/mec_service_mgmt/v1/services"
  url=url.replace("0.0.0.0:8000",ip)
  req=requests.get(url)
  print(req)
  
  print(req.content)



def getServiceID(ip,appinstance,email):
  url="http://0.0.0.0:8000/"+email+"/mec_service_mgmt/v1/services/asd"
  url=url.replace("asd",appinstance)
  url=url.replace("0.0.0.0:8000",ip)
  req=requests.get(url)
  print(req)
  print(req.content)




def getTransport(ip,email):
  url="http://0.0.0.0:8000/"+email+"/mec_service_mgmt/v1/transports"
  url=url.replace("0.0.0.0:8000",ip)
  req=requests.get(url)
  print(req)
  print(req.content)








def getIndividualMECservice(ip,email):
  url="http://0.0.0.0:8000/"+email+"/mec_service_mgmt/v1/resource_uri_allocated_by_MEC_platform"
  url=url.replace("0.0.0.0:8000",ip)
  req=requests.get(url)
  print(req)
  print(req.content)





def patchlive(ip,email):
  f={
      "state": "ACTIVE"
  }
  url="http://0.0.0.0:8000/"+email+"/mec_service_mgmt/v1/resource_uri_allocated_by_MEC_platform"
  url=url.replace("0.0.0.0:8000",ip)
  x=requests.patch(url,json=f)
  print(x)
  print(x.content)




def getDistance(ip,etsiID):
  f={
    "requester":"mep1",
    "address": "10.10.0.1",
    "latitude":"43.737087",
    "longitude":"7.421007"
  }
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/queries/distance?requester=mep1&address=10.10.0.1"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.get(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def postSubscriptionsCircle(ip,etsiID):
  f={
    "circleNotificationSubscription": {
    "clientCorrelator": "0123",
    "callbackReference": {
      "callbackData": "1234",
      "notifyURL": "http://my.callback.com/location-area-circle/some-id"
    },
    "address": [
      "10.100.0.4"
    ],
    "checkImmediate": True,
    "enteringLeavingCriteria": "Entering",
    "frequency": 1,
    "latitude": 43.748993,
    "longitude": 7.437573,
    "radius": 200,
    "trackingAccuracy": 10
  }
  }
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/area/circle"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.post(url,json=f)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)
  


def getUsers(ip,etsiID):
  url="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/queries/users"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.get(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)


def getZones(ip,etsiID):
  url="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/queries/zones"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.get(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)


def getZonesID(ip,etsiID,exampleID):
  url="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/queries/zones/exampleid"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.get(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)


def getZonesIDAccesPoints(ip,etsiID):
  url="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/queries/zones/exampleID/accessPoints"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.get(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)




def getZonesIDAccessPointsID(ip,etsiID):
  url="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/queries/zones/exampleZone/accessPoints/accespointID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.get(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)




def getcircle(ip,etsiID):
  url="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptiuns/area/circle"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.get(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def getcircleID(ip,etsiID,exampleID):
  url="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/area/circle/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.get(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)




def getsubscriptionDistance(ip,etsiID):
  url="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/distance"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.get(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def getsubscriptionDistanceID(ip,etsiID,exampleID):
  url="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/distance/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.get(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def getsubscriptionsPeriodic(ip,etsiID):
  url="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/periodic"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.get(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def getsubscriptionperiodicID(ip,etsiID,exampleID):
  url="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/periodic/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.get(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def getsubscriptionUserTracking(ip,etsiID):
  url="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/userTracking"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.get(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def getsubscriptionUserTrackingID(ip,etsiID,exampleID):
  url="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/userTracking/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.get(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def getzonalTraffic(ip,etsiID):
  url="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/zonalTraffic"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.get(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def getzonalTrafficID(ip,etsiID,exampleID):
  url="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/zonalTraffic/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.get(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def getzoneStatus(ip,etsiID):
  url="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/zoneStatus"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.get(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def getzoneStatusID(ip,etsiID,exampleID):
  url="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/zoneStatus/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.get(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def putsubscriptioncircleID(ip,json,etsiID,exampleID):
  f={
  "circleNotificationSubscription": {
    "clientCorrelator": "0123",
    "callbackReference": {
      "callbackData": "1234",
      "notifyURL": "http://my.callback.com/location-area-circle/some-id"
    },
    "address": [
      "10.100.0.4"
    ],
    "checkImmediate": true,
    "enteringLeavingCriteria": "Entering",
    "frequency": 1,
    "latitude": 43.748993,
    "longitude": 7.437573,
    "radius": 200,
    "resourceURL": "http://[hostIP]/sbox-xyz123/location/v2/subscriptions/area/circle/subscription123",
    "trackingAccuracy": 10
  }
}
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/area/circle/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.put(url,json=f)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def deletesubscriptioncircleID(ip,etsiID,exampleID):
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/area/circle/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.delete(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)


def putsubscriptiondistanceID(ip,json,etsiID,exampleID):
  f={
  "distanceNotificationSubscription": {
    "clientCorrelator": "0123",
    "callbackReference": {
      "callbackData": "1234",
      "notifyURL": "http://my.callback.com/location-distance/some-id"
    },
    "monitoredAddress": [
      "10.10.0.1",
      "10.1.0.1"
    ],
    "checkImmediate": true,
    "criteria": "AllWithinDistance",
    "distance": 100,
    "frequency": 10,
    "referenceAddress": [
      "10.100.0.1"
    ],
    "resourceURL": "http://[hostIP]/sbox-xyz123/location/v2/subscriptions/distance/subscription123",
    "trackingAccuracy": 10
  }
}
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/distance/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.put(url,json=f)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def deletesubscriptionDistanceID(ip,etsiID,exampleID):
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/distance/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.delete(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def putsubscriptionPeriodicID(ip,json,etsiID,exampleID):
  f={
  "periodicNotificationSubscription": {
    "address": [
      "string"
    ],
    "callbackReference": {
      "callbackData": "string",
      "notificationFormat": "XML",
      "notifyURL": "string"
    },
    "clientCorrelator": "string",
    "duration": 0,
    "frequency": 0,
    "link": [
      {
        "href": "string",
        "rel": "string"
      }
    ],
    "requestedAccuracy": 0,
    "requester": "string",
    "resourceURL": "string"
  }
}
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/periodic/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.put(url,json=f)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def deletesubscriptionPeriodicID(ip,etsiID,exampleID):
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/periodic/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.delete(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def putsubscriptionUserTrackingID(ip,json,etsiID,exampleID):
  f={
  "userTrackingSubscription": {
    "clientCorrelator": "0123",
    "resourceURL": "http://[hostIP]/sbox-xyz123/location/v2/subscriptions/userTracking/subscription123",
    "callbackReference": {
      "notifyURL": "http://my.callback.com/location-user-tracking/some-id"
    },
    "address": "10.100.0.1",
    "userEventCriteria": [
      "Entering"
    ]
  } 
} 
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/userTracking/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.put(url,json=f)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def deletesubscriptionUserTrackingID(ip,etsiID,exampleID):
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/userTracking/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.delete(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def putsubscriptionzonalTrafficID(ip,json,etsiID,exampleID):
  f={
  "zonalTrafficSubscription": {
    "clientCorrelator": "0123",
    "resourceURL": "http://[hostIP]/sbox-xyz123/location/v2/subscriptions/zonalTraffic/subscription123",
    "callbackReference": {
      "notifyURL": "http://my.callback.com/location-zonal-traffic/some-id"
    },
    "zoneId": "zone01",
    "userEventCriteria": [
      "Entering"
    ]
  }
}
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/zonalTraffic/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.put(url,json=f)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def deletesubscriptionzonalTrafficID(ip,etsiID,exampleID):
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/zonalTraffic/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.delete(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def putsubscriptionzoneStatusID(ip,jsonm,etsiID,exampleID):
  f={
  "zoneStatusSubscription": {
    "clientCorrelator": "0123",
    "resourceURL": "http://[hostIP]/sbox-xyz123/location/v2/subscriptions/zoneStatus/subscription123",
    "callbackReference": {
      "notifyURL": "http://my.callback.com/location-zonal-status/some-id"
    },
    "zoneId": "zone01",
    "numberOfUsersZoneThreshold": 3,
    "operationStatus": [
      "Serviceable"
    ]
  }
}
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/zoneStatus/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.put(url,json=f)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)



def deletesubscriptionzoneStatusID(ip,etsiID,exampleID):
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/zoneStatus/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.delete(url)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)

def postsubscriptionsareacircle(ip,jsonm,etsiID,exampleID):
  f={
  "circleNotificationSubscription": {
    "clientCorrelator": "0123",
    "callbackReference": {
      "callbackData": "1234",
      "notifyURL": "http://my.callback.com/location-area-circle/some-id"
    },
    "address": [
      "10.100.0.4"
    ],
    "checkImmediate": true,
    "enteringLeavingCriteria": "Entering",
    "frequency": 1,
    "latitude": 43.748993,
    "longitude": 7.437573,
    "radius": 200,
    "trackingAccuracy": 10
  }
}
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/area/circle"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.post(url,json=f)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)

def postsubscriptionszoneStatus(ip,jsonm,etsiID,exampleID):
  f={
  "zoneStatusSubscription": {
    "clientCorrelator": "0123",
    "callbackReference": {
      "notifyURL": "http://my.callback.com/location-zonal-status/some-id"
    },
    "zoneId": "zone01",
    "numberOfUsersZoneThreshold": 3,
    "operationStatus": [
      "Serviceable"
    ]
  }
}
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/zoneStatus"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.post(url,json=f)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)


def postsubscriptiondistance(ip,jsonm,etsiID,exampleID):
  f={
  "distanceNotificationSubscription": {
    "clientCorrelator": "0123",
    "callbackReference": {
      "callbackData": "1234",
      "notifyURL": "http://my.callback.com/location-distance/some-id"
    },
    "monitoredAddress": [
      "10.10.0.1",
      "10.1.0.1"
    ],
    "checkImmediate":True,
    "criteria": "AllWithinDistance",
    "distance": 100,
    "frequency": 10,
    "referenceAddress": [
      "10.100.0.1"
    ],
    "trackingAccuracy": 10
  }
}
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/distance"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.post(url,json=f)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)


def postsubscriptionperiodic(ip,jsonm,etsiID,exampleID):
  f={
  "periodicNotificationSubscription": {
    "address": [
      "string"
    ],
    "callbackReference": {
      "callbackData": "string",
      "notificationFormat": "XML",
      "notifyURL": "string"
    },
    "clientCorrelator": "string",
    "duration": 0,
    "frequency": 0,
    "link": [
      {
        "href": "string",
        "rel": "string"
      }
    ],
    "requestedAccuracy": 0,
    "requester": "string",
    "resourceURL": "string"
  }
}
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/periodic"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.post(url,json=f)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)


def postsubscriptionuserTracking(ip,jsonm,etsiID,exampleID):
  f={
  "userTrackingSubscription": {
    "clientCorrelator": "0123",
    "callbackReference": {
      "notifyURL": "http://my.callback.com/location-user-tracking/some-id"
    },
    "address": "10.100.0.1",
    "userEventCriteria": [
      "Entering"
    ]
  }
}
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/userTracking"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.post(url,json=f)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)


def postsubscriptionzonalTraffic(ip,jsonm,etsiID,exampleID):
  f={
  "zonalTrafficSubscription": {
    "clientCorrelator": "0123",
    "callbackReference": {
      "notifyURL": "http://my.callback.com/location-zonal-traffic/some-id"
    },
    "zoneId": "zone01",
    "userEventCriteria": [
      "Entering"
    ]
  }
}
  url ="http://try-mec.etsi.org/"+etsiID+"/mep1/location/v2/subscriptions/zonalTraffic"
  url=url.replace("try-mec.etsi.org",ip)
  try:
    x=requests.post(url,json=f)
    result=x.decode("utf-8")
    print(result)
  except Exception as e:
    print(e)









if __name__ == '__main__':
     #getServices("0.0.0.0:8000","joao@gmail.com")
     #getServiceID("0.0.0.0:8000","exampleid","joao@gmail.com")
     getcircle("0.0.0.0:8000","sbxe83svpr")
     postSubscriptionsCircle("0.0.0.0:8000","sbxe83svpr")
     getZones("0.0.0.0:8000","sbxe83svpr")
     postsubscriptiondistance("0.0.0.0:8000","","sbxe83svpr","exampleID") 
    