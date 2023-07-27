import os
import smtplib
import email.message

class Email:

    def __init__(self):
        self.remetente = ""
        self.senha = ""
        parametros = self.config_email()
        for p in parametros:
            if p[0] == "remetente": self.remetente = p[1]
            if p[0] == "senha": self.senha = p[1]

    def enviar_email(self, remetente, destinatario, assunto, mensagem):
        global _remetente
        global _senha

        if remetente == "":
            remetente = self.remetente

        msg = email.message.Message()
        msg["Subject"] = assunto
        msg["From"] = remetente
        msg["To"] = destinatario
        password = self.senha
        msg.add_header("Content-Type", "text/html")
        msg.set_payload(mensagem)

        s = smtplib.SMTP("smtp.gmail.com: 587")
        s.starttls()
        s.login(msg["From"], password)
        s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))

        return True

    def config_email(self):
        parametros = []
        with open(os.path.dirname(os.path.realpath(__file__)) + "/email_config.txt") as arquivo:
            linhas = arquivo.readlines()
            arquivo.close()

        for linha in linhas:
            if "remetente" in linha:
                parametros.append(["remetente", linha.split("=")[1].strip().replace('"', '').replace('\n', '')])

            if "senha" in linha:
                parametros.append(["senha", linha.split("=")[1].strip().replace('"', '').replace('\n', '')])

        return parametros