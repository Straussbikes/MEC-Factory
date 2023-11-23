import json

from solver import checksyntax
import syntaxchecker
from urllib.parse import urlparse

def solver(method,url,errorC):
        parsed_url = urlparse(url)
        path = parsed_url.path
        split = path.split("/")
        newurl=""
        flag=0
        print(path)
        tam=len(split)-1
        (corrected,flag)=checksyntax(path)
        print((corrected,flag))
        example=""
        solveds="/".join(corrected)
        if(flag==1):
            path=solveds
            newurl=solveds
        solution2=""
        if(method=="GET"):
            try:
                solution2,example=do_GET(path,errorC)
            except Exception as e:
                print(e)
        elif(method=="POST"):
            try:
                solution2,example=do_POST(path,errorC)
            except Exception as e:
                print(e)
        elif(method=="PUT"):
            try:
                solution2,example=do_PUT(path,errorC)
            except Exception as e:
                print(e)
        elif(method=="DELETE"):
            solution2,example=do_DELETE(path,errorC)
        elif(method=="PATCH"):
            solution2,example=do_PATCH(path,errorC)
        else:
            print("Method not recognized")
        if(solution2==0):
            return (flag,newurl,"Url syntax error","{}")
        return (flag,newurl,solution2,example)
    #encaminhar para funcao

    #a=codigo de erro b=conteudo retornado do MEP
    
