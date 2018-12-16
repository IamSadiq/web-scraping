# import selenium
from selenium import webdriver

browser = webdriver.chrome()
browser.get('instagram.com/abberfeeds')

# follow_button = browser.find_element_by_class_name('_follow')
follow_button = browser.find_element_by_css_selector('button')
follow_button.click()