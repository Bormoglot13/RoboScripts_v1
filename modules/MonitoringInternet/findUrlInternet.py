from automagica import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#def main(excel_path=None):
#    if excel_path is None:
#        excel_path = sys.argv[1]  # 'data.xlsx'
excel_path = sys.argv[1]
email_login = 'robot12378462376@gmail.com'
reciever_email = 'dolzhikds@gmail.com'
email_password = 'Hayg2syA*'
email_smtp_server = 'smtp.gmail.com'

lookup_terms = []
lookup_terms.append(ExcelReadRowCol(excel_path, 1, 2))
browser = ChromeBrowser()

for j, item in enumerate(lookup_terms):

    browser.get('https://google.com')
    browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div/div[1]/input').send_keys(item)
    browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div/div[3]/center/input[1]').submit()
    articles = browser.find_elements_by_class_name("g")
    urls = set()

    for article in articles:
        try:
            import re
            #print(article.text)
            urls.add(re.findall('https?://(?:[-\w./]|(?:%[\da-fA-F/]{2}))+', article.text)[0])
        except:
            pass
    #print(urls)
    #sys.exit()
    for i, url in enumerate(urls):
        ExcelWriteRowCol(excel_path, r=i + 2, c=j + 2, write_value=url)

lookup_terms = []
for col in range(2, 6):
    try:
        lookup_terms.append(ExcelReadRowCol(excel_path, col, 2))
    except:
        pass

print(lookup_terms)

for j, item in enumerate(lookup_terms):
    browser.get('https://yandex.ru')
    browser.find_element_by_xpath('//*[@id="text"]').send_keys(item)
    ActionChains(browser) \
        .key_down(Keys.RETURN) \
        .perform()
browser.quit()

#StartFile(excel_path)

msg = MIMEMultipart()
msg['From'] = email_login
msg['To'] = reciever_email
msg['Subject'] = 'Робот закончил выполнение'
message = 'Приветствую! Робот закончил выполнение запущенной задачи.'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP(email_smtp_server, 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login(email_login, email_password)
mailserver.sendmail(email_login, reciever_email, msg.as_string())
mailserver.quit()


#if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
#    main('/Users/adar7/PycharmProjects/RoboScripts/data.xlsx')