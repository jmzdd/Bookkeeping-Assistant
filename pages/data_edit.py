import flet as ft
import datetime
def data_edit_page(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_change(e):
        page.add(ft.Text(f"Date changed: {e.control.value.strftime('%Y-%m-%d')}"))

    def handle_dismissal(e):
        page.add(ft.Text(f"DatePicker dismissed"))

    time_picker = ft.TimePicker(
        confirm_text="Confirm",
        error_invalid_text="Time out of range",
        help_text="Pick your time slot",
    )
    # 使用 Column 布局将多个组件垂直排列
    column = ft.Column(
        [
            # ft.ElevatedButton(
            #     "时间选择按钮",
            #     icon=ft.Icons.TIME_TO_LEAVE,
            #     on_click=lambda _: page.open(time_picker),
            # ),
            ft.ExpansionPanelList(
                elevation=5,
                controls=[
                    ft.ExpansionPanel(
                        header=ft.ListTile(title=ft.Text("基本设置",weight=ft.FontWeight.NORMAL, font_family="MiSans")),
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
                                leading=ft.Icon(ft.Icons.ATTACH_MONEY),
                                title=ft.Row([
                                    ft.ElevatedButton(
                                        "时间选择按钮",
                                        icon=ft.Icons.TIME_TO_LEAVE,
                                        on_click=lambda _: page.open(time_picker),
                                    ),
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
                                                first_date=datetime.datetime(year=2023, month=10, day=1),
                                                last_date=datetime.datetime(year=2024, month=10, day=1),
                                                on_change=handle_change,
                                                on_dismiss=handle_dismissal,
                                            )
                                        ),
                                    ),
                                    ft.TextField(label="几",suffix_text="日"),
                                ]),
                            ),
                            ft.Row([
                                ft.ElevatedButton(
                                    text="确认提交",
                                    icon=ft.Icons.DONE,
                                    icon_color="green",
                                    style=ft.ButtonStyle(
                                        text_style=ft.TextStyle(
                                            font_family="MiSans"
                                        )
                                    )
                                )
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
        horizontal_alignment=ft.CrossAxisAlignment.START
    )
    return column