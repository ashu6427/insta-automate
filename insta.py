import click as click
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# First opening chrome browser and then to instagram login page
browser = webdriver.Chrome(executable_path='chromedriver.exe')
browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

# here we are sending username and password and login to your account
sleep(1)
input_name = browser.find_element_by_name('username')
input_name.send_keys('ashutoshbagal6427@gmail.com')
sleep(1)
input_password = browser.find_element_by_name('password')
input_password.send_keys('Ashu@302001')
sleep(1)
submit = browser.find_element_by_tag_name('form')
submit.submit()
sleep(3)

# clicking not now button and turning off notifications
not_now = browser.find_element_by_xpath("/html/body/div[1]/div/div/section/main/div/div/div/div/button")
not_now.click()
sleep(2)
notify_off = browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
notify_off.click()
sleep(2)

# Here we are moving to #puppy page for performing operation
puppy_page = browser.find_element_by_xpath("/html/body/div[1]/div/div/section/nav/div[2]/div/div/div[2]/input")
puppy_page.send_keys("#puppy")
sleep(2)
puppy_page.send_keys(Keys.ENTER)
sleep(3)
puppy_page.send_keys(Keys.ENTER)
sleep(2)


# this function is made for image click event and then liking,commenting and closing the image
def photo_likings(path):
    sleep(3)
    image = browser.find_element_by_xpath(path)
    image.click()
    sleep(2)
    like_img = browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[1]/button")
    like_img.click()
    comment_button = browser.find_element_by_xpath(
        "/html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[2]/button")
    comment_button.click()
    sleep(3)
    comment_img = browser.find_element_by_xpath(
        "/html/body/div[6]/div[2]/div/article/div[3]/section[3]/div/form/textarea")
    comment_img.send_keys("Very nice picture!!")
    sleep(1)
    comment_img.send_keys(Keys.ENTER)
    sleep(2)
    close_img = browser.find_element_by_xpath("/html/body/div[6]/div[3]/button")
    close_img.click()


# Here we have given paths for various images (if you want you can change as per your preference)
# paths for first photo like and comment
path1 = "/html/body/div[1]/div/div/section/main/article/div[1]/div/div/div[1]/div[1]/a"
# path for second photo like and comment
path2 = "/html/body/div[1]/div/div/section/main/article/div[1]/div/div/div[1]/div[2]/a"
# path for third photo like and comment
path3 = "/html/body/div[1]/div/div/section/main/article/div[1]/div/div/div[1]/div[3]/a"

photo_likings(path1)
sleep(1)
photo_likings(path2)
sleep(1)
photo_likings(path3)

# perform the log out operation
click_logo = browser.find_element_by_xpath(
    "/html/body/div[1]/div/div/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img")
click_logo.click()
sleep(1)
log_out = browser.find_element_by_xpath(
    "/html/body/div[1]/div/div/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div")
log_out.click()

# exiting the browser
browser.quit()
