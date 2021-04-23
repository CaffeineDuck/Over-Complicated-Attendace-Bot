from dataclasses import dataclass


@dataclass
class School:
    start_time: int
    end_time: int
    class_interval: int
    school_site: str = "https://ingrails.com/school"
    username_xpath: str = "/html/body/section/div/section[1]/div/form/input[2]"
    password_xpath: str = "/html/body/section/div/section[1]/div/form/input[3]"
    login_button_xpath: str = "/html/body/section/div/section[1]/div/form/button"
    notification_cancel_button_xpath: str = "/html/body/div[7]/div/div/div[3]/button"
    online_class_xpath: str = '//*[@id="onlineClassMenu"]'
    join_button_xpath: str = (
        '//*[@id="right-side"]/section/div/div/div[1]/section/ul/li/span/a[1]'
    )
    profile_button_xpath: str = "/html/body/header/nav/div/ul/li/a"
    logout_button_xpath: str = "/html/body/header/nav/div/ul/li/ul/li/div/a"
