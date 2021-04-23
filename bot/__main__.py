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
    school_site="https://ingrails.com/school",
    username_xpath="/html/body/section/div/section[1]/div/form/input[2]",
    password_xpath="/html/body/section/div/section[1]/div/form/input[3]",
    login_button_xpath="/html/body/section/div/section[1]/div/form/button",
    notification_cancel_button_xpath="/html/body/div[7]/div/div/div[3]/button",
    online_class_xpath='//*[@id="onlineClassMenu"]',
    join_button_xpath='//*[@id="right-side"]/section/div/div/div[1]/section/ul/li/span/a[1]',
    profile_button_xpath="/html/body/header/nav/div/ul/li/a",
    logout_button_xpath="/html/body/header/nav/div/ul/li/ul/li/div/a",
)

main_bot = AttendanceBot(
    executable_path=bot_config.chromedriver,
    students=students,
    school=school,
)

if __name__ == "__main__":
    main_bot.start()