def do_GET(url,d):
        split = url.split("/")
        tam=len(split)-1
        print(url)
        if(split[3]=="location"):
             with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/013.json","r") as f:
                data=json.load(f)
                if(split[5]=="subscriptions"):
                    if(split[tam]=="circle"):
                        return data["GET"]["subscriptions/area/circle"][str(d)],data["GET"]["subscriptions/area/circle"]["example"]["txt"]
                    if(split[tam-1]=="circle"):
                        return data["GET"]["subscriptions/area/circle/subscriptionsID"][str(d)],data["GET"]["subscriptions/area/circle/subscriptionsID"]["example"]["txt"]
                    if(split[tam]=="distance"):
                        return data["GET"]["subscriptions/distance"][str(d)],data["GET"]["subscriptions/distance"]["example"]["txt"]
                    if(split[tam-1]=="distance"):
                        return data["GET"]["subscriptions/distance/subscriptionsID"][str(d)],data["GET"]["subscriptions/distance/subscriptionsID"]["example"]["txt"]
                    if(split[tam]=="periodic"):
                        return data["GET"]["subscriptions/periodic"][str(d)],data["GET"]["subscriptions/periodic"]["example"]["txt"]
                    if(split[tam-1]=="periodic"):
                        return data["GET"]["subscriptions/periodic/subscriptionsID"][str(d)],data["GET"]["subscriptions/periodic/subscriptionsID"]["example"]["txt"]
                    if(split[tam]=="userTracking"):
                        return data["GET"]["subscriptions/userTracking"][str(d)],data["GET"]["subscriptions/userTracking"]["example"]["txt"]
                    if(split[tam-1]=="userTracking"):
                        return data["GET"]["subscriptions/distance/subscriptionsID"][str(d)],data["GET"]["subscriptions/distance/subscriptionsID"]["example"]["txt"]
                    if(split[tam]=="zonalTraffic"):
                        return data["GET"]["subscriptions/zonalTraffic"][str(d)],data["GET"]["subscriptions/zonalTraffic"]["example"]["txt"]
                    if(split[tam-1]=="zonalTraffic"):
                        return data["GET"]["subscriptions/zonalTraffic/subscriptionID"][str(d)],data["GET"]["subscriptions/zonalTraffic/subscriptionID"]["example"]["txt"]
                    if(split[tam]=="zoneStatus"):
                       return data["GET"]["subscriptions/zoneStatus"][str(d)],data["GET"]["subscriptions/zoneStatus"]["example"]["txt"]
                    if(split[tam-1]=="zoneStatus"):
                        return data["GET"]["subscriptions/zoneStatus/subscriptionID"][str(d)],data["GET"]["subscriptions/zoneStatus/subscriptionID"]["example"]["txt"]
                if(split[5]=="queries"):
                     if(split[tam]=="distance"):
                           return data["GET"]["subscriptions/area/circle"][str(d)],data["GET"]["subscriptions/area/circle"]["example"]["txt"]
                     if(split[tam]=="users"):
                           return data["GET"]["queries/users"][str(d)],data["GET"]["queries/users"]["example"]["txt"]
                     if(split[tam]=="zones"):
                           return data["GET"]["queries/zones"][str(d)], data["GET"]["queries/zones"]["example"]["txt"]
                     if(split[tam-1]=="zones"):
                           return data["GET"]["queries/zones/zonesID"][str(d)],data["GET"]["queries/zones/zonesID"]["example"]["txt"]
                     if(split[tam]=="accessPoints"):
                           return data["GET"]["queries/zones/zonesID/accessPoints"][str(d)],data["GET"]["queries/zones/zonesID/accessPoints"]["example"]["txt"]
                     if(split[tam-1]=="accessPoints"):
                           return data["GET"]["queries/zones/zonesID/accessPoints/accessPointsID"][str(d)],data["GET"]["queries/zones/zonesID/accessPoints/accessPointsID"]["example"]["txt"]
        if(split[3]=="bwm"):
            with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/015.json","r") as f:
                data=json.load(f)
                if(split[5]=="bw_allocations"):
                     return data["bwm"]["GET"]["bw_allocations"][str(d)],data["bwm"]["GET"]["bw_allocations"]["example"]["txt"]["example"]["txt"]
                if(split[tam-1]=="bw_allocations"):
                     return data["bwm"]["GET"]["bw_allocations"][str(d)],data["bwm"]["GET"]["bw_allocations"]["example"]["txt"]
        if(split[3]=="rni"):
            with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/012.json","r") as f:
                data=json.load(f)
                if(split[tam]=="rab_info"):
                     return data["rni"]["GET"]["rab_info"][str(d)],data["rni"]["GET"]["rab_info"]["example"]["txt"]
                if(split[tam]=="plmn_info"):
                     return data["rni"]["GET"]["plmn_info"][str(d)],data["rni"]["GET"]["plmn_info"]["example"]["txt"]
                if(split[tam]=="layer2_meas "):
                     return data["rni"]["GET"]["layer2_meas"][str(d)],data["rni"]["GET"]["layer2_meas"]["example"]["txt"]
                if(split[tam]=="subscriptions"):
                     return data["rni"]["GET"]["subscriptions"][str(d)],data["rni"]["GET"]["subscriptions"]["example"]["txt"]
                if(split[tam-1]=="subscriptions"):
                     return data["rni"]["GET"]["subscriptions"][str(d)],data["rni"]["GET"]["subscriptions"]["example"]["txt"]
        if(split[3]=="vis"):
            with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/030.json","r") as f:
                data=json.load(f)
                if(split[tam]=="uu_unicast_provisioning_info"):
                     return data["vis"]["GET"]["uu_unicast_provisioning_info"][str(d)],data["vis"]["GET"]["uu_unicast_provisioning_info"]["example"]["txt"]
                if(split[tam]=="subscriptions"):
                     return data["vis"]["GET"]["subscriptions"][str(d)],data["vis"]["GET"]["subscriptions"]["example"]["txt"]
                if(split[tam-1]=="subscriptions"):
                     return data["vis"]["GET"]["subscriptions"][str(d)],data["vis"]["GET"]["subscriptions"]["example"]["txt"]
        if(split[3]=="wai"):                
            with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/028.json","r") as f:
                data=json.load(f)    
                if(split[tam]=="ap_information"):
                     return data["wai"]["GET"]["ap_information"][str(d)],data["wai"]["GET"]["ap_information"]["example"]["txt"]
                if(split[tam]=="sta_information"):
                     return data["wai"]["GET"]["sta_information"][str(d)],data["wai"]["GET"]["sta_information"]["example"]["txt"]
                if(split[tam]=="subscriptions"):
                     return data["wai"]["GET"]["subscriptions"][str(d)],data["wai"]["GET"]["subscriptions"]["example"]["txt"]
                if(split[tam-1]=="subscriptions"):
                     return data["wai"]["GET"]["subscriptions"][str(d)],data["wai"]["GET"]["subscriptions"]["example"]["txt"]
        

