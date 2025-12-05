from enum import StrEnum


class TypeOfWork(StrEnum):
    SETTING_UP = 'наладка'
    FIRST_CONTROL = 'первый профилактический контроль'
    RESTORATION = 'восстановление'
    CONTROL = 'профилактический контроль'
    TESTING = 'опробование'


class EmployeePosition(StrEnum):
    ENGINEER = 'инженер'
    ENGINEER_2_CATEGORY = 'инженер 2-ой категории'
    ENGINEER_1_CATEGORY = 'инженер 1-ой категории'
    LEAD_ENGINEER = 'ведущий инженер'