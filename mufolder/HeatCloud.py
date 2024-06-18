import time
import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # для нажатия клаив клавиатуры
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # ожидания различных событий
from selenium.webdriver.support.ui import Select  # работа со списками
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains # lля сколддинга к нужному элементу импортируем класс ActionChains
from selenium.common.exceptions import NoSuchElementException
# import pytest
 # здесь  авторизация админа Котлы

class Admin_kotly(unittest.TestCase):

    def authorization(self, driver): # авторизация

        driver.get("https://heatcloud-admin.technaxis.com/external/login")


        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-0']" )))#
            email_field.send_keys("hcadmin@mail.ru")
        except TimeoutError:
            print("время ожидания поля емэйл вышло")

        try:
            password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-1']" )))
            password_field.send_keys("password")
        except TimeoutError:
            print("время ожидания поля пароль вышло")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                       "/html/body/app-root/portal-login/div/mat-card/mat-card-content/div[2]/div/div/app-spinner-button/button")))
        if button_voity.is_displayed():  # если кнпока видна , то
            button_voity.click()


    def fillter(self, driver):
        time.sleep(5)
        # со стаутсом  Гтовит воду
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@id='mat-tab-label-1-2']"))).click()
        time.sleep(3)

        # со статусом   Работает
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@id='mat-tab-label-1-0']"))).click()
        time.sleep(3)

        # со статусом   Ошибка
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@id='mat-tab-label-1-1']"))).click()
        time.sleep(3)

    def sort_order(self, driver):

        # нажатие На Все
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@id='mat-tab-label-1-3']"))).click()
        time.sleep(2)

        # упорядолчивнаие по ФИО
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Change sorting for name']"))).click()

        time.sleep(3)
        # упорядолчивнаие по телеофну
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH,"//button[@aria-label='Change sorting for phone']"))).click()

        time.sleep(3)
        # упорядолчивнаие по сер номер устройства
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Change sorting for serialnumber']"))).click()

        time.sleep(3)
        # упорядолчивнаие по статутсу котла
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//button[@aria-label='Change sorting for status']"))).click()

        time.sleep(3)
        # упорядолчивнаие по статутсу устройства
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//button[@aria-label='Change sorting for boiler']"))).click()


    def search(self, driver): # поиск

        time.sleep(2)
        # нажатие На Все
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@id='mat-tab-label-1-3']"))).click()

        time.sleep(2)
        search_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@type='search']")))

        search_field.click()
        search_field.send_keys("Вероника") # поси к по имени
        search_field.send_keys(Keys.ENTER) # нажатие на клавишу Enter

        time.sleep(3)



        search_field.clear() # очищаем поле  сперва потом вводим данные
        search_field.send_keys("+79278523641")
        search_field.send_keys(Keys.ENTER)  # нажатие на клавишу Enter

        time.sleep(3)
        search_field.clear()  # очищаем поле  сперва потом вводим данные
        search_field.send_keys("1234567-sd") # сер номер устройства
        search_field.send_keys(Keys.ENTER)  # нажатие на клавишу Enter




    def profile_device(self, driver):


        time.sleep(2)
        # нажатие На Все "//*[@id="mat-tab-content-5-3"]/div/div/mat-table/mat-row[26]/mat-cell[1]"
        elem_device = driver.find_element_by_xpath("//*[@id='mat-tab-content-2-3']/div/div/mat-table/mat-row[2]")
        elem_device.click()


        # try:
        #     if elem_device.is_displayed(): # если elem_device виден то
        #         elem_device.click()
        #     else:
        #         # скроллим к нужному элменту
        #         actions = ActionChains(driver)  # создаем объект клааса ActionChains
        #         actions.move_to_element(elem_device).perform()  # переходим к нужному элементу
        #         elem_device.click()
        #
        # except TimeoutError:
        #     print("время ожидания вышло")

        time.sleep(3)
        # Нажимаем кнопку Выйти:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                        "/html/body/app-root/portal-layout-classic/mat-sidenav-container/mat-sidenav-content/div/portal-top-horizontal-menu/mat-toolbar/mat-toolbar-row/button"))).click()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()

    def test_method_admin_authorization(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось

        self.fillter(driver)# вызов метода  фильтрации,котрый выше
        self.sort_order(driver) # вызов метода сртирвоаик по полям  , котрый выше
        self.search(driver)# вызов метода  поика ,котрый выше
       # self.profile_device(driver) # вызов метода профиля ,котрый выше


    def tear_down(self):
        time.sleep(5)
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()


