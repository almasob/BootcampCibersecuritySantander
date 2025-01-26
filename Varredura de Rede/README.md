# VARREDURA DE REDES com NMAP
**NMAP** é a ferramenta de varredura pela linha de comando.  
**ZENMAP** é a ferramenta de varredura por interface gráfica.  

## Passo a passo de uma simples varredura
Abrimos as VMs do Kali, Metasploitable e Windows 7.  
Ambas devem estar na mesma rede LAN.  
No Kali, utilizaremos o comando `nmap -sn 192.185.56.0/24` para fazer a varredura na rede.  
`-sn` é um parâmetro para retornar apenas os hosts que estão ONLINE.  
![unnamed](https://github.com/user-attachments/assets/955324da-3a60-47ca-896a-c0bdf72ecdba)

Podemos complementar o comando, utilizando `> varredura.txt`.  
Dessa forma, iremos criar um arquivo com o resultado da pesquisa.  
![unnamed](https://github.com/user-attachments/assets/e6189a17-2ad6-4891-8f55-b2243c183f6a)

Utilizamos o comando `nano varredura.txt` para ler o arquivo:  
![unnamed](https://github.com/user-attachments/assets/d9303fe7-8a3f-4dcb-adfb-f5898d5966ae)

Agora que sabemos os IPs dos dispositivos na rede, podemos utilizar parâmetros para coletar informações específicas.  
Irei dar 2 exemplos:  
`nmap -O 192.168.56.101` irá mostrar o sistema operacional e algumas informações do dispositivo alvo  
![unnamed](https://github.com/user-attachments/assets/da8bc754-3f33-4e08-8416-ca0370d43fcb)


`nmap -A 192.168.56.101` irá fazer uma varredura mais avançada, detectando o ST, serviços ativos e versões, executa scripts para coleta de informações, mostra o caminho percorrido pelos pacotes.  
- O resultado deste exemplo, é uma sáida muito extensa, então, deixo para você testar em sua própria máquina.
