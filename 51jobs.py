# coding = utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get('https://www.51job.com')
ele = driver.find_element_by_id("kwdselectid")
ele.send_keys('python')
ele = driver.find_element_by_id('work_position_input')
ele.click()

time.sleep(2)
driver.find_element_by_id('work_position_click_ip_location_000000_020000').click()
time.sleep(2)

# for ele in eles:
    # ele.click()

driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()

driver.find_element_by_id('work_position_click_bottom_save').click()
