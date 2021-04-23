from dataclasses import dataclass

from .School import School


@dataclass
class Student:
    # school: School
    username: str
    password: str
