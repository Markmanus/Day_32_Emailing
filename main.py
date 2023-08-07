import smtplib

my_email = "test@test.com"
password = "test123"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="Test",
    msg="Subject:Hello\n This is the body of my email. \n\n "

)
connection.close()

