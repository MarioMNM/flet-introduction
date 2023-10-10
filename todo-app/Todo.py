import flet as ft

class TodoApp(ft.UserControl):
    def build(self):
        self.new_task = ft.TextField(hint_text="Add a new To-Do", expand=True)
        self.tasks_view = ft.Column()

        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD, 
                            on_click=self.handleAddEvent
                        ),
                    ],
                ),
                self.tasks_view,
            ],
        )

    def handleAddEvent(self, e):
        self.tasks_view.controls.append(ft.Checkbox(label=self.new_task.value))
        self.new_task.value = ""
        self.update()