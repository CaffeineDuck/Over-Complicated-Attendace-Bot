import time

from bot.Base.StudentBase import StudentBase
from bot.Utils.attend import Attend
from bot.Utils.login import Login
from bot.Decorators.Time import wait


class StudentAttendance(StudentBase):
    @wait()
    def login(self):
        login_interface = Login(self.driver, self.student, self.school)
        login_interface.login()

    @wait()
    def attend(self):
        attend_interface = Attend(self.driver, self.student, self.school)
        attend_interface.attend()

    @wait()
    def logout(self):
        self.driver.find_element_by_xpath("/html/body/header/nav/div/ul/li/a").click()
        self.driver.find_element_by_xpath(
            "/html/body/header/nav/div/ul/li/ul/li/div/a"
        ).click()

    def complete_attendance(self):
        self.login()
        self.attend()
        self.logout()
