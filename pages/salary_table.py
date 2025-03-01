import flet as ft
from data_manager import DataManager

def salary_table_page(page: ft.Page, data_manager: DataManager):
    # 存放每次新建的数据表组件
    data_rows = []

    def load_saved_data():
        # 清空计算出的日薪列表
        data_manager.hourly_rate_list.clear()

        for temp in range(len(data_manager.work_days)):
            cell_work_days = ft.DataCell(ft.Text(data_manager.work_days[temp]))
            cell_times = ft.DataCell(ft.Text(f"{data_manager.start_times[temp]}至{data_manager.end_times[temp]}"))
            cell_time_diffs = ft.DataCell(ft.Text(f"共{data_manager.time_diffs[temp]}小时"))
            cell_money = ft.DataCell(ft.Text(f"{float(data_manager.time_diffs[temp])*float(data_manager.get_hourly_rate())}元"))

            # 将计算出的日薪全部存在列表中
            data_manager.hourly_rate_list.append(float(data_manager.time_diffs[temp])*float(data_manager.get_hourly_rate()))

            data_row = ft.DataRow(cells=[
                cell_work_days,
                cell_times,
                cell_time_diffs,
                cell_money
            ])

            data_rows.append(data_row)
        data_table.rows.extend(data_rows)

    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("日期")),
            ft.DataColumn(ft.Text("时间")),
            ft.DataColumn(ft.Text("时长")),
            ft.DataColumn(ft.Text("日薪")),
        ],
        rows=[],
    )

    load_saved_data()

    page_info = ft.Column(controls=[
        ft.Text(f"{data_manager.get_name()}的薪资记录表"),
        ft.Text(f"共{len(data_manager.work_days)}条记录，🪙总计{sum(data_manager.hourly_rate_list)}元"),
        data_table
    ])


    page.update()

    return page_info
