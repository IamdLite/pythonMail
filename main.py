import smtplib
import datetime as dt
import pandas
import random

# Enter the newly created random email here
MY_EMAIL = "example@gmail.com" 

# Enter the password of the email
MY_PASSWORD = "password"

PLACE_HOLDER = "[name]"
# The placeholder will be replaced by the various names to customize the wishes
list_birthdays = []


now = dt.datetime.now()
month_day = (now.month, now.day)

data = pandas.read_csv("./birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

          
if month_day in birthdays_dict:
   birthday_person = birthdays_dict[month_day]
   with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as file:
        mail = file.read()
        custom_mail = mail.replace(PLACE_HOLDER, birthday_person["name"])   

        with smtplib.SMTP("smtp.gmail.com",  587) as connection:
            connection.starttls()
            connection.login(user = MY_EMAIL, password = MY_PASSWORD )
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"subject:Happy birthday\n\n{custom_mail}"
            )

