#import dos pacotes necessários
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#criação do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

#criação de um objeto de mensagem
msg = MIMEMultipart()
texto = "Estou enviando um email com Python"

#parâmetros
senha = ""
msg['From'] = ""
msg['To'] = ""
msg['Subject'] = "Teste de Envio de email"

#criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

#Login na conta para envio
server.login(msg['From'], senha)

#envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())
print('Mensagem enviada com sucesso')

#encerramento do servidor
server.quit()




