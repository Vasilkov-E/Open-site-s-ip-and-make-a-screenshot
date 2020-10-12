from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def screenshot_of_web_page(urls_all: list):
    '''
    :param urls_all:
    :return:
    '''
    try:
        for url in urls_all:
            try:
                driver = webdriver.Chrome(ChromeDriverManager().install())
                driver.get('https://' + url)
                driver.save_screenshot(f'screenshots\{url.replace("/", "_")}.png')
                driver.quit()
            except:
                pass
            else:
                pass
    except Exception as exception:
        print("скрин не вышел" + str(exception))


