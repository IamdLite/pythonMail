import smtplib
import datetime as dt
import pandas

# Enter the newly created random email here
MY_EMAIL = "example@gmal.com" 

# Enter the password of the email
MY_PASSWORD = "password"

PLACE_HOLDER = "[name]"
# The placeholder will be replaced by the various names to customize the wishes
list_birthdays = []

birthdays = pandas.read_csv("./birthdays.csv")
list_birthdays = birthdays.to_dict(orient="records")
mailing_day = dt.datetime.now().day
mailing_month = dt.datetime.now().month

def get_message(name):
    with open("./letter_templates/letter_3.txt") as file:
        mail = file.read()
        new_mail = mail.replace(PLACE_HOLDER, f"{name}")
        return new_mail
          
for birthday in list_birthdays:
    name = birthday["name"]
    name = dt.datetime(year=birthday["year"], month=birthday["month"], day=birthday["day"])
    
    if name.date().day == mailing_day and name.date().month == mailing_month:
        custom_mail = get_message(birthday["name"])  
        with smtplib.SMTP("smtp.gmail.com",  587) as connection:
            connection.starttls()
            connection.login(user = MY_EMAIL, password = MY_PASSWORD )
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday["email"],
                msg=f"subject:Happy birthday\n\n{custom_mail}"
            )

