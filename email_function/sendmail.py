def send_mail(send_to = 'Khatantuulb@ot.mn', send_from = "Erkhembayare@riotinto.com", subject = "test for dictionary",
              server="mnoytsmtp1.corp.riotinto.org"):
    # assert isinstance(send_to, list)
    
    from os.path import basename
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.utils import COMMASPACE, formatdate
    # from emailtemp import html
    from query import get_sub_emails, get_random_words
    from email_function.emailtemp import template_for_email
    import smtplib
    
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    html = template_for_email()
    # html = """\
    # <html>
    #   <head></head>
    #   <body>
    #     <p>Hello GDM,<br><br>
    #     Following Excavations are <b>'{}'</b> not successfully imported to CaveCad! Please check on <a href="https://mnoytap14.corp.riotinto.org/ot/CaveCad_GS/App/FileImport?projectid=1/">CaveCad</a><br><br><br>
        
    #     <small>This is an automated email from QC and Excavation Display. Do no reply</small>
    #     </p>
    #   </body>
    # </html>""".format(text)
    
    msg.attach(MIMEText(html, 'html'))

    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
    print('Email has been sent!')