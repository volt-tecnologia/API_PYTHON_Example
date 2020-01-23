import requests,json;
from requests.auth import HTTPBasicAuth;
from requests.exceptions import Timeout;
class VoltDevice:

    def __init__(self, username, password,ip):
        self.ip = ip if len(ip) > 0 else '127.0.0.1'
        self.username = username;
        self.password = password;
        #print(self.updateInfo())

        #print(self.lastInfo)

    def updateInfo(self):
        resp = self.reqGETHTTP('http://'+self.ip+'/status.json');
        
        if resp.status_code == 200:
            self.lastInfo = resp.json();
            
        #else: 
            #print(resp.status_code);

            #self.lastInfo = 0;
        
        return resp.status_code;

    def reqGETHTTP(self, url):
        print(url);
        try:
            response = requests.get(url,auth=HTTPBasicAuth(self.username,self.password), timeout=2);
            #print(response.status_code)
            if response.status_code == 401:
                response._content = b''

            return response;
        except Timeout:
            print('Erro de Timeout')
            response = requests.Response()
            response.status_code = 500
            response._content = b''
            
            return response

        
    def reqPOSTHTTP(self, url, payload):
        print(url);
        try:
            response = requests.post(url,auth=HTTPBasicAuth(self.username,self.password),data=payload, timeout=2);
            #print(response.status_code)
            return response;
        except Timeout:
            print('Erro de Timeout')
            response = requests.Response()
            response.status_code = 500
            response._content = b''
            
            return response

    def configEthernet(self, boolDhcp, newhost, newip, newgtw, newmask, newdns1, newdns2):
        payload = {'dhcp':('true' if boolDhcp == True else 'false'),'host':newhost,'ip':newip,'gw':newgtw,'sub':newmask,'dns1':newdns1, 'dns2':newdns2}
        #print(payload)
        response = self.reqPOSTHTTP('http://'+self.ip+'/config.htm?', payload)
        
        if(response.status_code == 200): 
           response = self.reqGETHTTP("http://" + self.ip + "/reset.cgi?timeout=1")
           return response
        else: 
            return response
         

    def ctrlAc(self, tomada, op, habilita=True, ac_name=lambda: getNomeAC(tomada)):
        if(self.lastInfo != 0):
        
            if op == 0:
                if(self.getRmac(tomada)):            
                    return self.reqGETHTTP("http://" + self.ip + "/outpoe.cgi?poe=" + str(tomada) + "&sts="+('0' if self.getAc(tomada)  else'1')+"&pr=0");
                    
                else: 
                    response = requests.Response()
                    response.status_code = 0
                    response._content = b'Porta '+str(tomada).encode()+b' desabilitada!!'
                    return response
                    
            elif op == 1:                
                #if(len(ac_name)>0):
                return self.reqGETHTTP("http://" + self.ip + "/output.htm?porta=" + str(tomada) + "&rmac=" + ("true" if habilita else "false") + "&nt=" + ac_name);
                    
                #else: return "Digite um nome válido para a tomada!!";
                
        else: return 'Equipamento não conectado';

    def getRmac(self, tomada):
        resp = False
        if tomada == 1: resp = self.lastInfo['rmac1'] == 'true';
        elif tomada == 2: resp = self.lastInfo['rmac2'] == 'true';
        elif tomada == 3: resp = self.lastInfo['rmac3'] == 'true';
        elif tomada == 4: resp = self.lastInfo['rmac4'] == 'true';
        elif tomada == 5: resp = self.lastInfo['rmac5'] == 'true';
        elif tomada == 6: resp = self.lastInfo['rmac6'] == 'true';
        elif tomada == 7: resp = self.lastInfo['rmac7'] == 'true';
        elif tomada == 8: resp = self.lastInfo['rmac8'] == 'true';
        elif tomada == 9: resp = self.lastInfo['rmac9'] == 'true';
        elif tomada == 10: resp = self.lastInfo['rmac10'] == 'true';

        return resp;

    def getAc(self, tomada):
        resp = False
        if tomada == 1: resp = self.lastInfo['ac0'] =='0';
        elif tomada == 2: resp = self.lastInfo['ac1'] =='0';
        elif tomada == 3: resp = self.lastInfo['ac2'] =='0';
        elif tomada == 4: resp = self.lastInfo['ac3'] =='0';
        elif tomada == 5: resp = self.lastInfo['ac4'] =='0';
        elif tomada == 6: resp = self.lastInfo['ac5'] =='0';
        elif tomada == 7: resp = self.lastInfo['ac6'] =='0';
        elif tomada == 8: resp = self.lastInfo['ac7'] =='0';
        elif tomada == 9: resp = self.lastInfo['ac8'] =='0';
        elif tomada == 10: resp = self.lastInfo['ac9'] =='0';

        return resp;

    def getNomeAC(self, tomada):
        if tomada == 1: return self.lastInfo['nt1']
        elif tomada == 2: return self.lastInfo['nt2']
        elif tomada == 3: return self.lastInfo['nt3']
        elif tomada == 4: return self.lastInfo['nt4']
        elif tomada == 5: return self.lastInfo['nt5']
        elif tomada == 6: return self.lastInfo['nt6']
        elif tomada == 7: return self.lastInfo['nt7']
        elif tomada == 8: return self.lastInfo['nt8']
        elif tomada == 9: return self.lastInfo['nt9']
        elif tomada == 10: return self.lastInfo['nt10']

    def getDate(self):
        return self.lastInfo['rtc_days']+'/'+self.lastInfo['rtc_months']+'/'+self.lastInfo['rtc_years']

    def getTime(self):
        return self.lastInfo['rtc_hours']+':'+self.lastInfo['rtc_minutes']+':'+self.lastInfo['rtc_seconds']

    def getUptime(self):
        return self.lastInfo['updia']+'d '+self.lastInfo['uphora']+'h '+self.lastInfo['upmin']+'m'