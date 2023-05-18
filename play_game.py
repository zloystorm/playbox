import time

from loguru import logger
from playwright.sync_api import sync_playwright
from pynput.keyboard import Key, Controller




def main():
    with sync_playwright() as p:
        with open('verif_mails.txt') as file_to_emails:
            while True:
                jopech = file_to_emails.readline()
                email = jopech.split(":")[0]
                email_pass = jopech.split(":")[1]
                browser_type = p.chromium
                browser = browser_type.launch(headless=False)
                page = browser.new_page()

                page.goto('https://www.playbux.co/login')
                time.sleep(2)
                # page.get_by_role("button", name="Go to Login").click()

                page.get_by_placeholder("email@example.com").fill(email)
                time.sleep(1)
                page.get_by_placeholder("Enter password").fill("Dima28111756d!")
                time.sleep(1)
                page.get_by_role("button", name="Login").click()
                time.sleep(1)
                logger.info(f'{email} Login: done')
                with page.expect_popup() as page1_info:
                    page.get_by_role("img", name="1BRK").click()
                    page = page1_info.value
                keyboard = Controller()
                page.get_by_text("E", exact=True).click()
                page.get_by_text("E", exact=True).click()
                page.get_by_text("E", exact=True).click()
                page.get_by_text("E", exact=True).click()
                page.get_by_text("E", exact=True).click()

                time.sleep(0.5)
                keyboard.press('a')
                keyboard.press('w')
                time.sleep(0.6)
                keyboard.release('a')
                keyboard.release('w')
                time.sleep(0.5)


                keyboard.press('e')
                keyboard.release('e')
                page.get_by_role("button", name="Draw").click()
                time.sleep(1)
                page.get_by_role("button", name="icongame/ui/brick_logo.png Insert 1 BRICK").click()
                time.sleep(1)
                page.get_by_role("button", name="Skip")
                time.sleep(8)
                page.screenshot(path=f'screens/{email}-{browser_type.name}.png')
                time.sleep(2)
                browser.close()

                # page.get_by_text("E", exact=True).click()


if __name__ == '__main__':
    main()
