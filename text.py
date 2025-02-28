import flet as ft
from data_manager import DataManager
def salary_table_page(page: ft.Page, data_manager: DataManager):
    data_row = ft.DataRow(cells=[])

    def load_saved_data():
        num = len(data_manager.time_diffs)
        temp = 0
        while num > temp:
            cell_time_diffs = ft.DataCell(data_manager.time_diffs[temp])
            cell_work_days = ft.DataCell(data_manager.work_days[temp])
            cell_start_times = ft.DataCell(data_manager.start_times[temp])
            cell_end_times = ft.DataCell(data_manager.end_times[temp])

            data_row.cells.append(cell_time_diffs)
            data_row.cells.append(cell_work_days)
            data_row.cells.append(cell_start_times)
            data_row.cells.append(cell_end_times)

            data_table.rows.append(data_row)

            temp = temp + 1

            page.update()

    data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("日期")),
                ft.DataColumn(ft.Text("时间")),
                ft.DataColumn(ft.Text("时长")),
                ft.DataColumn(ft.Text("金额")),
            ],
            rows=[],
        )
    load_saved_data()

    return data_table
