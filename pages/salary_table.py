import flet as ft
from data_manager import DataManager
def salary_table_page(page: ft.Page):
    # 加载所有已经保存的数据
    data_manager = DataManager()

    def load_saved_data():
        for num in data_manager.time_diffs:
            day_control = ft.DataColumn(ft.Text("日期"))
            data_row.cells.append(day_control)

    data_row = ft.DataRow(cells=[])

    data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("日期")),
                ft.DataColumn(ft.Text("时间")),
                ft.DataColumn(ft.Text("时长")),
                ft.DataColumn(ft.Text("金额")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                    ],
                ),
            ],
        )
    page.update()
    return data_table
