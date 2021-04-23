import time

from bot.Base.StudentBase import StudentBase
from bot.Decorators.Time import wait
from selenium import webdriver


class Attend(StudentBase):
    @wait()
    def goto_online_class_page(self):
        self.driver.find_element_by_xpath(self.school.online_class_xpath).click()

    @wait()
    def join_online_class(self):
        self.driver.find_element_by_xpath(self.school.join_button_xpath).click()

    @wait()
    def close_notification(self):
        self.driver.find_element_by_xpath(
            self.school.notification_cancel_button_xpath
        ).click()

    @wait()
    def close_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def attend(self):
        self.close_notification()
        self.goto_online_class_page()
        self.join_online_class()
        self.close_new_tab()
