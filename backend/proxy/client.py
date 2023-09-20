import socket
import pickle
from time import sleep
import requests


#analisar semantica do pedido 

#application Suport
#pedidos Get

def gets():
  req=requests.get("http://0.0.0.0:8000/mac_servisse_mgmt/v1/servisses")
  print(req)
  print(req.content)
#http://0.0.0.0:8000/mac_servisse_mgmt/v1/servisses
#https://try-mec.etsi.org/sbxe83svpr/mep1/bwm/v1/bw_allocations


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

# asd=Mec app instance   
def getTraffic_rulesID(ip,appinstance,trafficinstance):
  url="http://0.0.0.0:8000/mec_app_support/v1/applications/asd/traffic_rules"
  url=url.replace("asd",appinstance)
  url=url.replace("rule",trafficinstance)
  url=url.replace("0.0.0.0:8000",ip)
  req=requests.get(url)
  print(req)
  print(req.content)

def postTraffic_rulesID(ip,appinstance,trafficinstance):
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
  url = 'http://0.0.0.0:8000/mec_app_support/v1/applications/asd/traffic_rules/rule'
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("rule",trafficinstance)
  url=url.replace("asd",appinstance)
  x = requests.post(url, json = f)
  #print(x
  print(x.content)

#appDNSRules
def getDNS_rules(ip,appinstance):
  url="http://0.0.0.0:8000/mec_app_support/v1/applications/asd/dns_rules"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  req=requests.get(url)
  print(req)
  print(req.content)

def getDNS_rulesID(ip,appinstance):
  url="http://0.0.0.0:8000/mec_app_support/v1/applications/asd/dns_rules/dns"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  req=requests.get(url)
  print(req)
  print(req.content)

def postConfirmT(ip,appinstance,json,rule):
  f={
  "dnsRuleId": "string",
  "domainName": "string",
  "ipAddressType": "IP_V6",
  "ipAddress": "string",
  "ttl": 0,
  "state": "ACTIVE"
} 
  url = 'http://0.0.0.0:8000/mec_app_support/v1/applications/asd/dns_rules/rule'
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  url=url.replace("rule",rule)
  x = requests.post(url, json = f)
  #print(x)
  print(x.content)




#appSubscriptions

def getSubscriptions(ip,appinstance):
  url="http://0.0.0.0:8000/mec_app_support/v1/applications/asd/subscriptions"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  req=requests.get(url)
  print(req)
  print(req.content)

def postSubscriptions(ip,appinstance):
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
  url = 'http://0.0.0.0:8000/mec_app_support/v1/applications/asd/subscriptions'
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  x = requests.post(url, json = f)
  #print(x)
  print(x.content)


def getSubscriptionsID(ip,appinstance,subs):
  url="http://0.0.0.0:8000/mec_app_support/v1/applications/asd/subscriptions/subscription"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  url=url.replace("subscription",subs)
  req=requests.get(url)
  print(req)
  print(req.content)

def delSubscriptions(ip,appinstance,subs):
  url="http://0.0.0.0:8000/mec_app_support/v1/applications/asd/subscriptions/a"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  url=url.replace("a",subs)
  req=requests.delete(url)
  print(req)
  print(req.content)
#appConfirmTermination

def postConfirmT(ip,appinstance,json):
  f={
  "operationAction": "TERMINATING"
}
  url = 'http://0.0.0.0:8000/mec_app_support/v1/applications/asd/confirm_termination'
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  x = requests.post(url, json = f)
  #print(x)
  print(x.content)



#appConfirmReady

# application Suport Confirm Ready
def postconfirmR(ip,appinstance,json):
  f={
    "indication": "READY"
  } 
  url = 'http://0.0.0.0:8000/mec_app_support/v1/applications/asd/confirm_ready'
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  x = requests.post(url, json = f)
  #print(x)
  print(x.content)


#timing

def getTiming_caps(ip):
  url="http://0.0.0.0:8000/mec_app_support/v1/timing/timing_caps"
  url=url.replace("0.0.0.0:8000",ip)
  req=requests.get(url)
  print(req)
  print(req.content)

