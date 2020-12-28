##################### Normal Starting Project ######################
import datetime as dt
import pandas
from random import randint
import smtplib
from email.mime.image import MIMEImage
my_user = "tj.coder1975@gmail.com"
my_pass = "BlueOcean75@"

# Instantiate a new object from dt:
today = dt.datetime.now()

# 2. Check if today matches a birthday in the birthdays.csv
today_month = today.month
today_day = today.day
today_tuple = (today_month, today_day)

# Create a dictionary from birthday.csv
birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = {index: (row["month"], row["day"]) for (index, row) in birthdays.iterrows()}

for index in birthdays_dict:

    birthday_date = birthdays_dict[index]
    if birthday_date == today_tuple:
        birthday_person = birthdays["name"][index]
        birthday_email = birthdays["email"][index]

        # Create a new random birthday card:
        file_path = f"./letter_templates/letter_{randint(1, 3)}.txt"
        with open(file_path) as file:
            letter = file.read()
            letter = letter.replace("[NAME]", birthday_person)

        with open("./cards_sent/cards.txt", mode="a") as file:
            file.write(letter)

        # 4. Send the letter generated in step 3 to that person's email address.
        # User credentials:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Secure mail server connection:
            connection.starttls()

            # Login to Gmail:
            connection.login(user=my_user, password=my_pass)

            # Send email:
            connection.sendmail(
                from_addr=my_user,
                to_addrs=birthday_email,
                msg=f"Subject: Happy Birthday!\n\n{letter}".encode("utf8")
            )
