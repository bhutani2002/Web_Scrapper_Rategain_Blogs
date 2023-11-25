from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
from openpyxl import Workbook
from selenium.common.exceptions import NoSuchElementException

url = "https://rategain.com/blog/"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(url)
driver.maximize_window()

blog_title_locator = '//*[@class="content"]/h6'

blog_date_locator = '//div[@class="bd-item"][1]/span'

blog_like_locator = '//*[@class="zilla-likes"]/span'

blog_image_locator = '//a[@class="rocket-lazyload entered lazyloaded"]'

next_button_locator = '//a[@class="next page-numbers"]'

blog_list = []
max_iterations = 3
pagination_element = driver.find_element(By.XPATH, '//*[@class="pagination col-xs-12"]')
last_page_of_blogs = pagination_element.find_element(By.XPATH, './/a[last()-1]')
start = time.time()
print(start)
for i in range(int(last_page_of_blogs.text)):
    iteration = 0
    if(i == 0):
        val = 2
    else:
        val = 1
    while iteration < max_iterations:
        # Scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(val)
        # Scroll up
        driver.execute_script(f"window.scrollTo(0, 0);")
        time.sleep(val)
        iteration += 1
    driver.implicitly_wait(5)
    blog_title = driver.find_elements(By.XPATH, blog_title_locator)
    blog_date = driver.find_elements(By.XPATH, blog_date_locator)
    blog_like = driver.find_elements(By.XPATH, blog_like_locator)
    blog_image_url = driver.find_elements(By.XPATH, blog_image_locator)
    Range = max(len(blog_title), len(blog_date), len(blog_like), len(blog_image_url))
    for i in range(Range):
        single_blog_title = blog_title[i].text if i < len(blog_title) else "No title defined"
        single_blog_date = blog_date[i].text if i < len(blog_date) else "No date defined"
        single_blog_like = blog_like[i].text if i < len(blog_like) else "No likes defined"
        single_blog_image_url = blog_image_url[i].get_attribute("data-bg") if i < len(blog_image_url) else "No image defined"
        blog_item = {
            "Blog_Title": single_blog_title,
            "Blog_Date": single_blog_date,
            "Blog_Like": single_blog_like,
            "Blog_Image_Url": single_blog_image_url
        }
        blog_list.append(blog_item)
    try:
        next_button = driver.find_element(By.XPATH, next_button_locator)
    except NoSuchElementException:
        break

    driver.execute_script("arguments[0].click();", next_button)

end = time.time()
print(end - start)

# Store Data in Excel File
book = Workbook()
sheet = book.create_sheet("Blogs_Data", 0)

headers = ["Blog_Title", "Blog_Date", "Blog_Like", "Blog_Image_Url"]
sheet.append(headers)
for blog in blog_list:
    blog_like = int(blog.get("Blog_Like", 0))
    row_data = [blog.get("Blog_Title", ""),
                blog.get("Blog_Date", ""),
                blog_like,
                blog.get("Blog_Image_Url", "")]

    sheet.append(row_data)
book.save("Blogs_Data.xlsx")


# Store Data in Csv File
# df = pd.DataFrame(blog_list)
# df.to_csv('All_Blog_Details.csv', index=False)

driver.quit()