from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://qna.habr.com/234234/'


def screenshot_of_web_page(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    print(url[8:-1])
    driver.save_screenshot(f'screenshots\{url[8:].replace("/","_")}.png')
    driver.quit()


screenshot_of_web_page(url)
