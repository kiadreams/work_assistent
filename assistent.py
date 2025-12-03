import os
from src.packages.worksheets.worksheet import WorkSheet, WorkSheetStyles, WorkSheetContent


if __name__ == '__main__':
    b_title = 'Пробная_ведомость_работ.xlsx'
    ws_first_title = 'Тестовая страница V05110______'
    if os.path.exists(b_title):
        os.remove(b_title)
    work_sheet = WorkSheet(b_title, ws_first_title)
    work_sheet.change_ws_title(WorkSheetStyles(), WorkSheetContent())
    work_sheet.save_work_sheet()
