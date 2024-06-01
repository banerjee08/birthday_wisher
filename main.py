##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and
# replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas as pd
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

file_path = "birthdays.csv"

# Reading the csv file
df = pd.read_csv(file_path)

# converting the data into tuples
data_tuples = [tuple(row) for row in df.values]

now = dt.datetime.now()
current_month = now.month
current_date = now.day


# email address and password
my_email = "banerjee.sumanto.developer@gmail.com"
password = "xfuu ucwz ynvj waea"

# iterating over the tuple
for person in data_tuples:
    name, email, year, month, date = person

    # generating random number
    random_letter_num = random.randint(1, 3)
    # print(random_letter_num)

    # checking if the birthday of a person matched today's date
    if month == current_month and date == current_date:
        with open(f"./letter_templates/letter_{random_letter_num}.txt") as letter:
            letters = letter.read()
            birthday_letter = letters.replace("[NAME]", f"{name}")
            print(birthday_letter)

        msg = MIMEMultipart()
        msg["From"] = my_email
        msg["To"] = email
        msg["Subject"] = "Happy Birthday!!!"

        msg.attach(MIMEText(birthday_letter, "plain"))

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)

            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=msg.as_string()
            )
