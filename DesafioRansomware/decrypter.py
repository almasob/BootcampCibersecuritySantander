#Importamos as bibliotecas 
import os  #maneira de interagir com o sistema operacional
import pyaes #implementa algoritmos para criptografia

#abertura do arquivo de texto para teste
file_name = 'teste.txt.ransomwaretroll'  #armazena na variável o nome do arquivo que será utilizado
file = open(file_name, "rb") #abre o arquivo no modo leitura binária (rb)
file_data = file.read() #lê o conteudo do arquivo e armazena na variável, mas não altera o original
file.close()

#remoção do arquivo original
os.remove(file_name)

#criação da criptografia
key = b'testeransomwares' #criação da chave criptográfica, indicando que será tratada como "byte literal"
aes = pyaes.AESModeOfOperationCTR(key) #aqui criamos o objeto que será usado para criptografar os dados

#descriptografia
crypto_data = aes.decrypt(file_data) #descriptografamos o conteudo que tinha dentro do arquivo original e armazenamos aqui

#salvando o novo arquivo descriptografado
new_file = 'teste.txt' #nome do novo arquivo descriptografado
new_file = open(f'{new_file}', 'wb') #arquivo é aberto em modo binário escrita(wb), necessário para dados criptografados
new_file.write(crypto_data) #escrevemos o conteudo criptografado que estava salvo em "crypto_data"
new_file.close()

