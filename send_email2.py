def send_mail(endereço):
    import smtplib
    import ssl
    from email.message import EmailMessage

    porta = 465

    # colocando as informações da conta que vai mandar o email
    email_adress = "retestping@gmail.com"
    email_pass = "arduinopython"

    # criando mensagem
    mensagem = EmailMessage()
    mensagem["Subject"] = "Flask Email"
    mensagem["From"] = email_adress
    mensagem["To"] = endereço
    mensagem.set_content("Mandei pelo python via Flask este email")

    """
    mensagem.add_alternative("""

    """
    )
    """

    # Criar SSL de contexto seguro
    contexto = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port=porta, context=contexto) as server:
        server.login(email_adress, email_pass)

        server.send_message(mensagem)
