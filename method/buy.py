import time

from selenium.webdriver.common.by import By

from utils.depend import chrome

'''
抢购操作核心函数
'''


def buy(cnt):
    # 当重复次数用尽，则自动退出
    if cnt < 0:
        print('抢购失败')
        chrome.close()
        exit(0)
    chrome.get("https://cart.jd.com/cart_index")  # 进入购物车页面
    while True:
        time.sleep(0.01)
        try:
            # 购物车商品列表全选按钮定位
            checkAllBtn = chrome.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[3]/div[1]/div/input")
            break
        except:
            continue
    # 判断购物车商品列表全选按钮是否被选中
    is_selected = checkAllBtn.is_selected()
    if not is_selected:
        checkAllBtn.click()
    while True:
        time.sleep(0.01)
        try:
            # 开始进行结算
            chrome.find_element(By.LINK_TEXT, '去结算').click()  # 进入结算页面
            # 提交订单
            chrome.find_element(By.XPATH,
                                '/html/body/div[15]/div/div[11]/div[8]/div/div[2]/div[1]/button[1]').click()  # 点击提交订单
            break
        except:
            continue
    # 判断是否提交成功
    info = "提交成功"
    if info in chrome.page_source:
        print("购买成功")
        exit()
    else:
        cnt -= 1
        print("抢购失败，正在重试！")
        buy(cnt)
