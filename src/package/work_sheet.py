import os
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.styles import Font, Border, Side


class WorkSheet:

    def __init__(self, wb_title) -> None:
        self.wb_title = wb_title
        self.ws_first_title = 'Тестовая страница V05110______'
        self.wb = Workbook()

    def save_work_sheet(self):
        self.wb.save(self.wb_title)

    @staticmethod
    def change_ws_title(ws: WorkSheet, title: str) -> None:
        ws.title = title
        ws['b2'] = 'Пробуем внести текст в ячейку второго столбца'
        ws['b2'].font = Font(bold=True)
        mrg_cells = 'b2:f2'
        ws.merge_cells(mrg_cells)



    def frame_cells(self, range_cells) -> None:
        border = self.create_full_border()
        rows = self.wb.active[range_cells]
        for row in rows:
            for cell in row:
                cell.border = border

    @staticmethod
    def create_full_border() -> Border:
        medium_side = Side(style='medium')
        full_border = Border(
            top=medium_side,
            right=medium_side,
            bottom=medium_side,
            left=medium_side
        )
        return full_border


if __name__ == '__main__':
    wb_title = 'Пробная_ведомость_работ.xlsx'
    if os.path.exists(wb_title):
        os.remove(wb_title)
    work_sheet = WorkSheet(wb_title)
    work_sheet.change_ws_title(work_sheet.wb.active, work_sheet.ws_first_title)
    work_sheet.frame_cells('b2:f2')
    work_sheet.save_work_sheet()

