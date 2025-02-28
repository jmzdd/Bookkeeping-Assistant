import flet as ft
from data_manager import DataManager

def salary_table_page(page: ft.Page, data_manager: DataManager):
    def load_saved_data():
        data_rows = []
        num = len(data_manager.time_diffs)
        for temp in range(num):
            cell_time_diffs = ft.DataCell(ft.Text(data_manager.time_diffs[temp]))
            cell_work_days = ft.DataCell(ft.Text(data_manager.work_days[temp]))
            cell_start_times = ft.DataCell(ft.Text(data_manager.start_times[temp]))
            cell_end_times = ft.DataCell(ft.Text(data_manager.end_times[temp]))

            data_row = ft.DataRow(cells=[
                cell_time_diffs,
                cell_work_days,
                cell_start_times,
                cell_end_times
            ])
            data_rows.append(data_row)

        data_table.rows.extend(data_rows)

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
    page.update()

    return data_table
