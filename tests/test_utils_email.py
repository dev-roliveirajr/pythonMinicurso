import sys
sys.path.append(".")

from src.models.utils_email import Email

def test_parametros():
    email = Email()
    assert [email.remetente, email.senha] != ["", ""]


def test_email():
    email = Email()
    mensagem = "<P>Olá,</P><P>Segue o relatório semanal de vendas:</P><PRE>==== Corpo da mensagem ====</PRE><P>Obrigado.</P>"
    assert email.enviar_email(email.remetente, "cihadak356@muzitp.com", "Relatório Semanal", mensagem) == True



