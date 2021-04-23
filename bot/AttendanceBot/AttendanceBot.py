import time
from datetime import datetime
from typing import List

from selenium import webdriver

from bot.Base.AttendanceBase import AttendanceBotBase
from bot.DataClass.School import School
from bot.DataClass.Student import Student
from bot.Utils.StudentAttendance import StudentAttendance


class AttendanceBot(AttendanceBotBase):
    def __init__(self, executable_path: str, school: School, students: List[Student]):
        super().__init__(executable_path, school)
        self.students = students

    def on_ready(self):
        print("Attendance bot ready to goooooooo!!!!!!!!")

    def take_attendance(self):
        for student in self.students:
            student_interface = StudentAttendance(self.driver, student, self.school)
            student_interface.complete_attendance()

    def time_check(self):
        now = datetime.now()
        if now.hour < self.school.end_time and now.hour > self.school.start_time:
            return True
        return False

    def start(self):
        print("Task Started!")
        while self.time_check():
            try:
                self.run()
                self.take_attendance()
                self.stop()
                print("Attendance taken for this period!")
                time.sleep(self.school.class_interval)
            except Exception:
                print("Failed to take attendance for this period.")
                time.sleep(100)
                print("Retrying....")
        print("Task Completed!")
