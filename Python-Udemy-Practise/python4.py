# UDEMY PYTHON COURSE

import PyPDF2
f = open("C:\\Users\\krish\\OneDrive\\Desktop\\Resume_VibhaMasti.pdf", "rb")
reader = PyPDF2.PdfReader(f)                              # not PdfFileReader (removed in python3)
print(len(reader.pages))                                  # not reader.numPages

# SENDING EMAILS

import smtplib
smtp_object = smtplib.SMTP("smtp.gmail.com", 587)  # TLS encryption

# ELHO method command which greets the sever and establishes a connection

smtp_object.ehlo()
smtp_object.starttls()

import getpass
email = getpass.getpass("email: ")
 # email2 = getpass.getpass("")
password = getpass.getpass("password: ")
smtp_object.login(email, password)

from_address = email
to_address = email
subject = input("enter subject line: ")
message = input("enter the body message: ")
msg = "Subject: " + subject + "\n" + message

smtp_object.sendmail(from_address, to_address, msg)

smtp_object.quit()

# tlakshmipranathi@gmail.com

# VIEWING EMAILS

import imaplib
M = imaplib.IMAP4_SSL("imap.gmail.com")

email = getpass.getpass("email: ")
password = getpass.getpass("password: ")

M.login(email, password)

print(M.list())

M.select("inbox")
typ, data = M.search(None, 'SUBJECT "SECOND TRY"')
email_id = data[0]
result, email_data = M.fetch(email_id, "(RFC822)")

raw_email = email_data[0][1]
raw_email_string = raw_email.decode("utf-8")

import email

email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)




