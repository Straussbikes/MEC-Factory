




class Payload:
    def __init__(self, appId,fromCli,fromMep,flagReso,erroCode,date,resolution,newurl,useremail,example):
        self.appId=appId
        self.fromCli=fromCli
        self.fromMep=fromMep
        self.flagReso=flagReso
        self.erroCode=erroCode
        self.date=date
        self.resolution=resolution
        self.newurl=newurl
        self.useremail=useremail
        self.example=example
    
    def get_appId(self):
        return self.appId
    def get_fromCli(self):
        return self.fromCli
    def get_fromMep(self):
        return self.fromMep
    def get_flagReso(self):
        return self.flagReso
    def get_erroCode(self):
        return self.erroCode
    def get_date(self):
        return self.date
    def get_resolution(self):
        return self.resolution
    def get_example(self):
        return self.example
    
    def set_example(self,a):
        self.example=a

    def set_appId(self,a):
         self.appId=a
    def set_fromCli(self,a):
         self.fromCli=a
    def set_fromMep(self,a):
         self.fromMep=a
    def set_flagReso(self,a):
         self.flagReso=a
    def set_erroCode(self,a):
         self.erroCode=a
    def set_date(self,a):
         self.date=a
    def set_resolution(self,a):
         self.resolution=a

    def get_newurl(self):
        return self.newurl

    def set_newurl(self,a):
         self.newurl=a

    def toJson(self):
        return { "appId" : self.appId,
                  "request":self.fromCli,
                  "response":self.fromMep,
                  "flagReso" :self.flagReso,
                  "erro" :self.erroCode,
                  "date" : self.date,
                  "solution" : self.resolution,
                  "newUrl" :  self.newurl,
                  "email":self.useremail,
                  "example":self.example
                 }

