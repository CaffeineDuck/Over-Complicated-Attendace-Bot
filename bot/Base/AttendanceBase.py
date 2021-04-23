from bot.DataClass.School import School
from selenium import webdriver


class AttendanceBotBase:
    def __init__(self, executable_path: str, school: School):
        self.executable_path = executable_path
        self.school = school

    def goto_site(self):
        self.driver = webdriver.Chrome(executable_path=self.executable_path)
        self.driver.get(self.school.school_site)

    def on_ready(self):
        pass

    def startup(self):
        pass

    def run(self):
        self.goto_site()
        self.on_ready()
        self.startup()

    def stop(self):
        self.driver.close()
