from dataclasses import dataclass


@dataclass
class School:
    school_site: str
    username_xpath: str
    password_xpath: str
    login_button_xpath: str
    notification_cancel_button_xpath: str()
    online_class_xpath: str
    join_button_xpath: str
    profile_button_xpath: str
    logout_button_xpath: str
