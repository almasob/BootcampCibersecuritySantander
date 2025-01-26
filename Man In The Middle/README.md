# MAN IN THE MIDDLE  
Este tipo de ataque permite um invasor espiar, conversar ou transferir dados entre as duas partes.  
Permite ao invasor interceptar dados, acessar senhas e fundos, envio de links maliciosos, e tudo isso camuflado.  
Lembrando que estou utilizando 3 máquinas virtuais na mesma LAN: Kali, Windows 7 e Metasploitable.  
Utilizaremos o Kali como origem do ataque, o Metasploitable como servidor do sistema vulnerável (DVWA) e o Windows 7 como o cliente.  
**Metasploitable** é uma máquina virtual vulnerável projetada especificamente para ser usada como alvo em testes de penetração e treinamento.  
A **DVWA(Damn Vulnerable Web Application)** é uma aplicação web vulnerável que foi projetada especificamente para ajudar no aprendizado de segurança de aplicações web em segurança cibernética.   
A DVWA já vem pré instalada no Metasploitable.

### FERRAMENTAS ÚTEIS
- WireShark
- Ettercap
- Cain e Abel
- Bettercap
- Máquinas Virtuais

## PASSO A PASSO DO WIRESHARK
Com o Wireshark conseguimos interceptar os pacotes trafegando entre o Kali e outros hosts da rede.  
Não intercepta nem manipula dados trafegando entre hosts terceiros.  
* Primeiro precisamos saber o IP do servidor DVWA(que é o MESTASPLOITABLE).
Digite `ip addr` no console do Metasploitable.  
No meu caso o ip é `192.168.56.101`  
No browser do Kali , iremos acessar o 192.168.56.101/dvwa.  
* Agora vamos abrir o Wireshark no Kali.  
Nas opções da captura dê um duplo clique no “ETH0” que é a interface padrão da rede local.  
Já iniciou a captura dos dados na rede.  
* Agora no browser, faça o login com qualquer informação no DVWA.  
Filtramos o conteúdo no Wireshark `http.request.method == “POST" `  
Agora conseguimos ter acesso aos dados de login no “HTML Form”.  
<img src="https://github.com/user-attachments/assets/eccfafb6-fe80-4c8b-a64f-180658a1181d" width = "800">



- Agora faremos o login com os dados corretos: login = admin, senha = password.  
Agora estamos logado no DVWA e conseguimos capturar os dados também.  
<img src = "https://github.com/user-attachments/assets/304de917-f32c-4da2-afa1-4b5cf084404e" width = "800">

## PASSO A PASSO COM ETTERCAP
**ETTERCAP** é conjunto de ferramentas para ataques man in the middle, mais avançado que o wireshark.  
Com ele, conseguiremos interceptar e manipular dados sendo trafegados entre hosts diferentes na rede.


* No terminal do Kali, digitamos `ettercap -G` para abrir a interface gráfica da ferramenta.  
Neste caso, utilizaremos o Windows 7 como cliente, e não o nosso próprio Kali.

* Primeira coisa que faremos, é escanear a rede, clicando na “lupa”, e depois no ícone ao lado da lupa, que é a “lista” de hosts encontrados.  
![unnamed](https://github.com/user-attachments/assets/7b266a2c-d4a9-45de-8e7b-aed9d12cb5b6)


* Sabemos o IP dos alvos, então:  
Definimos o IP do Metasploitable, que roda o DVWA, como “Target 1”.  
E o IP do cliente Windows 7 como “Target 2”.   
![unnamed](https://github.com/user-attachments/assets/9b5d8bcc-a293-42c3-af68-4652a8bec328)


* Agora iniciamos o “sniff”, apertando no ícone do “PLAY”.  
* Antes de iniciar os testes, precisamos habilitar o IP Forwarding no Kali.  
O **IP forwarding** é uma função do kernel do Linux que permite que o sistema roteie pacotes entre diferentes interfaces de rede.  
Isso permite que o sistema intercepte o tráfego passando entre 2 hosts, e faça o encaminhamento entre eles.  
Por padrão o valor desta função é “0”, ou seja, interceptamos o tráfego, mas não encaminhamos ao destino, quebrando a comunicação.  
Precisamos ativar essa função para que o ataque MitM funcione.  
Para ativar esta função, mudamos seu valor para “1”, com o seguinte comando no terminal do Kali:  
`echo 1 > /proc/sys/net/ipv4/ip_forward`  
* Agora, configuramos no Ettercap o “ARP Poisoning”.  
ARP Poisoning, é uma técnica para redirecionar o tráfego de rede entre dois dispositivos, manipulando as tabelas ARP dos dispositivos na rede local, para que o atacante receba e redirecione os dados entre os hosts.  
![unnamed](https://github.com/user-attachments/assets/18bcd7e8-d770-457b-9051-ed4041402a3e)


* Agora que está tudo configurado, é só dar PLAY no Ettercap para iniciar a captura.
* Agora abrimos o DVWA no Windows, realizamos o login e pronto, os dados são capturados no Ettercap.
![unnamed](https://github.com/user-attachments/assets/6f30aa36-3997-4cd9-a22e-4aeb909ea4e9)


