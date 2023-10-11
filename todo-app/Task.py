import flet as ft


class Task(ft.UserControl):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete
    
    def build(self):
        self.display_task = ft.Checkbox(
            value=False, 
            label=self.task_name, 
            on_change=self.handleStatusChange
        )
    
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.handleEdit
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.handleDelete
                        )
                    ]
                )
            ]
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.handleSave
                )
            ]
        )

        return ft.Column(controls=[self.display_view, self.edit_view])
    
    def handleEdit(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def handleSave(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def handleDelete(self, e):
        self.delete_task(self)
    
    def handleStatusChange(self, e):
        self.completed = self.display_task.value
        self.task_status_change(self)