from nicegui import ui

# In-memory task list
tasks: list[str] = []

# Global references to UI elements (we'll assign them later)
task_input = None
tasks_container = None


def refresh_tasks() -> None:
    """Rebuild the task list UI."""
    tasks_container.clear()

    if not tasks:
        with tasks_container:
            ui.label('No tasks yet. Add one above! 🙂').classes('text-gray-500')
        return

    with tasks_container:
        for i, task in enumerate(tasks):
            with ui.row().classes('items-center gap-2'):
                ui.label(f'{i + 1}. {task}')
                ui.button(
                    'Delete',
                    on_click=lambda _, index=i: delete_task(index),
                ).props('outline color=red')


def add_task(_) -> None:
    """Add a new task from the input box."""
    text = task_input.value.strip()
    if not text:
        ui.notify('Please enter a task before adding.', color='orange')
        return

    tasks.append(text)
    task_input.value = ''
    refresh_tasks()
    ui.notify('Task added!', color='green')


def delete_task(index: int) -> None:
    """Delete task by index and refresh UI."""
    try:
        removed = tasks.pop(index)
        refresh_tasks()
        ui.notify(f"Deleted: {removed}", color='red')
    except IndexError:
        ui.notify('Task not found.', color='negative')


# ---------- Build UI ----------

with ui.column().classes('w-full max-w-xl mx-auto mt-10 gap-4'):
    ui.label('✅ Personal Task Manager').classes('text-2xl font-bold')
    ui.label('NiceGUI web UI version of your todo app.')

    # --- Add task section ---
    ui.separator()
    ui.label('Add a new task').classes('text-lg font-semibold')

    with ui.row().classes('w-full items-center gap-2'):
        task_input = ui.input(
            'Task description',
            placeholder='e.g. Buy milk, finish project, call mom...',
        ).classes('w-full')

        ui.button('Add', on_click=add_task).props('color=primary')

    # Allow pressing Enter to add
    task_input.on('keydown.enter', add_task)

    # --- Tasks list section ---
    ui.separator()
    ui.label('Your tasks').classes('text-lg font-semibold')

    tasks_container = ui.column().classes('w-full')

# Initial render
refresh_tasks()

# Run the app
ui.run(title='Personal Task Manager', reload=False)