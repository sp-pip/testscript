# -*- coding: utf-8 -*-
from appium import webdriver
import time
import pytest
from PIL import Image
import os


class TestClass():
    @classmethod
    def setup_class(cls):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '127.0.0.1:62001',  # 连接到的设备名称，这个是夜神模拟器的名称
            'platformVersion': '4.4.2',  # Android版本
            'app': 'D:\\testscript\\zhongtai1030-1.apk',  # 连接到的设备名称，这个是夜神模拟器的名称
            'appPackage': 'com.ztsinhouse.optionsimulate',  # 包名
            'appActivity': 'com.qlot.common.app.SplashActivity',  # activity名称
            'noReset': True}  # 是否每次新装app,ture为不重装
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)
        cls.driver.find_element_by_xpath("//android.widget.RadioButton[contains(@index,'3')]").click()
        time.sleep(3)
        cls.driver.find_element_by_id("com.mszq.sjqqb:id/et_user").clear()
        cls.driver.find_element_by_id("com.mszq.sjqqb:id/et_user").send_keys(3001300)
        cls.driver.find_element_by_id("com.mszq.sjqqb:id/et_pwd").send_keys()

    @classmethod
    def setup_class(cls):
        cls.driver.quit()



    # def identifyingCode(self,driver, startx, starty, endx, endy):
    #     u'''获取验证码
    #     （startx，xstarty）---------------------------------
    #                       |     要截取的图片范围           |
    #                       |                                |
    #                       ---------------------------------- (endx,endy)
    #     '''
    #     driver.get_screenshot_as_file(os.getcwd() + '\\cirsschan.jpg')
    #     imGetScreen = Image.open(os.getcwd() + '\\cirsschan.jpg')
    #     box = (startx, starty, endx, endy)
    #     imIndentigy = imGetScreen.crop(box)
    #     imIndentigy.save(os.getcwd() + '\\indent.jpg')
    #     strCommand = 'tesseract.exe ' + os.getcwd() + '\\indent.jpg ' + os.getcwd() + '\\indet.txt'
    #     print
    #     strCommand
    #     os.system(strCommand)
    #
    #     rfindet = open(os.getcwd() + '\\indet.txt.txt', 'r')
    #     strIndet = rfindet.readline()
    #     return strIndet

    def test_buysucceed(self):
        self.driver.find_element_by_id("com.ztsinhouse.optionsimulate:id/tv_order").click()
        time.sleep(3)
        self.driver.find_element_by_name("50ETF购11月2300").click()
        time.sleep(3)
        self.driver.find_element_by_id("com.ztsinhouse.optionsimulate:id/ll_order1").click()


if __name__ == '__main__':
    pytest.main()





