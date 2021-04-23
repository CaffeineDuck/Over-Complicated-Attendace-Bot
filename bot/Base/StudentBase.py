from bot.DataClass.School import School
from bot.DataClass.Student import Student
from selenium import webdriver


class StudentBase:
    def __init__(self, driver: webdriver.Chrome, student: Student, school: School):
        self.driver = driver
        self.student = student
        self.school = school
