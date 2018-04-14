from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_counter():
    browser = webdriver.Chrome()
    browser.get('http://192.168.0.129')
    # 计数
    # 跳转到“计数器”页面
    browser.switch_to.frame(0)
    # 跳转：click“设备信息”
    tab_machine_msg = browser.find_element(by=By.CSS_SELECTOR, value="span.P001_menu_main_caption")
    tab_machine_msg.click()
    # 跳转；click"计数器"
    btn_counter = browser.find_element(by=By.ID, value="s81")
    btn_counter.click()
    # 计数：“按功能打印的页面”
    time.sleep(5)  # 需要优化处理方式，不能用时间来避免页面未返回的条件
    browser.switch_to.frame('deviceconfig')
    index04 = browser.page_source
    f = open('c://temp/index_device_function.html', 'w+', encoding='UTF-8')
    f.write(index04)
    f.close


    # 计数：“按纸张尺寸打印的页面”
    sel = browser.find_element(by=By.ID, value="addrType")
    all_options = sel.find_elements_by_tag_name("option")
    for option in all_options:
        if '2' == option.get_attribute("value"):
            option.click()
            time.sleep(5)
            index05 = browser.page_source
            f = open('c://temp/index_device_size.html', 'w+', encoding='UTF-8')
            f.write(index05)
            f.close
            break
    # 退出Chrome
    browser.quit()


def get_status():
    browser = webdriver.Chrome()
    browser.get('http://192.168.0.129')
    # 首页
    # 设备状态
    browser.switch_to.frame(0)
    browser.switch_to.frame("device")
    index01 = browser.page_source
    f = open('c://temp/index_machine_status.html', 'w+', encoding='UTF-8')
    f.write(index01)
    f.close
    # 纸张
    browser.switch_to.parent_frame()
    browser.switch_to.frame('paper')
    index02 = browser.page_source
    f = open('c://temp/index_paper.html', 'w+', encoding='UTF-8')
    f.write(index02)
    f.close
    # 墨粉
    browser.switch_to.parent_frame()
    browser.switch_to.frame('toner')
    index03 = browser.page_source
    f = open('c://temp/index_ink.html', 'w+', encoding='UTF-8')
    f.write(index03)
    f.close
    # 关闭Chrome
    browser.quit()


if __name__ == '__main__':
   get_counter()
   get_status()

