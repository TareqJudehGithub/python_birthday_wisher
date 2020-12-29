import pandas
import smtplib
import datetime as dt
from random import randint


class BirthdayWisher:
    date = dt.datetime.now()
    day = date.day
    month = date.month
    today_date = (month, day)

    def __init__(self):
        self.my_user = "Your Email address"
        self.my_pass = "Your Email password"
        self.recipients_birthday()

    def recipients_birthday(self):
        """Compare birthdays list birthday date with today's:"""
        birthdays = pandas.read_csv("birthdays.csv")
        birthdays_dict = {index: (row["month"], row["day"]) for (index, row) in birthdays.iterrows()}
        for index in birthdays_dict:
            birthday_date = birthdays_dict[index]
            recipient_name = birthdays["name"][index]
            recipient_email = birthdays["email"][index]

            if self.today_date == birthday_date:
                # Birthday card body:
                files_path = f"./letter_templates/letter_{randint(1, 3)}.txt"
                with open(files_path) as files:
                    card = files.read()
                    recipient_card = card.replace("[NAME]", recipient_name)

                # Send emails to recipients:
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=self.my_user, password=self.my_pass)
                    connection.sendmail(
                        from_addr=self.my_user,
                        to_addrs=recipient_email,
                        msg=f"Subject: Happy Birthday {recipient_name}!\n\n"
                            f"{recipient_card}".encode("utf8")
                    )

                # Save a copy of cards sent in a separate file:
                with open("cards_sent/cards.txt", mode="w") as file:
                    file.write(recipient_card)


BirthdayWisher()
