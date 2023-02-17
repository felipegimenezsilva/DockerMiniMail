import requests
import wget
import os
import time

# url of mail service
base_url = "https://www.1secmail.com/api/v1"

# folder and file configurations
data_folder   =  './data'
email_folder  = f'{data_folder}/email'
config_folder = f'{data_folder}/config'
config_email  = f'{config_folder}/email.txt'
config_update = f'{config_folder}/updates.txt'
time_seconds =  f'{config_folder}/time_seconds.txt'

# basic function to simplificate requests
get = lambda x : requests.get(f'{base_url}{x}').json()

# backend operations
random_emails = lambda qt : get(f'/?action=genRandomMailbox&count={qt}')
list_messages = lambda login, domain: get(f'/?action=getMessages&login={login}&domain={domain}')
read_message  = lambda login, domain, idm: get(f'/?action=readMessage&login={login}&domain={domain}&id={idm}')
down_attach   = lambda login, domain, idm, file_name, path  : wget.download(
    f'{base_url}/?action=download&login={login}&domain={domain}&id={idm}&file={file_name}', out=path)

# create the folders dinamicaly
def create_folders():
    try: os.makedirs(email_folder)
    except:pass
    try: os.makedirs(config_folder)
    except:pass

# generate emails if not exists
def create_emails( number_emails = 1 ):
    if not os.path.exists(config_email): 
        print("using random emails")
        with open(config_email,"w") as file: file.write('\n'.join(random_emails(number_emails)))
    else: print("using configured emails")

# checks for an update
def check_updates(login, domain):
    last = []
    if os.path.exists(config_update): 
        with open(config_update,"r") as file: last = file.read().split("\n")
    update = [ str(message['id']) for message in list_messages(login,domain) ]
    last = list(filter(lambda x : not x in update, last))    # removing old messages
    update = list(filter(lambda x : not x in last, update))  # getting messages to update
    save_messages(login, domain, update)
    with open(config_update,"w") as file: file.write("\n".join(update))

# format a name for the email
def format_email_name(info):
    return "_".join([
        str(info['id']),
        info['date'],
        info['subject']
    ]) + '.html'

# save an email, and the attachment of this email
def save_messages(login, domain, ids):
    for id_ in ids:
        message = read_message(login, domain, id_)
        body = message.get('body',None)
        if not body: continue
        folder_message = email_folder+'/'+format_email_name(message)
        try: os.makedirs(folder_message)
        except: continue
        with open(f'{folder_message}/message.html','w') as file: file.write(body)
        for attach in message['attachments']:
            filename = attach['filename']
            down_attach(login,domain,id_, filename, f'{folder_message}/att_{filename}')

# read emails from the configuration file
def get_configured_emails():
    if not os.path.exists(config_email): create_emails()
    emails = []
    with open(config_email,'r') as file:
        emails = [ email.split('@') for email in file.readlines()]
    return emails

# read the time seconds from file
def get_time_delay():
    if not os.path.exists(time_seconds):
        with open(time_seconds,"w") as file: file.write("600")
    with open(time_seconds,"r") as file:
        try : delay = int(file.read())
        except: delay = 600
    return delay

# main loop 
def main():
    print("Running Temp-Mail")
    delay = 600
    while True:
        try:
            create_folders()
            delay = get_time_delay()
            emails = get_configured_emails()
            for email,domain in emails: check_updates(email,domain)
        except: pass
        time.sleep( delay )

main()