def do_POST(url,d):
        split = url.split("/")
        tam=len(split)-1
        if(split[3]=="location"):
            with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/013.json","r") as f:
                data=json.load(f)
                if(split[5]=="subscriptions"):
                    if(split[tam]=="circle"):
                        return data["POST"]["subscriptions/area/circle"][str(d)],data["POST"]["subscriptions/area/circle"]["example"]["txt"]
                    if(split[tam]=="distance"):
                        return data["POST"]["subscriptions/distance"][str(d)],data["POST"]["subscriptions/distance"]["example"]["txt"]
                    if(split[tam]=="periodic"):
                        return data["POST"]["subscriptions/periodic"][str(d)],data["POST"]["subscriptions/periodic"]["example"]["txt"]
                    if(split[tam]=="userTracking"):
                        return data["POST"]["subscriptions/userTracking"][str(d)],data["POST"]["subscriptions/userTracking"]["example"]["txt"]
                    if(split[tam]=="zonalTraffic"):
                        return data["POST"]["subscriptions/zonalTraffic"][str(d)],data["POST"]["subscriptions/zonalTraffic"]["example"]["txt"]
                    if(split[tam]=="zoneStatus"):
                        return data["POST"]["subscriptions/zoneStatus"][str(d)],data["POST"]["subscriptions/zoneStatus"]["example"]["txt"]
        if(split[3]=="bwm"):
            with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/015.json","r") as f:
                data=json.load(f)
            if(split[tam-1]=="bw_allocations"):
                 return data["bwm"]["POST"]["bw_allocations"][str(d)],data["bwm"]["POST"]["bw_allocations"]["example"]["txt"]
        if(split[3]=="rni"):
            with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/012.json","r") as f:
                data=json.load(f)
                if(split[tam]=="subscriptions"):
                     return data["rni"]["POST"]["subscriptions"][str(d)],data["rni"]["POST"]["subscriptions"]["example"]["txt"]
        if(split[3]=="vis"):
            with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/030.json","r") as f:
                data=json.load(f)
                if(split[tam]=="provide_predicted_qos"):
                     return data["vis"]["POST"]["provide_predicted_qos"][str(d)],data["vis"]["POST"]["provide_predicted_qos"]["example"]["txt"]
                if(split[tam]=="subscriptions"):
                     return data["vis"]["POST"]["publish_v2x_message"][str(d)],data["vis"]["POST"]["publish_v2x_message"]["example"]["txt"]
                if(split[tam]=="subscriptions"):
                     return data["vis"]["POST"]["subscriptions"][str(d)],data["vis"]["POST"]["subscriptions"]["example"]["txt"]
        if(split[3]=="wai"):                
            with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/028.json","r") as f:
                data=json.load(f)    
                if(split[tam]=="subscriptions"):
                     return data["wai"]["POST"]["subscriptions"][str(d)], data["wai"]["POST"]["subscriptions"]["example"]["txt"]
def do_PUT(url,d):
        split = url.split("/")
        tam=len(split)-1
        if(split[3]=="location"):
             with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/013.json","r") as f:
                data=json.load(f)
                if(split[5]=="subscriptions"):
                    if(split[tam-1]=="circle"):
                        return data["PUT"]["subscriptions/area/circle/subscriptionsID"][str(d)], data["PUT"]["subscriptions/area/circle/subscriptionsID"]["example"]["txt"]
                    if(split[tam-1]=="distance"):
                        return data["PUT"]["subscriptions/distance/subscriptionsID"][str(d)],data["PUT"]["subscriptions/distance/subscriptionsID"]["example"]["txt"]
                    if(split[tam-1]=="periodic"):
                        return data["PUT"]["subscriptions/periodic/subscriptionsID"][str(d)],data["PUT"]["subscriptions/periodic/subscriptionsID"]["example"]["txt"]
                    if(split[tam-1]=="userTracking"):
                        return data["PUT"]["subscriptions/distance/subscriptionsID"][str(d)],data["PUT"]["subscriptions/distance/subscriptionsID"]["example"]["txt"]
                    if(split[tam-1]=="zonalTraffic"):
                        return data["PUT"]["subscriptions/zonalTraffic/subscriptionID"][str(d)],data["PUT"]["subscriptions/zonalTraffic/subscriptionID"]["example"]["txt"]
                    if(split[tam-1]=="zoneStatus"):
                        return data["PUT"]["subscriptions/zoneStatus/subscriptionID"][str(d)],data["PUT"]["subscriptions/zoneStatus/subscriptionID"]["example"]["txt"]
        if(split[3]=="bwm"):
            with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/015.json","r") as f:
                data=json.load(f)
            if(split[tam-1]=="bw_allocations"):
                 return data["bwm"]["PUT"]["bw_allocations"][str(d)],data["bwm"]["PUT"]["bw_allocations"]["example"]["txt"]
                 
        if(split[3]=="rni"):
            with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/012.json","r") as f:
                data=json.load(f)
                if(split[tam-1]=="subscriptions"):
                     return data["rni"]["PUT"]["subscriptions"][str(d)],data["rni"]["PUT"]["subscriptions"]["example"]["txt"]
        if(split[3]=="vis"):
            with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/030.json","r") as f:
                data=json.load(f)
                if(split[tam-1]=="subscriptions"):
                     return data["vis"]["PUT"]["subcriptions"][str(d)],data["vis"]["PUT"]["subcriptions"]["example"]["txt"]
        if(split[3]=="wai"):                
            with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/028.json","r") as f:
                data=json.load(f)    
                if(split[tam-1]=="subscriptions"):
                     return data["wai"]["PUT"]["subscriptions"][str(d)],data["wai"]["PUT"]["subscriptions"]["example"]["txt"]


