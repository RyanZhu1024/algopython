import smtplib

# list of email_id to send the mail
li = ["troyzx1024@gmail.com"]

for i in range(len(li)):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("troyzx1024@gmail.com", "Xuan1024!")
    message = "Message_you_need_to_send"
    s.sendmail("troyzx1024@gmail.com", li[i], message)
    s.quit()