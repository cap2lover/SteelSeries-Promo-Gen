import undetected_chromedriver as uc
from account_generator_helper import GmailNator
from selenium.webdriver.common.by import By
from selenium import webdriver
import warnings, os, time, requests
from random import randint

api = "https://127.0.0.1:50997"

warnings.filterwarnings('ignore')


def newTry():
    waitedOnPage = 0
    passw = "$y$yG€n-" + str(randint(10000,1000000)) + "-@#"
    mail = GmailNator()
    mail.set_email(mail.get_email_online(False,True,True))
    email = mail._email
    payload = {
        "acceptedPrivacyPolicy" : True,
        "email" : email,
        "password1" : passw,
        "password2" : passw,
        "subscribeToNewsletter" : True
    }
    print("Generating [" + email + "]")
    uwu = requests.post(api + "/user", verify=False, json=payload)
    if "429" in uwu.text:
        time.sleep(30)
    time.sleep(3)
    for _letter in mail.get_inbox():
        try:
            mailVerif = str(_letter.letter).replace("\r\n", "").strip()
            mailVerif = mailVerif.split('<a href="')[2]
            mailVerif = mailVerif.split('" style="border: solid 1px #fc4c02; box-sizing: border-box; cursor: pointer; display: inline-block; font-size: 16px; font-weight: normal; margin: 0; padding: 15px; text-decoration: none; line-height: 1; background-color: #fc4c02; border-color: #fc4c02')[0]
            if "http://link.steelseries.com/ls/click" not in mailVerif:
                return
            print("MailVerif Link [" + mailVerif[:40] + "]")
            driver = uc.Chrome(driver_executable_path='driver.exe')
            driver.get(mailVerif)
            while "Register an account" not in driver.page_source:
                time.sleep(1)
                waitedOnPage += 1
                if "Verify you are human" in driver.page_source:
                    driver.find_element(By.XPATH, '//*[@id="challenge-stage"]/div/input').click()
                if waitedOnPage == 60:
                    return
                pass
            waitedOnPage = 0
            driver.find_element(By.XPATH, '//*[@id="js-login-form-root"]/div/div/form/div[1]/label/input').send_keys(email)
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="js-login-form-root"]/div/div/form/div[2]/label/input').send_keys(passw)
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="js-login-form-root"]/div/div/form/button').click()
            while "Account successfully verified." not in driver.page_source:
                time.sleep(1)
                waitedOnPage += 1
                if waitedOnPage == 60:
                    return
                pass
            driver.close()
            payload = {
                "name" : "discordnitrodec2022"
            }
            reques = requests.post(api + "/promos/code", verify=False, json=payload)
            req = reques.json()
            print(Fore.GREEN + f"Code: {req['promocode']:30} | Email: {email} | Pass: {passw}")
            with open("account.txt", "a", encoding="utf-8") as myfile:
                myfile.write(f"{email}:{passw} | {req['promocode']}\n")
            with open("codes.txt", "a", encoding="utf-8") as myfile:
                myfile.write(f"{req['promocode']}\n")
        except:
            if 'dotcom' in reques.text:
                print(reques.text)
                print("Rate Limited, Changing ip")
                while True:
                    try:
                        requests.get("https://google.com")
                        break
                    except:
                        time.sleep(3)
                return
            else:
                print(reques.text)



if __name__ == '__main__':
    gene = 0
    while True:
        if gene == 4:
            time.sleep(40)
            gene = 0
        os.system('taskkill /f /IM SteelSeriesGGClient.exe>temp')
        os.system('start cmd /c "C:\Program Files\SteelSeries\GG\SteelSeriesGGClient.exe"')
        time.sleep(1)
        newTry()
        time.sleep(1)
        gene += 1