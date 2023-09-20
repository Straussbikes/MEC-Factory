import json
import syntaxchecker
#a=METODO b=URL c=response from MEP
def solver(method,url,response,errorC):
    #parse do pedido
        #print("url before" + str(url))
        split = url.split("/")
        newurl=""
        tam=len(split)-1
        (corrected,flag)=checksyntax(url)
        solveds="/".join(corrected)
        if(flag==1):newurl=solveds
        url=solveds
        solution2=""
        if(method=="GET"):
            solution2=do_GET(url,response,errorC)
        elif(method=="POST"):
            try:
                solution2=do_POST(url,response,errorC)
            except Exception as e:
                print(e)
        elif(method=="PUT"):
            do_PUT(url,response,errorC)
        elif(method=="DELETE"):
            do_DELETE(url,response,errorC)
        elif(method=="PATCH"):
            do_PATCH(url,response,errorC)
        else:
            print("Method not recognized")
        return (flag,newurl,solution2)
    #encaminhar para funcao

    #a=codigo de erro b=conteudo retornado do MEP

#feito e testado
#flag 1 verfica  se foi corrigido algo ou nao
def checksyntax(url):
      solved=[]
      splited=url.split("/")
      flag=0
      for a in splited:
          correction=syntaxchecker.testsyntax(a)
          solved+=[correction]
          if(a!=correction):
              flag=1
      #print(solved)       
      return(solved,flag)
      
    
def do_GET(url,response,d):
    with open("/home/bikes/Desktop/test/backend/proxy/getService.json","r") as f:
        data=json.load(f)
        splited=url.split("/")
        tam=len(splited)-1      
        if(splited[tam-1]=="subscriptions" and splited[1]=="mec_service_mgmt"):
            return data[splited[1]][splited[3]]["subscriptions"]["subscriptionId"][d]
        elif(splited[tam-1]=="services" and splited[3]=="applications"):
            return data[splited[1]][splited[3]]["services"]["serviceId"][d]
        elif(splited[tam-1]=="services" and splited[tam]!="services"):
            return data[splited[1]][splited[tam-1]][d]
        elif(splited[3]=="applications" and (splited[tam-1]=="traffic_rules" or splited[tam-1]=="dns_rules" or splited[tam-1]=="subscriptions")):
            return data[splited[1]][splited[3]]["appInstanceId"][splited[tam-1]][d]
        elif(splited[3]=="applications"):
            return data[splited[1]][splited[3]]["appInstanceId"][splited[tam]][d]
        elif(splited[3]=="applications" and splited[tam]=="traffic_rules"):
            return data[splited[1]][splited[3]]["appInstanceId"][splited[tam]][d]
        elif(splited[3]=="timing"):
            return data[splited[1]][splited[3]][splited[tam]][d]
        else:
            try:
                return (data[splited[1]][splited[tam]][d])
            except Exception:
                pass
#feito e testado
def do_POST(url,response,d):
    with open("/home/bikes/Desktop/test/backend/proxy/postService.json","r") as f:
        data=json.load(f)
        splited=url.split("/")
        tam=len(splited)-1
        #print(splited)   
        if(splited[tam]=="subscriptions"):
            return data[splited[1]][splited[3]][splited[tam]][d]
        elif(splited[tam]=="confirm_ready" or splited[tam]=="confirm_termination"):
            return data[splited[1]][splited[3]]["appInstanceId"][splited[tam]][d]
#feito e testado 
def do_DELETE(url,response,d):
    with open("/home/bikes/Desktop/test/backend/proxy/postService.json","r") as f:
        data=json.load(f)
        splited=url.split("/")
        tam=len(splited)-1
       # print(splited)
        if(splited[tam-1]=="subscriptions"):
            return data[splited[1]][splited[3]][splited[tam-1]][d]
        elif(splited[tam]=="registrations"):
            return data[splited[1]][splited[3]][splited[tam]]["appInstanceId"][d]
        elif(splited[tam-1]=="services"):
            return data[splited[1]][splited[3]]["appInstanceId"][splited[tam]]["serviceId"][d]
        elif((splited[tam-1]=="subscriptions") and splited[1]=="mec_service_mgmt"):
            return data[splited[1]][splited[3]]["appInstanceId"]["subscriptions"]["subscriptionId"][d]

def do_PUT(url,response,d):
    pass

def do_PATCH(url,response,d):
    pass



