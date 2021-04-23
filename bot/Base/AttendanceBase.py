from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from bot.DataClass.School import School


class AttendanceBotBase:
    def __init__(self, executable_path: str, school: School):
        self.executable_path = executable_path
        self.school = school

    def initiate_webdriver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=self.executable_path, chrome_options=chrome_options)

    def goto_site(self):
        self.driver.get(self.school.school_site)

    def on_ready(self):
        pass

    def startup(self):
        pass

    def run(self):
        self.initiate_webdriver()
        self.goto_site()
        self.on_ready()
        self.startup()

    def stop(self):
        self.driver.close()
