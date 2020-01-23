# Exemplo API Java para Filtro de Linha Smart Web

## 1. Importe as classe necessária
        from voltdevice import VoltDevice

## 2. Instancie um objeto de FiltroSmartWeb

        """
                O objeto deve ser instanciado passando 3 argumentos:
                -username: String = nome de usuário para autenticação
                -password: String = senha de usuário para autenticação
                -ip: Endereço IP do equipamento
        """
        self.vd = VoltDevice('admin','voltvolt','192.168.0.90')
        
        
## 3. Funções

### 3.1. Atualizar informações salvas no objeto equip
        """ def updateInfo(self)

        Este método realiza uma requisição GET ao equipamento pedindo as informações atualizadas e retorna um valor inteiro com o código de resposta HTTP.
        É responsável por atualizar todos os atributos do objeto com as informações recebidas, como estado das tomadas, temperatura e outros parâmetros e configurações do equipamento.
           Retorno: 
           -200: Requisição realizada com sucesso e Informações atualizadas no objeto
           -401: Requisição recusada por falha na autenticação
           -500: Equipamento inacessível    

        """

        resp = self.vd.updateInfo()

### 3.2. Informações do equipamento

#### 3.2.1 Informação de status da tomada (Ligada/Desligada)

    """def getAc(self, tomada):
        A função retorna uma Boolean com o status (True = ligada / False: desligada) da tomada (1-10) passada como argumento   
        resp = self.vd.getAc(tomada):
    """
    #Exemplo:
    stTomada1 = self.vd.getAc(1);
    #print(stTomada1) #True/False

#### 3.2.2 Informação de status da tomada (Habilitada/Desabilitada)

    """def getRmac(self, tomada):
        A função retorna uma Boolean com o status (True = Habilitada / False: Desabilitada) da tomada (1-10) passada como argumento   
        resp = self.vd.getRmac(tomada):
    """
    #Exemplo:
    stTomada1 = self.vd.getRmac(1);
    #print(stTomada1) #True/False

#### 3.2.3 Nome da tomada (Ligada/Desligada)

    """def getNomeAc(self, tomada):
        A função retorna uma String com o status (True = ligada / False: desligada) da tomada (1-10) passada como argumento   
        resp = self.vd.getNomeAc(tomada):
    """
    #Exemplo:
    NomeTomada1 = self.vd.getNomeAc(1);
    #print(NomeTomada1)

#### 3.2.4 Uptime do equipamento

    """def getUptime(self):
        A função retorna uma String com o uptime do equipamento
        Exemplo de retorno: '12d10h8m' 
        resp = self.vd.getUptime()
    """
    #Exemplo:
    uptime = self.vd.getNomeAc(1);
    #print(uptime) 

### Preparando restante da biblioteca para manipulação das informações



## 4. Controle de Tomadas
    """ def ctrlAc(self, tomada, op, habilita=True, ac_name="")

        Ao método controlTomda, devem ser passados os argumentos: 
        -tomada: number:(0-10) tomada que receberá o comando
        -op:Comando a ser enviado à tomada (0:liga/desliga ; 1:habilita/desabilita e configura nome da porta)
        -habilita: opcional Boolean para infomar a configuração a ser realizada na tomada( True: Habilitar / False: Desabilitar)
        -ac_name: opcional string com um nome para a porta, obrigatório para op 1(mudar nome da porta). Caso op seja 0 , não é necessário esse argumento para o método

        Este método retorna um objeto requests.Response com o código de resposta HTTP da requisição realizada no atributo status_code e a informação de erro em caso de código de resposta diferente de 200, acessível no atributo content
        {
                200: sucesso
                401: Falha na autenticacação
                500: Equipamento não localizado
        }
    """

    resp = self.vd.ctrlAc(tomada, op, habilita, ac_name); 
    

### Exemplos:
### 4.1. Ligar/Desligar Tomada:
    resp = self.vd.ctrlAc(1,0) #args: tomada 1 e op 0. Inverte o estado da tomada 1 (Liga/Desliga)
    #print(resp.status_code)
    #print(resp.content.decode())# devido ao atributo content ser em bytes

### 4.2. Configurar status (Habilitada/Desabilitada) e nome da Tomada:
     resp = self.vd.ctrlAc(3, 2, True, 'teste_tomada'); #args: tomada 3, op 2 e habilita True. Configura o status da tomada como 'Habilitada' e o nome da tomada 3 para 'teste_tomada'
     #print(resp.status_code)
     #print(resp.content.decode())# devido ao atributo content ser em bytes
     

## 5. Configurar interface Ethernet
     
     """ def configEthernet(self, boolDhcp, newhost, newip, newgtw, newmask, newdns1, newdns2):

        À função configEthernet, devem ser passados os argumentos: 
        -boolDhcp: Boolean (True habilita DHCP do equipamento / False desabilita)
        -newhost: String ( Hostname à ser configurado no equipamento)
        -newip: String ( Endereço IP a ser configurado no equipamento)
        -newgtw: String ( Endereço de gateway a ser configurado no equipamento)
        -newmask: String ( Máscara de rede a ser configurada no equipamento)
        -newdns1: String ( Endereço de DNS primário)
        -newdns2: String ( Endereço de DNS secundário)

       Este método retorna um objeto requests.Response com o código de resposta HTTP da requisição realizada no atributo status_code e a informação de erro em caso de código de resposta diferente de 200, acessível no atributo content
        {
                200: sucesso
                401: Falha na autenticacação
                500: Equipamento não localizado
        }

    """
    resp = self.vd.configEthernet(boolDhcp, newhost, newip, newgtw, newmask, newdns1, newdns2)
### Exemplo
        """
        Configurar a interface de rede com os argumentos:
        Hostname: 'Filtro de Linha'
        IP: '192.168.0.91'
        Gateway: '192.168.0.1'
        Máscara de rede: '255.255.255.0'
        DNS Primário: '8.8.8.8'
        DNS Secundário: '8.8.4.4'

            
        """
        resp = self.vd.configEthernet(False, 'Filtro de Linha', '192.168.0.91', '192.168.0.1', '255.255.255.0', '8.8.8.8', '8.8.4.4');
        #print(resp.status_code)
        #print(resp.content.decode())# devido ao atributo content ser em bytes