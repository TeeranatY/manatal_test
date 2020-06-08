from bs4 import BeautifulSoup
from selenium import webdriver
import time
def get_follower(url="https://twitter.com/KMbappe") :
    # try:
    #init webdriver
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(options=options)
    time.sleep(1)
    driver.get(url)
    time.sleep(1)
    
    # page_source checking
    # file = open("output.txt","w",encoding="utf-8")
    # file.write(driver.page_source)
    # file.close()
    
    #scrape page_source using beautifulsoup
    bs = BeautifulSoup(driver.page_source,"lxml")
    get_tag = bs.find("a",href=lambda  href:href and "follower" in href)
    # print(get_tag)
    follower = get_tag.find_all("span")[1].string
    print(follower)
    driver.quit()
    # except :
    #     print("Something gone wrong")
    return follower

if __name__ == "__main__":
    inp = str(input("Please enter : ").strip())
    if "https://twitter.com/" not in inp :
        get_follower()
    else :
        get_follower(inp)
    