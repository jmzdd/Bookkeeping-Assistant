import flet as ft
from data_manager import DataManager
from datetime import datetime

info_column = ft.Column(controls=[])
data_column = ft.Column(controls=[])
def data_edit_page(page: ft.Page, data_manager: DataManager):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def select_day(e):
        data_manager.set_work_day(e.control.value.strftime('%Y-%m-%d'))

    def select_begin_time(e):
        data_manager.set_begin_time(begin_time_picker.value)

    def select_end_time(e):
        data_manager.set_end_time(end_time_picker.value)

    # 关闭提示窗口函数
    def close_windows(e):
        page.close(cue_window)

    cue_window = ft.AlertDialog(
        modal=True,
        title=ft.Text("提示消息"),
        icon=ft.Icon(name="WARNING", color="yellow"),
        content=data_column,
        inset_padding=50,
        actions=[
            ft.TextButton("好的", on_click=close_windows),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def add_data(e):
        user_day = data_manager.get_work_day()
        start_time = data_manager.get_begin_time()
        end_time = data_manager.get_end_time()
        data_column.controls.clear()
        if user_day is None or start_time is None or end_time is None:
            if user_day is None:
                data_column.controls.append(ft.Text("请选择日期"))
            if start_time is None:
                data_column.controls.append(ft.Text("请选择开始时间"))
            if end_time is None:
                data_column.controls.append(ft.Text("请选择结束时间"))
            data_column.height = 100  # 设置最大高度
            data_column.expand = False  # 禁用自动扩展
            page.open(cue_window)
        else:
            # 假设今天是基准日期
            today = datetime.today()
            start_datetime = datetime.combine(today, start_time)
            end_datetime = datetime.combine(today, end_time)

            time_diff = end_datetime - start_datetime

            # 将时间差转换为小时数
            hours_diff = time_diff.total_seconds() / 3600

            # 格式化时间
            formatted_start_time = start_time.strftime("%H时%M分")
            formatted_end_time = end_time.strftime("%H时%M分")

            # 创建新的控件并添加到 dynamic_column
            new_control = ft.Text(f"{user_day}, {formatted_start_time}-{formatted_end_time}, 共{hours_diff:.1f}小时, 共{float(hours_diff) * float(data_manager.get_hourly_rate())}米")
            info_column.controls.append(new_control)

            data_manager.add_data(hours_diff, user_day, start_time, end_time)

            # 更新页面以显示新控件
            page.update()

    # 定义删除数据的函数
    def delete_data(e):
        if info_column.controls:
            # 移除最后一个控件
            info_column.controls.pop()
        # 移除存储的数据
        data_manager.delete_data()

        # 更新页面以反映更改
        page.update()

    # 定义清空数据的函数
    def clear_data(e):
        # 清空所有控件
        info_column.controls.clear()
        # 清空所有存储的数据
        data_manager.time_diffs.clear()
        data_manager.work_days.clear()
        data_manager.start_times.clear()
        data_manager.end_times.clear()
        # 更新页面以反映更改
        page.update()

    def set_name(e):
        data_manager.set_name(e.control.value)

    def set_hourly_rate(e):
        data_manager.set_hourly_rate(e.control.value)

    end_time_picker = ft.TimePicker(
        confirm_text="确认",
        cancel_text="取消",
        error_invalid_text="时间超出范围",
        help_text="请选择时间",
        hour_label_text="小时",
        minute_label_text="分钟",
        time_picker_entry_mode=ft.TimePickerEntryMode.INPUT,
        on_change=select_end_time,
    )

    begin_time_picker = ft.TimePicker(
        confirm_text="确认",
        cancel_text="取消",
        error_invalid_text="时间超出范围",
        help_text="请选择时间",
        hour_label_text="小时",
        minute_label_text="分钟",
        time_picker_entry_mode=ft.TimePickerEntryMode.INPUT,
        on_change=select_begin_time,
    )

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
                    content=info_column,
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
                                title=ft.TextField(
                                    label="名字",
                                    value=data_manager.get_name(),
                                    on_change=set_name
                                ),
                            ),
                            ft.ListTile(
                                leading=ft.Icon(ft.Icons.ATTACH_MONEY),
                                title=ft.TextField(
                                    label="每小时多少米",
                                    value=data_manager.get_hourly_rate(),
                                    on_change=set_hourly_rate
                                ),
                            ),
                            ft.ListTile(
                                # leading=ft.Icon(ft.Icons.ACCESS_TIME),
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
                                ],alignment=ft.MainAxisAlignment.CENTER),
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
                                    on_click=clear_data,  # 绑定清空数据的函数
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
    return main_column
