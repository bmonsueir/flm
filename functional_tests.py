from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://flm-bmonsueir.c9users.io/')

assert "Formulator's Lab" in browser.title