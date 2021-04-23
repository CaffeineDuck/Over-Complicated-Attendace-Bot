from bot.Base.StudentBase import StudentBase

class Login(StudentBase):
    def send_username(self, username: str):
        self.driver.find_element_by_xpath(self.school.username_xpath).send_keys(
            username
        )

    def send_password(self, password: str):
        self.driver.find_element_by_xpath(self.school.password_xpath).send_keys(
            password
        )

    def click_login(self):
        self.driver.find_element_by_xpath(self.school.login_button_xpath).click()

    def login(self):
        student = self.student
        self.send_username(student.username)
        self.send_password(student.password)
        self.click_login()
