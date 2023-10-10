import flet as ft
from Todo import TodoApp


def main(page: ft.Page):
    page.title = "To-Do App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # create app instance
    todo = TodoApp()

    # add app's root control to page
    page.add(todo)


ft.app(main)
