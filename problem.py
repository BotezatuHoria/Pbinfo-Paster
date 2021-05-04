from selenium import webdriver
import random
import time
import pyautogui

from caine_mort.secrets import *

driver = None

v_list = [i for i in range(1, 4000)]

while True:
    try:
        driver = webdriver.Chrome(PATH)

        idx =  random.randint(0, len(v_list))
        problem_idx = v_list[idx]

        driver.get("http://www.zecelainfo.com/membership-account/login/?redirect_to=http%3A%2F%2Fwww.zecelainfo.com%2Fmembership-account%2F")

        user_login = driver.find_element_by_id('user_login')
        user_login.send_keys(ZECE_LA_INFO_ACC)

        user_pass = driver.find_element_by_id('user_pass')
        user_pass.send_keys(ZECE_LA_INFO_PASS)

        button = driver.find_element_by_id('wp-submit')
        button.click()

        driver.get(f"http://www.zecelainfo.com/{problem_idx}")

        copy_pg = driver.find_element_by_class_name('wp-block-preformatted')
        code = copy_pg.text
        
        time.sleep(2)

        driver.get("https://www.pbinfo.ro/")

        user_login_pb = driver.find_element_by_id('user')
        user_login_pb.send_keys(PBINFO_ACC)

        user_pass_pb = driver.find_element_by_id('parola')
        user_pass_pb.send_keys(PBINFO_PASS)

        button_pb = driver.find_elements_by_css_selector('button.btn.btn-primary')[1]
        button_pb.click()

        time.sleep(5)

        aur3l = f"https://www.pbinfo.ro/probleme/{problem_idx}"
        driver.get(aur3l)

        time.sleep(2)
        pyautogui.scroll(-1000000)

        time.sleep(1)

        paster = driver.find_element_by_css_selector('.CodeMirror-code div pre span span')

        coords = paster.location
        print(coords)

        pyautogui.click(button='right', x = 400, y = 600)

        time.sleep(0.1)
        pyautogui.press('escape')
        time.sleep(0.1)

        pyautogui.typewrite(code)

        button_pb_solve = driver.find_element_by_id('btn-submit')
        button_pb_solve.click()

        time.sleep(5)

        del v_list[idx]
        driver.quit()
    except Exception:
        print("404 NOT FOUND")
        del v_list[idx]
        driver.quit()
        continue