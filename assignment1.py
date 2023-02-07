import datetime
import os
import pandas as pd
import smtplib

#To print time and current directory path
current_time = datetime.datetime.now()
curDir = os.getcwd()

print("\nCurrent directory:", curDir)
print("Task: Automatically copy data from a CSV file into a new CSV and send notification to email once completed.")

# Importing the CSV file created using CSVpad software
print("\n--Importing the CSV file.--")
original_file = "Students Grade For Test 2 Arab Language.csv"
data = pd.read_csv(original_file)
print("Original File :", original_file)
print("Current time:", current_time)

# Saving the dataframe to a new CSV file
print("\n--Copying the CSV file.--")
copied_file = "[FINAL] Students Grade For Test 2 Arab Language.csv"
data.to_csv(copied_file, index=False)
print("Copied File :", copied_file)
print("Current time:", current_time)

# Checking the copy process successful or not
print("\n--Checking the output file.--")

# Specify output path
#path = "/home/izzatisanosi/Desktop/Advance Programming/Assignments/Assignment 1/[FINAL] Students Grade For Test 2 Arab Language.csv"
path = curDir + "/" + copied_file
 
# Check whether the specified output path exists or not, send email if exist
isExist = os.path.exists(path)
if isExist == True:
    print("The output file exists. Sending notification to email...")

    sender_email = 'izzatisanosi98@gmail.com'
    password = ''
    receiver_email = 'sitinurizzati@graduate.utm.my'

    message = """Subject: !!SUCCESSFULLY EXPORT CSV!!

    Konnichiwa!
    The data has been successfully copied and saved to a new CSV file.
    Arigatou gozaimashita."""

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()
    
    print("\nCopy Completed! Email notification was sent to", receiver_email, "!")
    print("Current time:", current_time, "\n")
