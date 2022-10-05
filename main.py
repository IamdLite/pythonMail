import smtplib

my_email = "diffouofopa.esdras@ictuniversity.edu.cm"
my_password = "Fopa@ictu2021"

with smtplib.SMTP("smtp.gmail.com",  587) as connection:
    connection.starttls()
    connection.login(user = my_email, password = my_password )
    connection.sendmail(
        from_addr=my_email,
        to_addrs="langmi.prosper@ictuniversity.edu.cm",
        msg="subject:Lp Studio\n\nExpressing emotions through media"
    )