import flet as ft
from Task import Task

class TodoApp(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="Add a new To-Do", expand=True)
        self.tasks = ft.Column()

        self.filter = ft.Tabs(
            selected_index=0,
            on_change=self.handleChangeFilter,
            tabs=[ft.Tab(text="all"), ft.Tab(text="active"), ft.Tab(text="completed")]
        )

        self.items_left = ft.Text("0 items left")

        self.view = ft.Column(
            width=600,
            controls=[
                ft.Row(
                    [ft.Text(value="Todos", style="headlineMedium")],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD, 
                            on_click=self.handleAdd
                        ),
                    ],
                ),
                ft.Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.tasks,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                self.items_left,
                                ft.OutlinedButton(
                                    text="Clear completed", 
                                    on_click=self.handleClearCompleted
                                )
                            ]
                        )
                    ]
                ),
            ],
        )
       
    def build(self):
        return self.view

    def handleAdd(self, e):
        task = Task(self.new_task.value, self.task_status_change, self.delete_task)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    def task_status_change(self, task):
        self.update()

    def delete_task(self, task):
        self.tasks.controls.remove(task)
        self.update()

    def handleClearCompleted(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                self.delete_task(task)

    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.tasks.controls:
            task.visible = (
                status == "all"
                or (status == "active" and task.completed is False)
                or (status == "completed" and task.completed)
            )
            if not task.completed:
                count += 1
        self.items_left.value = f"{count} active item(s) left"
        super().update()
    
    def handleChangeFilter(self, e):
        self.update()