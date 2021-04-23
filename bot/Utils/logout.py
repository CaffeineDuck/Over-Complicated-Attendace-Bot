import time

from bot.Base.StudentBase import StudentBase

class Logout(StudentBase):
    def logout(self):
        self.driver.find_element_by_xpath(self.school.profile_button_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.school.logout_button_xpath).click()