def list_action(task_db):
    return task_db.get_all_tasks()


def get_action(task_db, name):
    return task_db.get_task(name)


def add_action(task_db, task):
    return task_db.add_task(task)


def edit_action(task_db, old_name, edited_task):
    return task_db.edit_task(old_name=old_name, edited_task=edited_task)


def delete_action(task_db, name):
    return task_db.delete_task(name)
