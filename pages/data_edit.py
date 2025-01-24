import flet as ft


def handle_picker_change(page, e):
    selected_fruit_ref.current.value = fruits[int(e.data)]
    page.update()

selected_fruit_ref = ft.Ref[ft.Text]()
fruits = ["苹果","香蕉","橙子"]
cupertino_picker = ft.CupertinoPicker(
        selected_index=0,  # 修改初始索引为0
        magnification=1.22,
        squeeze=1.2,
        use_magnifier=True,
        on_change=lambda e: handle_picker_change(ft.Page, e),
        controls=[ft.Text(value=f) for f in fruits],
    )
def data_edit_page(page: ft.Page):
    # time_picker = ft.TimePicker(
    #     confirm_text="Confirm",
    #     error_invalid_text="Time out of range",
    #     help_text="Pick your time slot",
    # )
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
            ft.Container(
                content=ft.Column([
                    ft.Row(
                        tight=True,
                        controls=[
                            ft.Text("选择水果:", size=23),
                            ft.TextButton(
                                content=ft.Text(value=fruits[0], ref=selected_fruit_ref, size=23),  # 修改初始值索引为0
                                style=ft.ButtonStyle(color=ft.Colors.BLUE),
                                on_click=lambda e: page.open(
                                    ft.CupertinoBottomSheet(
                                        cupertino_picker,
                                        height=216,
                                        padding=ft.padding.only(top=6),
                                    )
                                ),
                            ),
                        ],
                    ),
                ]),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.Colors.AMBER,
                height=150,
                border_radius=10,
            ),
            # 添加一个按钮以在页面中添加一行表单数据
            # ft.Row([
            #     ft.ElevatedButton(
            #         text="再加一行",
            #         icon=ft.Icons.ADD_BOX,
            #         icon_color="green",
            #         style=ft.ButtonStyle(
            #             text_style=ft.TextStyle(
            #                 font_family="MiSans"
            #             )
            #         )
            #     )
            # ], alignment=ft.MainAxisAlignment.CENTER),
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START
    )
    return column