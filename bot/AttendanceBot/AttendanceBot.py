from typing import List
import time

from bot.Base.AttendanceBase import AttendanceBotBase
from bot.DataClass.School import School
from bot.DataClass.Student import Student
from selenium import webdriver
from bot.Utils.StudentAttendance import StudentAttendance


class AttendanceBot(AttendanceBotBase):
    def __init__(self, executable_path: str,  school: School, students: List[Student]):
        super().__init__(executable_path, school)
        self.students = students
    
    def on_ready(self):
        print('Attendance bot ready to goooooooo!!!!!!!!')

    def take_attendance(self):
        for student in self.students:
            student_interface = StudentAttendance(self.driver, student, self.school)
            student_interface.complete_attendance()

    def start(self):
        self.run()
        self.take_attendance()
        print('Task Completed!')