import flet as ft


def main(page: ft.Page):
    def funct_click(e):
        page.add(ft.Checkbox(label=text_box.value))
        text_box.value=""
        text_box.focus()
        text_box.update()
    
    text_box = ft.TextField(hint_text="Enter Text")
    btn = ft.ElevatedButton("Clicked!",on_click=funct_click)
    page.add(text_box,btn)
ft.app(main)