def do_DELETE(url,d):
        split = url.split("/")
        tam=len(split)-1
        if(split[3]=="location"):
             with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/013.json","r") as f:
                data=json.load(f)
                if(split[5]=="subscriptions"):
                    if(split[tam-1]=="circle"):
                        return data["DELETE"]["subscriptions/area/circle/subscriptionsID"][str(d)],data["DELETE"]["subscriptions/area/circle/subscriptionsID"]["example"]["txt"]
                    if(split[tam-1]=="distance"):
                        return data["DELETE"]["subscriptions/distance/subscriptionsID"][str(d)],data["DELETE"]["subscriptions/distance/subscriptionsID"]["example"]["txt"]
                    if(split[tam-1]=="periodic"):
                        return data["DELETE"]["subscriptions/periodic/subscriptionsID"][str(d)],data["DELETE"]["subscriptions/periodic/subscriptionsID"]["example"]["txt"]
                    if(split[tam-1]=="userTracking"):
                        return data["DELETE"]["subscriptions/distance/subscriptionsID"][str(d)],data["DELETE"]["subscriptions/distance/subscriptionsID"]["example"]["txt"]
                    if(split[tam-1]=="zonalTraffic"):
                        return data["DELETE"]["subscriptions/zonalTraffic/subscriptionID"][str(d)],data["DELETE"]["subscriptions/zonalTraffic/subscriptionID"]["example"]["txt"]
                    if(split[tam-1]=="zoneStatus"):
                        return data["DELETE"]["subscriptions/zoneStatus/subscriptionID"][str(d)],data["DELETE"]["subscriptions/zoneStatus/subscriptionID"]["example"]["txt"]
        if(split[3]=="bwm"):
            with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/015.json","r") as f:
                data=json.load(f)
            if(split[tam-1]=="bw_allocations"):
                 return data["bwm"]["DELETE"]["bw_allocations"][str(d)], data["bwm"]["DELETE"]["bw_allocations"]["example"]["txt"]
        if(split[3]=="rni"):
            with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/012.json","r") as f:
                data=json.load(f)
                if(split[tam-1]=="subscriptions"):
                     return data["rni"]["DELETE"]["subscriptions"][str(d)],data["rni"]["DELETE"]["subscriptions"]["example"]["txt"]
        if(split[3]=="vis"):
            with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/030.json","r") as f:
                data=json.load(f)
                if(split[tam-1]=="subscriptions"):
                     return data["vis"]["DELETE"]["subscriptions"][str(d)], data["vis"]["DELETE"]["subscriptions"]["example"]["txt"]
        if(split[3]=="wai"):                
            with open("/home/bikes/Desktop/MECGIT/MEC-Factory/backend/proxy/028.json","r") as f:
                data=json.load(f)    
                if(split[tam-1]=="subscriptions"):
                     return data["wai"]["DELETE"]["subscriptions"][str(d)],data["wai"]["DELETE"]["subscriptions"]["example"]["txt"]