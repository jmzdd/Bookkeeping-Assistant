import flet as ft


def main(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    selected_fruit_ref = ft.Ref[ft.Text]()
    fruits = [
        "苹果",
        "香蕉",
        "橙子",
    ]

    def handle_picker_change(e):
        selected_fruit_ref.current.value = fruits[int(e.data)]
        page.update()

    cupertino_picker = ft.CupertinoPicker(
        selected_index=0,  # 修改初始索引为0
        magnification=1.22,
        squeeze=1.2,
        use_magnifier=True,
        on_change=handle_picker_change,
        controls=[ft.Text(value=f) for f in fruits],
    )

    page.add(
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
    )


ft.app(main)
