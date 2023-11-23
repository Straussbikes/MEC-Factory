#!/usr/bin/env python3
import socket
import threading
import solver
import payload
import datetime
import json
import requests
import re
import database
import etsisolver
requestss ={}
global appId
appId=0

def takeJSON(request):
 
 request = request.decode('utf-8')
# Divida a solicitação em linhas
 request_lines = request.split('\r\n')

# Procure o cabeçalho 'Content-Type'
 content_type = None
 for line in request_lines:
     if line.startswith('Content-Type:'):
         content_type = line.split(': ')[1]
         break

# Verifique se o Content-Type indica que o corpo é JSON
 if content_type and 'application/json' in content_type:
    # Encontre o início do corpo JSON
    json_start = request.find('{', request.find('\r\n\r\n'))  # Encontra o primeiro '{' após a quebra de linha dupla

    if json_start != -1:
        # Extraia e analise o JSON
        json_data = json.loads(request[json_start:])
        return json_data
    else:
        print("JSON não encontrado no corpo do pedido.")
 else:
    print("O Content-Type não indica um corpo JSON.")


def sendETSI(method,new_request_data_bytes,withjson):
  if(method=="GET"):
       response=requests.get(new_request_data_bytes)
       return response
  elif(method=="POST"):
       json_data = json.dumps(withjson)
       response=requests.post(new_request_data_bytes,data=json_data, headers={"Content-Type": "application/json"})
       return response
  elif(method=="PUT"):
       response=requests.put(new_request_data_bytes)
       return response
  elif(method=="PATCH"):
       response=requests.put(new_request_data_bytes)
       return response

def extractETSIID(url):
    url_parts = url.split('/')
    id = url_parts[3]
    return id

def parseRequest(request):
        request=request.decode('utf-8')
        parts = request.split(' ')
        parts[1]=parts[1][1:]
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        matches = re.findall(pattern, parts[1])
        
        if(matches):
            email=matches[0]
            # Use re.sub to replace the matched substring with an empty string
            parts[1] = re.sub(pattern, '', parts[1])

            request=" ".join(parts)
            #print(request)
            request=request.encode('utf-8')
            return  request ,email
        else:
            return parts[1] , "no"


class HttpProxy:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.proxy_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.proxy_socket.bind((self.host, self.port))
        self.proxy_socket.listen(5)
        
 
    #thread para handler client
    def start(self):
        
        while True:
            client_socket, client_address = self.proxy_socket.accept()
            

            threading.Thread(target=self.handle_client, args=(client_socket,)).start()
    #tunel que recebe pedido do cliente e devolve a resposta enviando ao solver a reposta do MEP
    def  handle_client(self, client_socket):
        #fromClient
        request = client_socket.recv(4096)
        #print(request)
        #this function deletes the user email
        parsedRequest,useremail=parseRequest(request)
        if (not(useremail=="no")):
                method,url,a = parsedRequest.split(b'\r\n')[0].split()
                mep_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                mep_socket.connect(("0.0.0.0", 8080))
                mep_socket.sendall(parsedRequest)
                #toMEP
                response = mep_socket.recv(4096)
            
                req=response.split(b'\r\n')
                erro=req[0].split()
                method=method.decode("utf-8") 
                url=url.decode("utf-8")

                global appId
                newurl=0
                example=""
                solution,newurl,solution2,example=solver.solver(method,url,req,erro[1].decode("utf-8"))
                
                if(solution==1):
                    print("O seu url tinha erros de syntax, o pedido correto é: " + str(newurl))

                current_datetime=datetime.datetime.now()
                formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                pay=payload.Payload(str(appId),str(method+" "+ url),str(response),"0",str(erro[1].decode("utf-8")),formatted_datetime,str(solution2),str(newurl),useremail,example)
                requestss[appId]=pay.toJson()
                buffer=[]
                buffer.append(pay.toJson())
                try:
                    if pay is not None : 
                        response1 = requests.post("http://localhost:5000/response", json=buffer[0])
                        buffer.pop(0)
                except Exception as error:
                    print("no connection to backend",error)
                appId=appId+1
                
                client_socket.sendall(response)
                client_socket.close()
                mep_socket.close()
        else:
            new_host = "https://try-mec.etsi.org"  # Replace "new_ip_address" with the desired IP
            try:
                request_data_str = request.decode('utf-8')
            except UnicodeDecodeError as e:
                
                print(f"Erro de decodificação: {e}")
            lines = request_data_str.split('\r\n')
            lines2=lines[0].split(' ')
            newurl=new_host+lines2[1]
            etsiId=extractETSIID(newurl)
            # Substituir "0.0.0.0:8000" por etsi
            new_request_data_str = request_data_str.replace("0.0.0.0:8000", new_host)
            method=lines2.pop(0)
            new_request_data_bytes = new_request_data_str.encode('utf-8')
            json=takeJSON(new_request_data_bytes)
            responseETSI=sendETSI(method,newurl,json)
            
            response_bytes = responseETSI.content
            current_datetime=datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            
            solution,newurl,solution2,example=etsisolver.solver(method,newurl,responseETSI.status_code)
            email=database.getEmail(etsiId)
            pay=payload.Payload(str(appId),str(method+" "+ newurl),str(response_bytes.decode("utf-8")),"0",str(responseETSI.status_code),formatted_datetime,str(solution2),str(newurl),email,example)
            requestss[appId]=pay.toJson()
            buffer=[]
            buffer.append(pay.toJson())
            
            try:
                if pay is not None : 
                    response1 = requests.post("http://localhost:5000/response", json=buffer[0])
                    buffer.pop(0)
            except Exception as error:
                    print("no connection to backend",error)
            appId=appId+1
           
            client_socket.sendall(response_bytes)
            client_socket.close()













if __name__ == '__main__':
   
   
    proxy = HttpProxy('0.0.0.0', 8000)
    
    proxy.start()