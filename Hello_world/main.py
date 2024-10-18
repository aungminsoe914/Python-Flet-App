import flet as ft


def main(page: ft.Page):
    text=ft.Text(value="Hello World",color="green")
    page.add(text)
ft.app(main)
