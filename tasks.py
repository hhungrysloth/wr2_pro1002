def add_task(task_list, task):
    """Add a task to a list if it is not already present."""
    task = task.strip()
    if task and task not in task_list:
        task_list.append(task)
    return task_list


def remove_task(task_list, task):
    """Remove a task from the list if it exists."""
    task = task.strip()
    if task in task_list:
        task_list.remove(task)
    return task_list