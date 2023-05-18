import email
import imaplib
import re
import time

from loguru import logger
import email
import imaplib
import re

from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync


def verif_by_link(mail, link):
    with sync_playwright() as p:
            browser_type = p.firefox
            browser = browser_type.launch(headless=True)
            page = browser.new_page()
            stealth_sync(page)
            page.goto(link)
            time.sleep(3)
            logger.info(f'{mail}: verif')
            browser.close()
            print(f'verif done for: {mail}')


with open('verif_mails.txt', 'r') as mails_obj:
    while True:
        n = 0
        for mail_pass in mails_obj:
            n += 1
            time.sleep(1)
            try:
                mail = mail_pass.split(':')
                print(*mail)
                imap = imaplib.IMAP4_SSL('imap.rambler.ru')
                imap.login(f'{mail[0]}', f'{mail[1]}')
                imap.select('INBOX')

                s = imap.search(None, 'HEADER', 'Subject', '"Confirm your Playbux account"')
                b = str(s[1][0])[2:-1][0]
                try:
                    result, msg = imap.fetch(b, "(RFC822)")
                    msg = email.message_from_bytes(msg[0][1])
                    payload = msg.get_payload()

                    for part in msg.walk():
                        if part.get_content_subtype() == 'plain' and part.get_content_maintype() == 'text':
                            text = part.get_payload(decode=True).decode('utf-8')
                            links = re.findall(r'http\S+', text)

                            logger.info(f'{n}: ты хороший {mail_pass} ')
                            with open('verif_links.txt', 'a') as f:
                                pas = mail[1].replace('\n','')
                                f.write(f"{mail[1]}:{mail[2]}\n")
                                verif_by_link(mail[0],links[0] )
                except:
                    logger.error(f'{n} MAIL: ты идешь нахуй {mail_pass} ')
            except:
                logger.error(f'{n} LOGIN: ты идешь нахуй {mail_pass} ')
