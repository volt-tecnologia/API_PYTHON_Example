import requests,json;
from requests.auth import HTTPBasicAuth;
from requests.exceptions import Timeout;
class VoltDevice:

    def __init__(self,ip, username, password):
        self.ip = ip if len(ip) > 0 else '127.0.0.1'
        self.username = username;
        self.password = password;
        self.updateInfo()

        #print(self.lastInfo)

    def updateInfo(self):
        resp = self.httpGetInfo();
        
        if resp != 'timeout' and resp !=401 and resp !=402 and resp !=403:
            self.lastInfo = resp;
            return
        else: 
            print('Equipamento não encontrado!!');
            self.lastInfo = 0;
            return resp

    def httpGetInfo(self):
        resp = self.reqGETHTTP('http://'+self.ip+'/status.json');
            

        if resp=='timeout' or resp.status_code==401:
            return resp
        else: return resp.json();

    def reqGETHTTP(self, url):
        print(url);
        try:
            response = requests.get(url,auth=HTTPBasicAuth(self.username,self.password), timeout=2);
            print(response.status_code)

            return response;
        except Timeout:
            print('Erro de Timeout')
            return 'timeout'

        
    def reqPOSTHTTP(self, url, payload):
        print(url);
        try:
            response = requests.post(url,auth=HTTPBasicAuth(self.username,self.password),data=payload, timeout=2);
            #print(response.status_code)
            return response;
        except Timeout:
            print('Erro de Timeout')
            return 'timeout'

    def configEthernet(self, boolDhcp, newhost, newip, newgtw, newmask, newdns1, newdns2):
        payload = {'dhcp':('true' if boolDhcp == True else 'false'),'host':newhost,'ip':newip,'gw':newgtw,'sub':newmask,'dns1':newdns1, 'dns2':newdns2}
        #print(payload)
        response = self.reqPOSTHTTP('http://'+self.ip+'/config.htm?', payload)
        
        if(response != 'timeout' and response.status_code == 200): 
           response = self.reqGETHTTP("http://" + self.ip + "/reset.cgi?timeout=1")
        
        return response 

    def ctrlAc(self, tomada, op, habilita, ac_name):
        if(self.lastInfo != 0):
        
            if op == 0:
                if(self.getRmac(tomada) != 'false'):            
                    return self.reqGETHTTP("http://" + self.ip + "/outpoe.cgi?poe=" + str(tomada) + "&sts="+('0' if self.getAc(tomada) == '0'  else'1')+"&pr=0");
                    
                else: return 'Porta '+str(tomada)+' desabilitada!!'
                    
            elif op == 1:                
                if(len(ac_name)>0):
                    return self.reqGETHTTP("http://" + self.ip + "/output.htm?porta=" + str(tomada) + "&rmac=" + ("true" if habilita else "false") + "&nt=" + ac_name);
                    
                else: return "Digite um nome válido para a tomada!!";
                
        else: return 'Equipamento não conectado';

    def getRmac(self, tomada):
        if tomada == 1: return self.lastInfo['rmac1']
        elif tomada == 2: return self.lastInfo['rmac2']
        elif tomada == 3: return self.lastInfo['rmac3']
        elif tomada == 4: return self.lastInfo['rmac4']
        elif tomada == 5: return self.lastInfo['rmac5']
        elif tomada == 6: return self.lastInfo['rmac6']
        elif tomada == 7: return self.lastInfo['rmac7']
        elif tomada == 8: return self.lastInfo['rmac8']
        elif tomada == 9: return self.lastInfo['rmac9']
        elif tomada == 10: return self.lastInfo['rmac10']

    def getAc(self, tomada):
        if tomada == 1: return self.lastInfo['ac0']
        elif tomada == 2: return self.lastInfo['ac1']
        elif tomada == 3: return self.lastInfo['ac2']
        elif tomada == 4: return self.lastInfo['ac3']
        elif tomada == 5: return self.lastInfo['ac4']
        elif tomada == 6: return self.lastInfo['ac5']
        elif tomada == 7: return self.lastInfo['ac6']
        elif tomada == 8: return self.lastInfo['ac7']
        elif tomada == 9: return self.lastInfo['ac8']
        elif tomada == 10: return self.lastInfo['ac9']

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