# 导入必要的第三方库
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 初始化Metamask
def init_metamask(Phrase,Password):
    print("等待页面加载……")
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH,'//button[text()="开始使用"]').click()
    driver.find_element(By.XPATH,'//button[text()="不，谢谢"]').click()
    driver.find_element(By.XPATH,'//button[text()="导入钱包"]').click()

    driver.find_element(By.XPATH,'//*[@id="import-srp__srp-word-0"]').send_keys(Phrase)
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(Password)
    driver.find_element(By.XPATH,'//*[@id="confirm-password"]').send_keys(Password)
    driver.find_element(By.XPATH,'//*[@id="create-new-vault__terms-checkbox"]').click()
    driver.find_element(By.XPATH,'//button[text()="导入"]').click()

    print("等待导入完成……")
    time.sleep(5)
    driver.find_element(By.XPATH,'//button[text()="全部完成"]').click()
    
# 添加 PlatON 网络
def add_platon_network(name,rpc,chainId,sign,scan):
    print("添加PlatON网络……")
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[1]/div/div[2]/div/div/span').click()
    driver.find_element(By.XPATH,'//button[text()="添加网络"]').click()
    driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[3]/a/h6').click()

    # 输入参数
    inputs = driver.find_elements(By.XPATH,'//input')
    inputs[1].send_keys(name)
    inputs[2].send_keys(rpc)
    inputs[3].send_keys(chainId)
    inputs[4].send_keys(sign)
    inputs[5].send_keys(scan)

    print("输入完毕，等待页面加载……")
    time.sleep(5)
    driver.find_element(By.XPATH,'//button[text()="保存"]').click()

# 钱包连接
def connect_to_website():
    driver.find_element(By.XPATH,'//div[text()="Connect to wallet"]').click()
    print("等待页面响应")
    time.sleep(1)
    driver.find_element(By.XPATH,'//span[text()="MetaMask"]').click()
    print("等待页面响应")
    time.sleep(1)
    driver.execute_script("window.open('')")
    # 这个地方的 window_handles[] 要根据你们的具体情况来判断
    driver.switch_to.window(driver.window_handles[2])
    driver.get('chrome-extension://{}/popup.html'.format(extension_id))
    print("等待页面响应")
    time.sleep(1)
    print("等待点击‘下一步’")
    time.sleep(1)
    driver.find_element(By.XPATH,'//button[text()="下一步"]').click()
    print("等待点击‘连接’")
    time.sleep(1)
    driver.find_element(By.XPATH,'//button[text()="连接"]').click()
    print("等待点击‘签名’")
    time.sleep(1)
    driver.find_element(By.XPATH,'//button[text()="签名"]').click()
    print("popup页面关闭")
    driver.close()

def ok_metamask():
    driver.execute_script("window.open('')")
    driver.switch_to.window(driver.window_handles[2])
    driver.get('chrome-extension://{}/popup.html'.format(extension_id))
    print("等待钱包页面加载")
    time.sleep(3)
    driver.find_element(By.XPATH,'//button[text()="确认"]').click()
    time.sleep(3)
    print("popup页面关闭")
    driver.close()
