import click, uuid, sqlite3
from .models import Task, Priority
from .text_helpers import red_text, green_text


class TaskWizardDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.con = sqlite3.connect(self.db_name)
        self.cur = self.con.cursor()
        self.create_table()

    def __del__(self):
        self.con.close()

    def create_table(self):
        self.cur.execute(
            """
    CREATE TABLE IF NOT EXISTS Tasks (
      id TEXT PRIMARY KEY,
      name TEXT NOT NULL,
      due_date DATE NOT NULL,
      priority TEXT NOT NULL,
      description TEXT
    )
    """
        )
        self.con.commit()

    def get_all_tasks(self):
        try:
            sql = """SELECT * FROM Tasks"""
            self.cur.execute(sql)
            rows = self.cur.fetchall()
            tasks = []

            for row in rows:
                task = Task(
                    name=row[1],
                    due_date=row[2],
                    priority=Priority[row[3]],
                    description=row[4],
                    id=uuid.UUID(row[0]),
                )
                tasks.append(task)
            return tasks

        except sqlite3.Error as e:
            self._print_sql_error(e)
            return []

    def get_task(self, name):
        try:
            sql = """SELECT id, name, due_date, priority, description
              FROM Tasks WHERE name = ? """
            self.cur.execute(sql, (name,))
            row = self.cur.fetchone()

            if row:
                task = Task(
                    name=row[1],
                    due_date=row[2],
                    priority=Priority[row[3]],
                    description=row[4],
                    id=uuid.UUID(row[0]),
                )
                return task
            else:
                return None
        except sqlite3.Error as e:
            self._print_sql_error(e)
            return None

    def add_task(self, task):
        try:
            sql = """INSERT INTO Tasks (id, name, due_date, priority, description)
                     VALUES (?, ?, ?, ?, ?)
                  """
            self.cur.execute(
                sql,
                (
                    str(task.id),
                    task.name,
                    task.due_date,
                    task.priority.name,
                    task.description,
                ),
            )
            self.con.commit()
            click.echo(green_text(f"Task '{task.name}' added successfully."))
        except sqlite3.Error as e:
            self._print_sql_error(e)

    def edit_task(self, old_name, edited_task: Task):
        try:
            sql = """UPDATE Tasks 
                     SET name = ?, due_date = ?, priority = ?, description = ?
                     WHERE name = ?"""
            self.cur.execute(
                sql,
                (
                    edited_task.name,
                    edited_task.due_date,
                    edited_task.priority.name,
                    edited_task.description,
                    old_name,
                ),
            )
            self.con.commit()
            click.echo(green_text(f"Task '{old_name}' updated successfully."))
        except sqlite3.Error as e:
            self._print_sql_error(e)

    def delete_task(self, name):
        try:
            sql = """DELETE FROM Tasks WHERE name = ?"""
            self.cur.execute(sql, (name,))
            self.con.commit()
            click.echo(green_text(f"'{name}' was deleted successfully."))
        except sqlite3.Error as e:
            self._print_sql_error(e)

    def _print_sql_error(self, e):
        click.echo(red_text(f"Database Error: {e}"))
