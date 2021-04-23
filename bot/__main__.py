from selenium import webdriver

from bot import AttendanceBot, School, Student
from config.bot import bot_config
from config.class_conf import class_config
from config.school import school_config

students = [Student(school_config.username, school_config.password)]

school = School(
    start_time=class_config.start,
    end_time=class_config.end,
    class_interval=class_config.interval,
)

main_bot = AttendanceBot(
    executable_path=bot_config.chromedriver,
    students=students,
    school=school,
)

if __name__ == "__main__":
    main_bot.start()
