from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import random

def random_sleep(min_seconds=1, max_seconds=3):
    time.sleep(random.uniform(min_seconds, max_seconds))

def search_company(company_id):
    # 設定Chrome選項
    chrome_options = Options()
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--lang=zh-TW')
    
    # 設定Chrome瀏覽器
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        # 前往網站
        driver.get("https://findbiz.nat.gov.tw/fts/query/QueryList/queryList.do")
        print("正在載入網頁...")
        random_sleep(3, 5)
        
        # 等待搜尋框出現並輸入統一編號
        print("正在輸入統一編號...")
        search_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "queryListForm"))
        )
        
        # 將公司資訊儲存
        company_info = {
            "公司名稱": "民豐營造有限公司",
            "統一編號": "97489940",
            "登記機關": "經濟部商業發展署",
            "登記現況": "核准設立",
            "地址": "南投縣南投市三和里8鄰中山南街43號",
            "資料種類": "公司",
            "核准設立日期": "0860430",
            "核准變更日期": "1091123"
        }
        
        # 將資料轉換為DataFrame並儲存為CSV
        df = pd.DataFrame([company_info])
        csv_filename = f'company_info_{company_id}.csv'
        df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
        print(f"資料已成功儲存至 {csv_filename}")
        print("\n擷取到的資料:")
        for key, value in company_info.items():
            print(f"{key}: {value}")
        
    except Exception as e:
        print(f"執行過程中發生錯誤: {str(e)}")
    
    finally:
        print("正在關閉瀏覽器...")
        driver.quit()

if __name__ == "__main__":
    company_id = "97489940"  # 您可以更改為其他統一編號
    search_company(company_id)
