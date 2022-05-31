#!/usr/bin/env python3

# Copyright (c) 2022 Emilie Beske Unna-Lindhard & Nils Müllenborn - The code is free to use for anybody, but please reference our project when doing so.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.headless = True

i = 1


def spike():
    # open both files
    with open('runtime-2.log','r') as firstfile, open('out.txt','w') as secondfile:
        # read content from first file
        for line in firstfile:
             # write content to second file
             secondfile.write(line)


def selenium_script_1():
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(30)

    driver.get("http://10.20.82.158/")
    driver.find_element(By.CSS_SELECTOR,
                        "#menu-1-583d012d > li.menu-item.menu-item-type-post_type.menu-item-object-page.menu-item-52 > a").click()
    # blog overview

    driver.find_element(By.XPATH,
                        "//*[@id='content']/div/div/section[2]/div/div/div/div[2]/div/div/article[1]/div/h3/a").click()
    # post 5
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

    # scroll down

    driver.back()
    # back to previous page

    driver.find_element(By.XPATH,
                        "/html/body/div/div[2]/div/div/section[2]/div/div/div/div[2]/div/div/article[5]/div/h3/a").click()
    # blogpost 3

    driver.back()
    # back to previous page

    driver.find_element(By.XPATH,
                        "/html/body/div/div[2]/div/div/section[2]/div/div/div/div[2]/div/div/article[4]/div/h3/a").click()
    # post 1

    driver.find_element(By.XPATH,
                        "/html/body/div/div[2]/div/div/main/div/section[2]/div/div/div/div[1]/div/p[7]/a").click()
    # link in bottom of post 1 to contact page

    driver.find_element(By.CSS_SELECTOR,
                        "#menu-1-583d012d > li.menu-item.menu-item-type-post_type.menu-item-object-page.menu-item-542 > a").click()
    # gallery
    driver.find_element(By.CSS_SELECTOR, "#gallery-1 > figure:nth-child(1) > div > a > img").click()
    time.sleep(2)
    # click first picture in gallery

    # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.RIGHT)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[2]").send_keys(Keys.RIGHT)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[2]").send_keys(Keys.RIGHT)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[2]").send_keys(Keys.RIGHT)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[2]").send_keys(Keys.RIGHT)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[2]").send_keys(Keys.RIGHT)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[2]").send_keys(Keys.RIGHT)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]").click()
    # exit gallery image view

    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/nav[1]/ul/li[4]/a").click()
    # news

    driver.find_element(By.XPATH,
                        "/html/body/div/div[2]/div/div/main/article/div/div/section/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/h3").click()
    # news article no. 1

    driver.quit()


def selenium_script_2():
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(30)

    driver.get("http://10.20.82.158/")

    driver.find_element(By.CSS_SELECTOR, "#menu-item-52").click()
    # blog overview

    driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/main/div/article[1]/div/div/header/h2/a").click()
    # post 5

    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    # scroll down
    driver.back()
    # back to previous page

    driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/main/div/article[5]/div/div/header/h2/a").click()
    # blogpost 3
    driver.back()
    # back to previous page

    driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/main/div/article[4]/div/div/header/h2/a").click()
    # post 1

    driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/main/article/div/div/p[7]/a").click()
    # link in bottom of post 1 to contact page

    driver.find_element(By.CSS_SELECTOR, "#menu-item-542 > a").click()
    # gallery
    driver.find_element(By.CSS_SELECTOR, "#post-518 > div > figure:nth-child(2) > a > img").click()
    # click first picture in gallery
    time.sleep(2)
    driver.back()

    driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/article/div/figure[2]/a/img").click()
    time.sleep(2)
    driver.back()

    driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/article/div/figure[3]/a/img").click()
    time.sleep(2)
    driver.back()

    driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/article/div/figure[4]/a/img").click()
    time.sleep(2)
    driver.back()

    driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/article/div/figure[5]/a/img").click()
    time.sleep(2)
    driver.back()

    driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/article/div/figure[6]/a/img").click()
    time.sleep(2)
    driver.back()

    driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/article/div/figure[7]/a/img").click()
    time.sleep(2)
    driver.back()

    driver.find_element(By.XPATH, "/html/body/div/header/div/div/div/div/div[3]/div/nav/div/ul/li[4]/a").click()
    # news

    driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/article/div/p[1]/a").click()

    # news article 1
    driver.quit()


def selenium_script_3():
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(30)

    driver.get("http://10.20.82.158/")

    driver.find_element(By.CSS_SELECTOR, "#menu-item-52").click()
    # blog overview

    driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/main/div/article[1]/div/div/header/h2/a").click()
    # post 5

    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    # scroll down
    driver.back()
    # back to previous page

    driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/main/div/article[5]/div/div/header/h2/a").click()
    # blogpost 3
    driver.back()
    # back to previous page

    driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/main/div/article[4]/div/div/header/h2/a").click()
    # post 1

    driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/main/article/div/div/p[7]/a").click()
    # link in bottom of post 1 to contact page

    driver.find_element(By.CSS_SELECTOR, "#menu-item-542 > a").click()
    # gallery
    driver.find_element(By.CSS_SELECTOR, "#post-518 > div > figure:nth-child(2) > a > picture > img").click()
    # click first picture in gallery
    time.sleep(2)
    driver.back()

    driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/article/div/figure[2]/a/picture/img").click()
    time.sleep(2)
    driver.back()

    driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/article/div/figure[3]/a/picture/img").click()
    time.sleep(2)
    driver.back()

    driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/article/div/figure[4]/a/picture/img").click()
    time.sleep(2)
    driver.back()

    driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/article/div/figure[5]/a/picture/img").click()
    time.sleep(2)
    driver.back()

    driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/article/div/figure[6]/a/picture/img").click()
    time.sleep(2)
    driver.back()

    driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/article/div/figure[7]/a/picture/img").click()
    time.sleep(2)
    driver.back()

    driver.find_element(By.XPATH, "/html/body/div/header/div/div/div/div/div[3]/div/nav/div/ul/li[4]/a").click()
    # news

    driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/article/div/p[1]/a").click()
    # new article 1
    driver.quit()

d = datetime.now()
print("Experiment started:", d)
time.sleep(300)

while i <= 10:
    time.sleep(120)
    spike()
    d = datetime.now()
    print("script and time started at: ", d)
    time.sleep(20)
    start = time.time()

    # selenium_script_1()
    # selenium_script_2()
    selenium_script_3()


    end = time.time()
    print("script", i, "run - time taken:", end - start)
    i += 1

time.sleep(300)
print("Experiment done")
