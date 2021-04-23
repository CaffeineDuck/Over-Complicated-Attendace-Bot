from dataclasses import dataclass


@dataclass
class School:
    start_time: int
    end_time: int
    class_interval: int
    school_site: str
    username_xpath: str
    password_xpath: str
    login_button_xpath: str
    notification_cancel_button_xpath: str()
    online_class_xpath: str
    join_button_xpath: str
    profile_button_xpath: str
    logout_button_xpath: str