def getCurrent_Time(ip):
  url="http://0.0.0.0:8000/mec_app_support/v1/timing/current_time"
  url=url.replace("0.0.0.0:8000",ip)
  req=requests.get(url)
  print(req)
  print(req.content)


                            #  MEC SERVICE MANAGEMENT

#appSubscriptions

def getSubscriptionsserv(ip,appinstance):
  url="http://0.0.0.0:8000/mec_service_mgmt/v1/applications/asd/subscriptions"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  req=requests.get(url)
  print(req)
  print(req.content)

def getSubscriptionsIDserv(ip,appinstance,subs):
  url="http://0.0.0.0:8000/mec_service_mgmt/v1/applications/asd/subscriptions/subs"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  url=url.replace("subs",subs)
  req=requests.get(url)
  print(req)
  print(req.content)

def postSubscriptions(ip,appinstance):
  url = 'http://0.0.0.0:8000/mec_service_mgmt/v1/applications/11/subscriptions'
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


#delete
#appsuport
def delSubscriptionsId(ip,appinstance,subs):
  url="http://0.0.0.0:8000/mec_app_support/v1/applications/asd/subscriptions/123"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  url=url.replace("123",subs)
  x= requests.delete(url)
  print(x)
  print(x.content)

#appServices



# GET SERVICES app SERVICES 1st


def postService(ip,appinstance):
   f={
   
   }
    
   url = 'http://0.0.0.0:8000/mec_service_mgmt/v1/applications/asd/services'
   url=url.replace("0.0.0.0:8000",ip)
   url=url.replace("asd",appinstance)
   x = requests.post(url, json = f)
   print(x)
   print(x.content)

def getServiceID(ip,appinstance,service):
  url="http://0.0.0.0:8000/mec_service_mgmt/v1/applications/asd/services/123"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  url=url.replace("123",service)
  req=requests.get(url)
  print(req)
  print(req.content)



def putServiceID(ip,appinstance,service):
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
   url = 'http://0.0.0.0:8000/mec_service_mgmt/v1/applications/asd/services/123'
   url=url.replace("0.0.0.0:8000",ip)
   url=url.replace("asd",appinstance)
   url=url.replace("123",service)
   x = requests.post(url, json = f)
   print(x)
   print(x.content)


def delServiceID(ip,appinstance,service):
  url="http://0.0.0.0:8000/mec_service_mgmt/v1/applications/asd/services/123"
  url=url.replace("0.0.0.0:8000",ip)
  url=url.replace("asd",appinstance)
  url=url.replace("123",service)
  req=requests.delete(url)
  print(req)
  print(req.content)


#services


def getServices(ip):
  url="http://0.0.0.0:8000/joao@gmail.com/mac_service_mgmt/v1/services"
  url=url.replace("0.0.0.0:8000",ip)
  req=requests.get(url)
  print(req)
  print(req.content)



def getServiceID(ip,appinstance):
  url="http://0.0.0.0:8000/mec_service_mgmt/v1/services/asd"
  url=url.replace("asd",appinstance)
  url=url.replace("0.0.0.0:8000",ip)
  req=requests.get(url)
  print(req)
  print(req.content)


#Transports

def getTransport(ip):
  url="http://0.0.0.0:8000/mec_service_mgmt/v1/transports"
  url=url.replace("0.0.0.0:8000",ip)
  req=requests.get(url)
  print(req)
  print(req.content)





#individual MEC service


def getIndividualMECservice(ip):
  url="http://0.0.0.0:8000/mec_service_mgmt/v1/resource_uri_allocated_by_MEC_platform"
  url=url.replace("0.0.0.0:8000",ip)
  req=requests.get(url)
  print(req)
  print(req.content)




#server liveness
def patchlive(ip):
  f={
      "state": "ACTIVE"
  }
  url="http://0.0.0.0:8000/mec_service_mgmt/v1/resource_uri_allocated_by_MEC_platform"
  url=url.replace("0.0.0.0:8000",ip)
  x=requests.patch(url,json=f)
  print(x)
  print(x.content)


if __name__ == '__main__':
   
      getServices("0.0.0.0:8000")
      
      