from PIL import Image
import os
import glob
from selenium import webdriver


directory = '/Users/macbookderai/Desktop/Programación/Python/Programas/bingo fran/'
file_list = [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
file_list = glob.glob("*.html")
file_list.remove('plantilla.html')

# I have my files list

counter = 1
for html_file in file_list:
    path = f'file://{os.path.abspath(html_file)}'
    driver = webdriver.Safari()
    driver.get(path)
    width = driver.execute_script("return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);")
    height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
    screenshot = driver.get_screenshot_as_png()
    driver.quit()
    image = Image.open(screenshot)
    image = image.crop((0, 0, width, height))

    image.save(f'carton_{counter}.jpg', 'JPEG')
    counter += 1