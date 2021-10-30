
import pandas
import smtplib
import datetime as dt
import random
src="D:\us-states-game-start\letter_templates\birthdays.csv"
data = pandas.read_csv(src)
data_dict = data.to_dict()
dtobj= dt.datetime.now()
my_email = "utest3926@gmail.com"
pass1 = "Test@1234"
connection = smtplib.SMTP("smtp.gmail.com")
if dtobj.month == data_dict['month'][0] and dtobj.day == data_dict['day'][0]:
    with open(r"D:\us-states-game-start\letter_templates\letter_1.txt") as quote_file:
        wish = quote_file.read()
        wish = wish.replace("[Name]","Dad")
    connection.starttls()
    connection.login(user=my_email,password=pass1)
    connection.sendmail(from_addr = my_email,to_addrs = "testuser065@yahoo.com",msg = f"Subject: Happy Birthday! \n\n {wish}")
    connection.close()





