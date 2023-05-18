import time
from sys import stderr

from loguru import logger
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

logger.remove()
logger.add(stderr, format='<white>{time:HH:mm:ss}</white> | <lvl>{message}</lvl>', backtrace=True, diagnose=True)


def main():
    with sync_playwright() as p:
        n = 0
        logger.opt(colors=True).info(f'<g>BOT STARTED</>')
        with open('mails.txt', 'r') as file_to_emails:
            print('okay lets go')
            while True:
                jopech = file_to_emails.readline().split(':')
                logger.opt(colors=True).info(f'{jopech}')
                n += 1
                browser_type = p.firefox
                browser = browser_type.launch(headless=True)
                page = browser.new_page()
                stealth_sync(page)
                site = 'https://www.playbux.co/register'
                try:
                    page.goto(site)
                    page.query_selector('[name="email"]').fill(jopech[0])
                    time.sleep(1)
                    page.query_selector('[name="password"]').fill('Dima28111756d!')
                    time.sleep(1)
                    page.query_selector('[name="confirmPassword"]').fill('Dima28111756d!')
                    time.sleep(1)
                    page.query_selector('[name="agree"]').click()
                    time.sleep(1)
                    page.query_selector('[name="agree"]').check()
                    time.sleep(1)
                    # input('загоглушка')
                    page.query_selector('[type="submit"]').click()
                except:
                    logger.error(f'{n}: {jopech[0]}: button fail')

                try:
                    page.wait_for_selector('[class^="text-red-dark"]', timeout=1000)
                    page.query_selector('[type="submit"]').click()
                except:
                    pass

                try:
                    page.wait_for_selector('[alt="check completed"]', timeout=5000)
                    if page.query_selector('[alt="check completed"]'):
                        logger.opt(colors=True).info(f'<g>{n}: {jopech[0]}: sending emails</>')
                    else:
                        logger.error(f'{n}: {jopech[0]}: sending fail')
                except:
                    logger.error(f'{n}: {jopech[0]}: sending fail')
                time.sleep(1)
                browser.close()


if __name__ == '__main__':
    while True:
        main()
