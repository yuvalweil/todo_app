import streamlit as st

# Initialize the task list in Streamlit's session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []


def add_task():
    """Add a task from the text input to the session task list."""
    new_task = st.session_state.new_task_input.strip()
    if new_task:
        st.session_state.tasks.append(new_task)
        st.session_state.new_task_input = ""  # clear the box
    else:
        st.warning("Please enter a task before adding.")


def delete_task(index: int):
    """Delete a task by its index from the session task list."""
    st.session_state.tasks.pop(index)
    st.rerun()  # Refresh the app to update the list


def main():
    st.title("✅ Personal Task Manager")
    st.write("Simple web UI version of your CLI todo app.")

    # --- Add task section ---
    st.subheader("Add a new task")
    st.text_input(
        "Task description",
        key="new_task_input",
        placeholder="e.g. Buy milk, finish project, call mom..."
    )
    st.button("Add task", on_click=add_task)

    st.markdown("---")

    # --- Task list section ---
    st.subheader("Your tasks")

    if not st.session_state.tasks:
        st.info("No tasks yet. Add one above! 🙂")
    else:
        for i, task in enumerate(st.session_state.tasks):
            cols = st.columns([6, 1])
            with cols[0]:
                st.write(f"{i + 1}. {task}")
            with cols[1]:
                # Each delete button has a unique key
                if st.button("Delete", key=f"delete_{i}"):
                    delete_task(i)


if __name__ == "__main__":
    main()