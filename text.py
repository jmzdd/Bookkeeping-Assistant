import flet as ft
from data_manager import DataManager
from datetime import datetime
def data_edit_page(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    data_manager= DataManager()

    def select_day(e):
        data_manager.set_work_day(e.control.value.strftime('%Y-%m-%d'))
        # page.add(ft.Text(data_manager.get_work_day()))
    def select_begin_time(e):
        data_manager.set_begin_time(begin_time_picker.value)
        page.add(ft.Text(data_manager.get_begin_time()))

    def select_end_time(e):
        data_manager.set_end_time(end_time_picker.value)
        page.add(ft.Text(data_manager.get_end_time()))

    def add_data(e):
        start_time = data_manager.get_begin_time()
        end_time = data_manager.get_end_time()

        # 假设今天是基准日期
        today = datetime.today()
        start_datetime = datetime.combine(today, start_time)
        end_datetime = datetime.combine(today, end_time)

        time_diff = end_datetime - start_datetime

        page.add(ft.Text(f"Time difference: {time_diff}"))

        # 创建新的控件
        new_control = ft.Text(f"Time difference: {time_diff}")

        # 将新控件添加到 column 的 controls 列表中
        column.controls.append(new_control)

        # 更新页面以显示新控件
        page.update()

    end_time_picker = ft.TimePicker(
        confirm_text="确认",
        cancel_text="取消",
        error_invalid_text="时间超出范围",
        help_text="请选择时间",
        hour_label_text="小时",
        minute_label_text="分钟",
        on_change=select_end_time,
    )

    begin_time_picker = ft.TimePicker(
        confirm_text="确认",
        cancel_text="取消",
        error_invalid_text="时间超出范围",
        help_text="请选择时间",
        hour_label_text="小时",
        minute_label_text="分钟",
        on_change=select_begin_time,
    )
    # 使用 Column 布局将多个组件垂直排列
    column = ft.Column(
        controls=[
            ft.ExpansionPanelList(
                elevation=5,
                controls=[
                    ft.ExpansionPanel(
                        header=ft.ListTile(title=ft.Text("数据设置",weight=ft.FontWeight.NORMAL, font_family="MiSans")),
                        expanded=True,
                        content=ft.Column([
                            ft.ListTile(
                                leading=ft.Icon(ft.Icons.EMOJI_PEOPLE),
                                title=ft.TextField(label="名字"),
                            ),
                            ft.ListTile(
                                leading=ft.Icon(ft.Icons.ATTACH_MONEY),
                                title=ft.TextField(label="每小时多少钱"),
                            ),

                            ft.ListTile(
                                leading=ft.Icon(ft.Icons.ACCESS_TIME),
                                title=ft.Row([
                                    ft.ElevatedButton(
                                        "设置日期",
                                        icon=ft.Icons.CALENDAR_MONTH,
                                        on_click=lambda e: page.open(
                                            ft.DatePicker(
                                                cancel_text="取消",
                                                confirm_text="确定",
                                                field_label_text="输入日期",
                                                help_text="选择日期",
                                                field_hint_text="yyyy/mm/dd",
                                                date_picker_entry_mode=ft.DatePickerEntryMode.INPUT,
                                                # first_date=datetime.datetime(year=2023, month=10, day=1),
                                                # last_date=datetime.datetime(year=2024, month=10, day=1),
                                                on_change=select_day,
                                            )
                                        ),
                                    ),
                                    ft.ElevatedButton(
                                        "开始时间",
                                        icon=ft.Icons.AV_TIMER,
                                        on_click=lambda _: page.open(begin_time_picker),
                                    ),
                                    ft.ElevatedButton(
                                        "结束时间",
                                        icon=ft.Icons.AV_TIMER,
                                        on_click=lambda _: page.open(end_time_picker),
                                    ),
                                ]),
                            ),
                            ft.Divider(height=10, thickness=1),
                            ft.Row([
                                ft.ElevatedButton(
                                    text="添加数据",
                                    icon=ft.Icons.DONE,
                                    icon_color="green",
                                    on_click=add_data,
                                    style=ft.ButtonStyle(
                                        text_style=ft.TextStyle(
                                            font_family="MiSans"
                                        )
                                    )
                                ),
                                ft.ElevatedButton(
                                    text="删除数据",
                                    icon=ft.Icons.DELETE,
                                    icon_color="red",
                                    style=ft.ButtonStyle(
                                        text_style=ft.TextStyle(
                                            font_family="MiSans"
                                        )
                                    )
                                ),
                                ft.ElevatedButton(
                                    text="清空数据",
                                    icon=ft.Icons.CLEANING_SERVICES,
                                    icon_color="yellow",
                                    style=ft.ButtonStyle(
                                        text_style=ft.TextStyle(
                                            font_family="MiSans"
                                        )
                                    )
                                ),
                            ],alignment=ft.MainAxisAlignment.CENTER),
                            ft.Container(
                                height=5
                            )
                        ]),
                    ),
                ]
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,

    ),

    return column