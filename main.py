import flet as ft
import random
from pages import data_edit
from pages import history

Imgpath = [f"./assets/GIF/0.jpg",
        f"./assets/GIF/2.gif",
        f"./assets/GIF/3.gif",
        f"./assets/GIF/4.gif",
        f"./assets/GIF/5.gif",
        f"./assets/GIF/6.gif",
        f"./assets/GIF/7.gif",
        f"./assets/GIF/8.gif",
        f"./assets/GIF/9.gif",
        f"./assets/GIF/10.gif"]
def main(page: ft.Page):
    page.scroll= "auto"
    # 创建页面内容的占位符
    page_content = ft.Column()
    random_number = random.randint(1, 10)
    text=Imgpath[random_number-1]

    # 更新页面内容的函数
    def update_page_content(selected_index: int):
        if selected_index == 0:
            page_content.controls = [data_edit.data_edit_page(page)]
        elif selected_index == 1:
            page_content.controls = [history.history_page()]
        page.update()

    # 应用标题栏
    page.appbar = ft.AppBar(
        center_title=True,
        title=ft.Text("记账小助手", weight=ft.FontWeight.BOLD, font_family="MiSans"),
        actions=[
            ft.IconButton(
                icon=ft.Icons.INFO,
                icon_size=20,
                on_click=lambda e: page.open(about_windows)
            ),
            ft.Container(
                width=12
            )
        ]
    )

    # 关于界面弹窗
    def about_close(e):
        page.close(about_windows)

    about_windows = ft.AlertDialog(
        modal=True,
        title=ft.Text("关于本应用", weight=ft.FontWeight.BOLD, font_family="MiSans"),
        content=ft.Column(
            [
                ft.Text(spans=[
                    ft.TextSpan("心怀感激地使用"),
                    ft.TextSpan(
                        "Flet",
                        ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, weight=ft.FontWeight.NORMAL, size=15,
                                     color="#5abae7"),
                        url="https://flet.dev/"
                    ),
                    ft.TextSpan("构建")
                ]),
                ft.Text("由jmzdd用♥为你制作"),
                ft.Text(spans=[
                    ft.TextSpan("Github主页："),
                    ft.TextSpan(
                        "jmzdd",
                        ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, weight=ft.FontWeight.NORMAL, size=15, color="#5abae7"),
                        url="https://github.com/jmzdd"
                    ),
                ]),
                ft.Text("版本号：v1.0.0", weight=ft.FontWeight.NORMAL, font_family="MiSans")
            ],
            tight=True  # 控件紧密排列，不增加额外间距
        ),
        actions=[
            ft.TextButton("好的", on_click=about_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # 初始化导航栏
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.DATA_THRESHOLDING_OUTLINED,
                selected_icon=ft.Icons.DATA_THRESHOLDING,
                label="数据编辑",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.FEATURED_PLAY_LIST_OUTLINED,
                selected_icon=ft.Icons.FEATURED_PLAY_LIST,
                label="账单生成",
            )
        ],
        # 假设 e 是 ControlEvent 对象
        on_change=lambda e: update_page_content(e.control.selected_index)  # 获取选中的索引
    )

    # 创建欢迎界面
    def switch_to_main(e):
        # 移除欢迎页面
        page.controls.remove(welcome_page)

        # 设置 AppBar 为可见
        page.appbar.visible = True
        page.navigation_bar.visible = True
        page_content.visible = True
        page.update()

    welcome_page = ft.Stack([
        ft.Container(
            content=ft.Column([
                ft.Text("欢迎使用记账小助手！", size=25, weight=ft.FontWeight.BOLD, font_family="MiSans"),
                ft.Text("辛苦了一天，记得好好休息哦~", size=15),
                ft.Image(
                    src=text,
                    width=200,
                    height=200
                ),
                ft.Container(height=25),  # 使用Container来创建间距
                ft.ElevatedButton("🎉进入应用🎉", style=ft.ButtonStyle(text_style=ft.TextStyle(color=ft.Colors.BLACK, font_family="MiSans")), on_click=lambda e: switch_to_main(e))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            alignment=ft.alignment.center,
            width=page.width,
            height=page.height
        )
    ])

    # 初始状态下隐藏主界面
    page.appbar.visible = False
    page.navigation_bar.visible = False
    page_content.visible = False

    # 设置初始页面内容
    update_page_content(0)  # 默认显示“数据编辑”页面
    page.add(page_content)
    page.add(welcome_page)

ft.app(main)
