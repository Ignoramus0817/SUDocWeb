from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives

def sendHtmlEmail(link, sourceEmail, destinationEmail, username):
    subject = 'DocSys激活邮件'
    html_content = '请点击以下链接以激活账户<a href = "http://127.0.0.1:8000/activate/' + link + '/' + username + '">127.0.0.1:8000/activate/' + link + '/' + username + '</a>' 
    msg = EmailMultiAlternatives(u'DocSys激活邮件', from_email = sourceEmail, to = destinationEmail)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    