import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def chromedriver(url,download_path="./data/"):
    """
    It is not the best way to crawler the data due to the chromedriver should update to the same version with
    the Chrome. However, it is the direct and simple way to search the website and do some request on the browser.
    inputs:
        url:string.the website url.
    return: 
        None. Download the .zip to the download_path.
    """
    # basic selenium setting
    chromedriver_path = "./chromedriver.exe"

    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': download_path}
    options.add_experimental_option('prefs', prefs)

    chrome = webdriver.Chrome(chromedriver_path, chrome_options=options)
    # open the browser and connect to the website
    chrome.get(url)
    # Searching the "非本期下載" and click the button
    download = chrome.find_elemet_by_id("ui-id-2")
    download.click()
    # click the posted date selection and choose "108season2"
    date_select = Select(chrome.find_element_by_id("historySeason_id"))
    date_select.select_by_value("108S2")
    # Download format -> CSV
    download_select = Select(chrome.find_element_by_id("fileFormatId"))
    download_select.select_by_value("csv")
    # Download type -> 2, and  select 臺北市/新北市/桃園市/臺中市/高雄市的【不動產買賣】資料
    chrome.find_element_by_id("downloadTypeId2").click()
    chrome.find_element_by_xpath("//input[@value='A_lvr_land_A']").click() # Taipei
    chrome.find_element_by_xpath("//input[@value='F_lvr_land_A']").click() # New Taipei
    chrome.find_element_by_xpath("//input[@value='H_lvr_land_A']").click() # Taoyuan
    chrome.find_element_by_xpath("//input[@value='B_lvr_land_A']").click() # Taichung
    chrome.find_element_by_xpath("//input[@value='E_lvr_land_A']").click() # Kaohsiung
    # Click the download button
    chrome.find_element_by_id("downloadBtnId").click()
    
def request_download(url,download_path="./data/"):
   """
    Use GET to download the csv file.
    Inputs:
        url:string. The website url.
        download_path:string. The address to download the files.
    Return:
        None. Download the csv files to data folder.
   """
   counties = ['A','F','H','B','E'] #臺北市/新北市/桃園市/臺中市/高雄市
    for county in counties:
        get_url = url + "/DownloadSeason?season=108S2&fileName={c}_lvr_land_A.csv".format(c=county)
        try:
            download = requests.get(get_url)
            open(download_path+"{c}_lvr_land_A.csv".format(c=county),"wb").write(download.content)
            print("Download File {csv}_lvr_land_A.csv".format(csv=county))
        except:
            print("Download Failed. The url:{url} do not exist.".format(url=get_url))


if __name__ == '__main__':
    request_download("https://plvr.land.moi.gov.tw/")

