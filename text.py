import flet as ft
from data_manager import DataManager
from datetime import datetime

# 在页面顶部定义一个全局变量用于保存时间差数据
time_diffs = []

def data_edit_page(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    data_manager = DataManager()

    def select_day(e):
        data_manager.set_work_day(e.control.value.strftime('%Y-%m-%d'))

    def select_begin_time(e):
        data_manager.set_begin_time(begin_time_picker.value)

    def select_end_time(e):
        data_manager.set_end_time(end_time_picker.value)

    def add_data(e):
        start_time = data_manager.get_begin_time()
        end_time = data_manager.get_end_time()

        # 假设今天是基准日期
        today = datetime.today()
        start_datetime = datetime.combine(today, start_time)
        end_datetime = datetime.combine(today, end_time)

        time_diff = end_datetime - start_datetime

        # 创建新的控件并添加到 dynamic_column
        new_control = ft.Text(f"Time difference: {time_diff}")
        test_column.controls.append(new_control)

        # 将时间差数据保存到全局变量中
        time_diffs.append(time_diff)

        # 更新页面以显示新控件
        page.update()

    # 定义删除数据的函数
    def delete_data(e):
        if test_column.controls:
            # 移除最后一个控件
            test_column.controls.pop()
            # 移除最后一个时间差数据
            time_diffs.pop()
            # 更新页面以反映更改
            page.update()

    # 在页面初始化时加载已保存的时间差数据
    def load_saved_data():
        for diff in time_diffs:
            new_control = ft.Text(f"Time difference: {diff}")
            test_column.controls.append(new_control)

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

    # 动态添加控件的容器
    test_column = ft.Column(controls=[])

    dynamic_column = ft.Column(controls=[
        ft.Container(
            content=
            ft.Column(controls=[
                ft.Row([
                        ft.Icon(name=ft.Icons.CIRCLE, color=ft.Colors.RED, size=20),
                        ft.Icon(name=ft.Icons.CIRCLE, color=ft.Colors.ORANGE, size=20),
                        ft.Icon(name=ft.Icons.CIRCLE, color=ft.Colors.GREEN, size=20),
                ]),
                # 终端容器
                ft.Container(
                    content=test_column,
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    border_radius=10,
                    bgcolor=ft.Colors.OUTLINE_VARIANT,
                ),
            ]),
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            border_radius=10,
            bgcolor=ft.colors.BLUE_GREY_200,
        ),
    ])

    main_column = ft.Column(
        controls=[
            ft.ExpansionPanelList(
                elevation=5,
                controls=[
                    ft.ExpansionPanel(
                        header=ft.ListTile(title=ft.Text("数据设置", weight=ft.FontWeight.NORMAL, font_family="MiSans")),
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
                                        text_style=ft.TextStyle(font_family="MiSans")
                                    )
                                ),
                                ft.ElevatedButton(
                                    text="删除数据",
                                    icon=ft.Icons.DELETE,
                                    icon_color="red",
                                    on_click=delete_data,  # 绑定删除数据的函数
                                    style=ft.ButtonStyle(
                                        text_style=ft.TextStyle(font_family="MiSans")
                                    )
                                ),
                                ft.ElevatedButton(
                                    text="清空数据",
                                    icon=ft.Icons.CLEANING_SERVICES,
                                    icon_color="yellow",
                                    style=ft.ButtonStyle(
                                        text_style=ft.TextStyle(font_family="MiSans")
                                    )
                                ),
                            ], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Container(height=5)
                        ]),
                    ),
                ]
            ),
            dynamic_column  # 将动态添加控件的容器添加到这里
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
    )
    load_saved_data()
    return main_column
