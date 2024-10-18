import flet as ft


def main(page: ft.Page):
    def dropdownclick(e):
       text.value=f"select value is {dropdown.value}"
       page.update()
    
    text = ft.Text()
    dropdown = ft.Dropdown(
        width=300,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue")
        ]
    )
    btn = ft.ElevatedButton("Submit",on_click=dropdownclick)
    page.add(btn,dropdown,text)
ft.app(main)
