import requests



def getbw_allocations(ip,etsiID):
  url="http://try-mec.etsi.org/"+etsiID+"/mep1/bwm/v1/bw_allocations"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.get(url)
  print(req.content)



def postbw_allocations(ip,appinstance,trafficinstance,email,etsiID):
  f={
  "timeStamp": {
    "seconds": 1,
    "nanoSeconds": 6
  },
  "allocationDirection": "allocationDirection",
  "fixedBWPriority": "SEE_DESCRIPTION",
  "requestType": 0,
  "sessionFilter": [
    {
      "protocol": "protocol",
      "sourcePort": "sourcePort",
      "dstPort": "dstPort",
      "sourceIp": "sourceIp",
      "dstAddress": "dstAddress"
    },
    {
      "protocol": "protocol",
      "sourcePort": "sourcePort",
      "dstPort": "dstPort",
      "sourceIp": "sourceIp",
      "dstAddress": "dstAddress"
    }
  ],
  "appName": "appName",
  "allocationId": "allocationId",
  "appInsId": "appInsId",
  "fixedAllocation": "fixedAllocation"
}
  url = "https://try-mec.etsi.org/"+etsiID+"/mep1/bwm/v1/bw_allocations"
  url=url.replace("try-mec.etsi.org",ip)
  x = requests.post(url, json = f)
  print(x.content)

def getbw_allocationsID(ip,appinstance,etsiID,exampleID):
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/bwm/v1/bw_allocations/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.get(url)
  print(req)
  print(req.content)



def putbw_allocationsID(ip,etsiID,exampleID):
  f={
  "timeStamp": {
    "seconds": 1,
    "nanoSeconds": 6
  },
  "allocationDirection": "allocationDirection",
  "fixedBWPriority": "SEE_DESCRIPTION",
  "requestType": 0,
  "sessionFilter": [
    {
      "protocol": "protocol",
      "sourcePort": "sourcePort",
      "dstPort": "dstPort",
      "sourceIp": "sourceIp",
      "dstAddress": "dstAddress"
    },
    {
      "protocol": "protocol",
      "sourcePort": "sourcePort",
      "dstPort": "dstPort",
      "sourceIp": "sourceIp",
      "dstAddress": "dstAddress"
    }
  ],
  "appName": "appName",
  "allocationId": "allocationId",
  "appInsId": "appInsId",
  "fixedAllocation": "fixedAllocation"  
}
  url = "http://try-mec.etsi.org/"+etsiID+"/mep1/bwm/v1/bw_allocations/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  x = requests.put(url, json = f)
  #print(x
  print(x.content)

def deletebw_allocationsID(ip,etsiID,exampleID):
  url="https://try-mec.etsi.org/"+etsiID+"/mep1/bwm/v1/bw_allocations/exampleID"
  url=url.replace("try-mec.etsi.org",ip)
  req=requests.delete(url)
  print(req)
  print(req.content)














if __name__ == '__main__':
     
      #getbw_allocations("0.0.0.0:8000")
      putbw_allocationsID("0.0.0.0:8000","sbxe83svpr","exampleID")