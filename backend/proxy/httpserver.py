#!/usr/bin/env python3
import socket
import threading
import solver
import payload
import datetime
import json
import requests
import re

requestss ={}
global appId
appId=0



def parseRequest(request):
        request=request.decode('utf-8')
        parts = request.split(' ')
        
        parts[1]=parts[1][1:]
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        matches = re.findall(pattern, parts[1])
        email=matches[0]
        # Use re.sub to replace the matched substring with an empty string
        parts[1] = re.sub(pattern, '', parts[1])

        request=" ".join(parts)
        
        request=request.encode('utf-8')
        return  request ,email


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
        #this function deletes the user email
        request,useremail=parseRequest(request)
        method,url,a = request.split(b'\r\n')[0].split()
        mep_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mep_socket.connect(("0.0.0.0", 8080))
        mep_socket.sendall(request)
        #toMEP
        response = mep_socket.recv(4096)
      
        req=response.split(b'\r\n')
        erro=req[0].split()
        method=method.decode("utf-8") 
        url=url.decode("utf-8")

        global appId
        newurl=0
        solution,newurl,solution2=solver.solver(method,url,req,erro[1].decode("utf-8"))
        
        if(solution==1):
            print("O seu url tinha erros de syntax, o pedido correto é: " + str(newurl))
        #store data
        print(useremail)
        current_datetime=datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        pay=payload.Payload(str(appId),str(method+" "+ url),str(response),"0",str(erro[1].decode("utf-8")),formatted_datetime,str(solution2),str(newurl),useremail)
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





if __name__ == '__main__':
   
   
    proxy = HttpProxy('0.0.0.0', 8000)
    
    proxy.start()