import flet as ft

# 菜单组件方法
selected_months_ref = ft.Ref[ft.Text]()
selected_days_ref = ft.Ref[ft.Text]()
selected_hours_ref = ft.Ref[ft.Text]()
selected_minutes_ref = ft.Ref[ft.Text]()
selected_half_days_ref = ft.Ref[ft.Text]()

# 菜单列表
months = ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]
days = ["1日","2日","3日","4日","5日","6日","7日","8日","9日","10日","11日","12日","13日","14日","15日","16日","17日","18日","19日","20日","21日","22日","23日","24日","25日","26日","27日","28日","29日","30日","31日"]
half_days = ["上午","下午"]
hours = ["1点","2点","3点","4点","5点","6点","7点","8点","9点","10点","11点","12点"]
minutes = ["1分","2分","3分","4分","5分","6分","7分","8分","9分","10分","11分","12分","13分","14分","15分","16分","17分","18分","19分","20分","21分","22分","23分","24分","25分","26分","27分","28分","29分","30分",
           "31分","32分","33分","34分","35分","36分","37分","38分","39分","40分","41分","42分","43分","44分","45分","46分","47分","48分","49分","50分","51分","52分","53分","54分","55分","56分","57分","58分","59分"]


def data_edit_page(page: ft.Page):
    def months_change(e):
        selected_months_ref.current.value = months[int(e.data)]
        page.update()
    def days_change(e):
        selected_days_ref.current.value = days[int(e.data)]
        page.update()
    def half_days_change(e):
        selected_half_days_ref.current.value = half_days[int(e.data)]
        page.update()
    def hours_change(e):
        selected_hours_ref.current.value = hours[int(e.data)]
        page.update()
    def minutes_change(e):
        selected_minutes_ref.current.value = minutes[int(e.data)]
        page.update()
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
                    ft.Row([
                        ft.Text("选择日期：", weight=ft.FontWeight.NORMAL, font_family="MiSans"),
                        ft.TextButton(
                            content=ft.Text(value=months[0], ref=selected_months_ref, weight=ft.FontWeight.NORMAL, font_family="MiSans"),
                            # style=ft.ButtonStyle(color=ft.Colors.BLUE),
                            on_click=lambda e: page.open(
                                ft.CupertinoBottomSheet(
                                    ft.CupertinoPicker(
                                        selected_index=3,
                                        magnification=1.22,
                                        squeeze=1.2,
                                        use_magnifier=True,
                                        on_change=months_change,
                                        controls=[ft.Text(value=f) for f in months],
                                    ),
                                    height=216,
                                    padding=ft.padding.only(top=6),
                                )
                            ),
                        ),
                        ft.TextButton(
                            content=ft.Text(value=days[0], ref=selected_days_ref, weight=ft.FontWeight.NORMAL, font_family="MiSans"),
                            # style=ft.ButtonStyle(color=ft.Colors.BLUE),
                            on_click=lambda e: page.open(
                                ft.CupertinoBottomSheet(
                                    ft.CupertinoPicker(
                                        selected_index=3,
                                        magnification=1.22,
                                        squeeze=1.2,
                                        use_magnifier=True,
                                        on_change=days_change,
                                        controls=[ft.Text(value=f) for f in days],
                                    ),
                                    height=216,
                                    padding=ft.padding.only(top=6),
                                )
                            ),
                        ),
                    ]),
                    ft.Row([
                        ft.Text("从什么时候开始：", weight=ft.FontWeight.NORMAL, font_family="MiSans"),
                        ft.TextButton(
                            content=ft.Text(value=half_days[0], ref=selected_half_days_ref, weight=ft.FontWeight.NORMAL,
                                            font_family="MiSans"),
                            # style=ft.ButtonStyle(color=ft.Colors.BLUE),
                            on_click=lambda e: page.open(
                                ft.CupertinoBottomSheet(
                                    ft.CupertinoPicker(
                                        selected_index=3,
                                        magnification=1.22,
                                        squeeze=1.2,
                                        use_magnifier=True,
                                        on_change=half_days_change,
                                        controls=[ft.Text(value=f) for f in half_days],
                                    ),
                                    height=216,
                                    padding=ft.padding.only(top=6),
                                )
                            ),
                        ),
                        ft.TextButton(
                            content=ft.Text(value=hours[0], ref=selected_hours_ref, weight=ft.FontWeight.NORMAL,
                                            font_family="MiSans"),
                            # style=ft.ButtonStyle(color=ft.Colors.BLUE),
                            on_click=lambda e: page.open(
                                ft.CupertinoBottomSheet(
                                    ft.CupertinoPicker(
                                        selected_index=3,
                                        magnification=1.22,
                                        squeeze=1.2,
                                        use_magnifier=True,
                                        on_change=hours_change,
                                        controls=[ft.Text(value=f) for f in hours],
                                    ),
                                    height=216,
                                    padding=ft.padding.only(top=6),
                                )
                            ),
                        ),
                        ft.TextButton(
                            content=ft.Text(value=minutes[0], ref=selected_minutes_ref, weight=ft.FontWeight.NORMAL,
                                            font_family="MiSans"),
                            # style=ft.ButtonStyle(color=ft.Colors.BLUE),
                            on_click=lambda e: page.open(
                                ft.CupertinoBottomSheet(
                                    ft.CupertinoPicker(
                                        selected_index=3,
                                        magnification=1.22,
                                        squeeze=1.2,
                                        use_magnifier=True,
                                        on_change=minutes_change,
                                        controls=[ft.Text(value=f) for f in minutes],
                                    ),
                                    height=216,
                                    padding=ft.padding.only(top=6),
                                )
                            ),
                        ),
                    ]),
                    # ft.Row([
                    #     ft.Text("从什么时候结束：", weight=ft.FontWeight.NORMAL, font_family="MiSans"),
                    #     ft.TextButton(
                    #         content=ft.Text(value=half_days[0], ref=selected_half_days_ref, weight=ft.FontWeight.NORMAL,
                    #                         font_family="MiSans"),
                    #         # style=ft.ButtonStyle(color=ft.Colors.BLUE),
                    #         on_click=lambda e: page.open(
                    #             ft.CupertinoBottomSheet(
                    #                 ft.CupertinoPicker(
                    #                     selected_index=3,
                    #                     magnification=1.22,
                    #                     squeeze=1.2,
                    #                     use_magnifier=True,
                    #                     on_change=half_days_change,
                    #                     controls=[ft.Text(value=f) for f in half_days],
                    #                 ),
                    #                 height=216,
                    #                 padding=ft.padding.only(top=6),
                    #             )
                    #         ),
                    #     ),
                    #     ft.TextButton(
                    #         content=ft.Text(value=hours[0], ref=selected_hours_ref, weight=ft.FontWeight.NORMAL,
                    #                         font_family="MiSans"),
                    #         # style=ft.ButtonStyle(color=ft.Colors.BLUE),
                    #         on_click=lambda e: page.open(
                    #             ft.CupertinoBottomSheet(
                    #                 ft.CupertinoPicker(
                    #                     selected_index=3,
                    #                     magnification=1.22,
                    #                     squeeze=1.2,
                    #                     use_magnifier=True,
                    #                     on_change=hours_change,
                    #                     controls=[ft.Text(value=f) for f in hours],
                    #                 ),
                    #                 height=216,
                    #                 padding=ft.padding.only(top=6),
                    #             )
                    #         ),
                    #     ),
                    #     ft.TextButton(
                    #         content=ft.Text(value=minutes[0], ref=selected_minutes_ref, weight=ft.FontWeight.NORMAL,
                    #                         font_family="MiSans"),
                    #         # style=ft.ButtonStyle(color=ft.Colors.BLUE),
                    #         on_click=lambda e: page.open(
                    #             ft.CupertinoBottomSheet(
                    #                 ft.CupertinoPicker(
                    #                     selected_index=3,
                    #                     magnification=1.22,
                    #                     squeeze=1.2,
                    #                     use_magnifier=True,
                    #                     on_change=minutes_change,
                    #                     controls=[ft.Text(value=f) for f in minutes],
                    #                 ),
                    #                 height=216,
                    #                 padding=ft.padding.only(top=6),
                    #             )
                    #         ),
                    #     ),
                    # ]),
                    ft.Row([
                        # ft.Text("这是第一条数据", weight=ft.FontWeight.NORMAL, font_family="MiSans"),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_FOREVER_ROUNDED,
                            icon_color="red",
                            icon_size=20,
                            tooltip="删除这一条数据",
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ]),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.Colors.AMBER,
                height=200,
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