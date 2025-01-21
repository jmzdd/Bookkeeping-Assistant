import flet as ft
def data_edit_page(page: ft.Page):
    time_picker = ft.TimePicker(
        confirm_text="Confirm",
        error_invalid_text="Time out of range",
        help_text="Pick your time slot",
    )
    # 使用 Column 布局将多个组件垂直排列
    column = ft.Column(
        [
            ft.ElevatedButton(
                "时间选择按钮",
                icon=ft.Icons.TIME_TO_LEAVE,
                on_click=lambda _: page.open(time_picker),
            ),
            ft.ExpansionPanelList(
                # expand_icon_color=ft.Colors.AMBER,
                # divider_color=ft.Colors.AMBER,
                elevation=5,
                controls=[
                    ft.ExpansionPanel(
                        header=ft.ListTile(title=ft.Text("初始化数据"),bgcolor=ft.Colors.BLUE_400),
                        bgcolor=ft.Colors.BLUE_400,
                        expanded=True,
                        content=ft.ListTile(
                            title=ft.Text("This is in Panel 0"),
                            subtitle=ft.Text("Press the icon to delete panel 0"),
                            trailing=ft.IconButton(
                                ft.Icons.DELETE,
                                on_click=lambda _: print("Delete panel 0"),
                            ),
                        ),
                    ),
                ]
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START
    )
    return column