
from voltdevice import VoltDevice



vd = VoltDevice('admin','voltvol','192.168.0.90')
#print(vd.lastInfo)#imprime todas as informações adquiridas do equipamento
#print(vd.configEthernet(False, 'HOST1', '192.168.0.91', '192.168.0.6', '255.255.255.0', '8.8.8.8', '8.8.4.3'));#config ethernet
#print(vd.ctrlAc(3,0,''))

#resp = vd.reqGETHTTP('http://'+vd.ip+'/status.json');
#print(resp.status_code);
#print(resp.json());