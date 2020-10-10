"""
Copyright Bhoshaga 2020
collect_data.py uses selenium to collect information from MyIpo

WINDOWS ONLY - CHROMEDRIVER


"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv
import save_logs
import eel
import threading
import random
import getpass

username = getpass.getuser()

prefix_dir = f"C:\\Users\\{username}\\"




CHROMEDRIVER = f"C:\\Users\\{username}\\aimes\\data_files\\chromedriver.exe"


is_countdown = None


def printed_update(update):
    print(update)
    main_update(update)
    save_logs.log(update)


def main_update(update):
    eel.mainUpdate(update)


def stat_update(status):
    eel.statUpdate(status)


def stat_deets_update(deets):
    eel.statDeetsUpdate(deets)


def countdown(dur):

    global is_countdown
    while is_countdown:
        if dur > 60:
            minutes = dur // 60
            seconds = dur % 60
        else:
            minutes = 0
            seconds = dur
        # Format string
        if minutes == 0 and seconds == 0:
            stat_deets_update("processing...")
            break
        if minutes == 1:
            p_min = f'{minutes} min    '
        elif minutes > 1:
            p_min = f'{minutes} mins   '
        else:
            p_min = ""
        if seconds == 1:
            p_sec = f'{seconds} sec'
        elif seconds > 1:
            p_sec = f'{seconds} secs'
        else:
            p_sec = ""


        formated_ct = (f'{p_min}{p_sec}')
        if (seconds + 1) % 5 == 0:
            item = 'Reading MyIPO'
        else:
            item = formated_ct
        stat_deets_update(item)
        sleep(1)
        dur = dur - 1
    else:
        stat_deets_update("completed...")



def collect(start_date, end_date, today_file):

    global is_countdown
    is_countdown = True
    x = threading.Thread(target=countdown, args=[600])
    x.start()
    date_1 = start_date
    date_2 = end_date

    try:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(CHROMEDRIVER, options=options)
        # driver = webdriver.Chrome(CHROMEDRIVER)
        printed_update('Called chromedriver!')
    except:
        printed_update('cannot do chromedriver :(')
    # actionChain = webdriver.ActionChains(driver)
    # stat_update("Collecting Data")
    # stat_deets_update("Reading MyIPO")
    myipo = 'https://iponlineext.myipo.gov.my/SPHI/Extra/IP/TM/Qbe.aspx?sid=637190123825263638'
    driver.get(myipo)
    printed_update("Successfully opened website")
    sleep(2)
    """
    # LOGGING IN OPTION BELOW
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Login')]"))).click()
    # driver.find_element_by_xpath("//a[contains(text(), 'Login')]").click()
    sleep(2)
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//input[@type=\"text\"]")))
    driver.find_element_by_xpath("//input[@type=\"text\"]").send_keys(username)
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//input[@type=\"password\"]")))
    driver.find_element_by_xpath("//input[@type=\"password\"]").send_keys(password)
    sleep(2)
    driver.find_element_by_id('MainContent_lnkBtnLogin').click()
    'MainContent_lnkBtnLogin'
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID, 'SidebarContent_SidebarExtra_hdrTM_lblheader'))).click()
    sleep(0.2)
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Search for TM Registered')]"))).click()
    sleep(1)
    """
    printed_update("Clicking Advanced Search")
    WebDriverWait(driver, 16).until(
        ec.element_to_be_clickable((By.ID, "MainContent_lnkTMSearch"))).click()
    driver.find_element_by_xpath("//a[contains(text(), 'Advanced Search')]").click()
    printed_update("Entering dates...")
    WebDriverWait(driver, 16).until(ec.visibility_of_element_located((By.XPATH, "//input[@name=\"ctl00$MainContent$ctrlTMSearch$txtExpirationDateStart\"]")))
    driver.find_element_by_xpath("//input[@name=\"ctl00$MainContent$ctrlTMSearch$txtExpirationDateStart\"]")\
        .send_keys(date_1)
    driver.find_element_by_xpath("//input[@name=\"ctl00$MainContent$ctrlTMSearch$txtExpirationDateEnd\"]")\
        .send_keys(date_2)
    sleep(4)
    printed_update("Clicking search...")
    driver.find_element_by_id('MainContent_ctrlTMSearch_lnkbtnSearch').click()
    try:
        # clicks close pop up
        printed_update("Closed pop-up...")
        close_popup = '/html/body/div[17]/div/div/div[1]/button'
        WebDriverWait(driver, 14).until(ec.element_to_be_clickable((By.XPATH, close_popup)))
        sleep(0.2)
        driver.find_element_by_xpath(close_popup).click()
    except:
        pass

    # table_id = '/html/body/form/div[3]/div[3]/div/div[1]/div[3]/div[1]/div/table/tbody'
    # Change to 200
    printed_update("Reading table...")
    items_per_page = "/html/body/form/div[3]/div[3]/div/div[1]/div[3]/div[1]/div/table/tbody/tr[52]/td/div[3]/select"
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, items_per_page)))
    select = Select(driver.find_element_by_xpath(items_per_page))
    sleep(0.2)
    select.select_by_value('200')
    # tries to select value of 200, then waits for grey padding to disappear when 200 loads.
    try:
        WebDriverWait(driver, 16).until_not(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]')))
    except:
        sleep(3)
    # sort with no agent first
    printed_update("Sorting table...")
    try:
        WebDriverWait(driver, 16).until(ec.element_to_be_clickable((By.XPATH, '/html/body/form/div[3]/div[3]/div/div[1]/div[3]/div[1]/div/table/tbody/tr[1]/th[7]/a'))).click()
    # driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[1]/div[3]/div[1]/div/table/tbody/tr[1]/th[7]/a').click()
    except:
        sleep(5)
    try:
        WebDriverWait(driver, 16).until_not(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]')))
    except:
        sleep(3)
    # Collect Data
    printed_update("Collecting data...")
    t = 1
    with open(today_file, 'w') as f:
        the_writer = csv.writer(f)
        while t < 11: # CHANGE TO 2 FOR TESTING PURPOSES ELSE SHOULD BE 11
            cons = f'PAGE = {t}'
            stat_update(cons)
            printed_update(cons)
            t = t + 1
            for i in range(204):
                # Accessing row i
                try:
                    row = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[1]/div[3]/div[1]/div/table/tbody/tr[' + str(i) + ']')
                    try:
                        # tries to find owner
                        owner = row.find_element_by_xpath(
                            '/html/body/form/div[3]/div[3]/div/div[1]/div[3]/div[1]/div/table/tbody/tr[' + str(
                                i) + ']/td[5]').get_attribute('innerText')

                        # tries to find picture
                        try:
                            picture = row.find_element_by_xpath(
                                '/html/body/form/div[3]/div[3]/div/div[1]/div[3]/div[1]/div/table/tbody/tr[' + str(
                                    i) + ']/td[4]').find_element_by_tag_name('a').get_attribute('href')
                        except:
                            picture = 'no image'
                        # tries to find expiry date
                        try:
                            expiry_date = row.find_element_by_xpath(
                                '/html/body/form/div[3]/div[3]/div/div[1]/div[3]/div[1]/div/table/tbody/tr[' + str(
                                    i) + ']/td[6]').get_attribute('innerText')
                        except:
                            expiry_date = 'no expiry date'
                        # tries to find denomination number
                        try:
                            den = row.find_element_by_xpath(
                                '/html/body/form/div[3]/div[3]/div/div[1]/div[3]/div[1]/div/table/tbody/tr[' + str(
                                    i) + ']/td[3]').get_attribute('innerText')
                        except:
                            den = "no denomination"
                        # tries to get application number
                        try:
                            app_no = row.find_element_by_xpath(
                                '/html/body/form/div[3]/div[3]/div/div[1]/div[3]/div[1]/div/table/tbody/tr[' + str(
                                    i) + ']/td[2]').get_attribute('innerText')
                        except:
                            app_no = "no application number"
                        # tries to get agent / local rep
                        try:
                            agent = row.find_element_by_xpath(
                                '/html/body/form/div[3]/div[3]/div/div[1]/div[3]/div[1]/div/table/tbody/tr[' + str(
                                    i) + ']/td[7]').get_attribute('innerText')
                        except:
                            agent = "no agent"
                        # tries to get legal rep
                        try:
                            legal_rep = row.find_element_by_xpath(
                                '/html/body/form/div[3]/div[3]/div/div[1]/div[3]/div[1]/div/table/tbody/tr[' + str(
                                    i) + ']/td[8]').get_attribute('innerText')
                        except:
                            legal_rep = "no legal rep"
                        # tries to get nice classes
                        try:
                            nice_class = row.find_element_by_xpath(
                                '/html/body/form/div[3]/div[3]/div/div[1]/div[3]/div[1]/div/table/tbody/tr[' + str(
                                    i) + ']/td[9]').get_attribute('innerText')
                        except:
                            nice_class = "no nice class"
                        # tries to get application status
                        try:
                            app_status = row.find_element_by_xpath(
                                '/html/body/form/div[3]/div[3]/div/div[1]/div[3]/div[1]/div/table/tbody/tr[' + str(
                                    i) + ']/td[12]').get_attribute('innerText')
                        except:
                            app_status = "no nice class"

                        printed_update([app_no, den, picture, owner, expiry_date, agent, legal_rep, nice_class, app_status])
                        the_writer.writerow([app_no, den, picture, owner, expiry_date, agent, legal_rep, nice_class, app_status])
                    except:
                        continue

                except:
                    continue
            try:
                if t == 6:
                    WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.LINK_TEXT, '...'))).click()
                else:
                    WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.LINK_TEXT, str(t)))).click()
                WebDriverWait(driver, 16).until_not(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]')))
            except:
                continue

    sleep(2)
    is_countdown = False
    driver.quit()
