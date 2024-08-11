import click
from datetime import datetime
from .. import taskdb
from ..text_helpers import *
from . import cmd_actions
from ..models import Task, Priority


class TaskItCLI:
    def __init__(self):
        self.task_db = taskdb.TaskDatabase("taskit.db")
        self.commands = {
            "exit": self.exit_cmd,
            "help": self.help_cmd,
            "clear": self.clear_cmd,
            "list": self.list_cmd,
            "get": self.get_cmd,
            "add": self.add_cmd,
            "edit": self.edit_cmd,
            "delete": self.delete_cmd,
        }

    def run(self):
        print_logo()
        while True:
            user_input = click.prompt("cmd %").lower().strip()
            print_logo()
            cmd = self.commands.get(user_input, lambda: self.unknown_cmd(user_input))
            if cmd() == "exit":
                break

    def exit_cmd(self):
        click.echo("Exiting TaskIt... Goodbye")
        return "exit"

    def help_cmd(self):
        print_commands()

    def clear_cmd(self):
        pass

    def list_cmd(self):
        tasks = cmd_actions.list_action(self.task_db)
        if tasks:
            for task in tasks:
                click.echo(str(task))
                click.echo("-" * 40)
        else:
            click.echo(red_text("No tasks found."))

    def get_cmd(self):
        name = click.prompt("Name").strip()
        task = cmd_actions.get_action(self.task_db, name)
        if task:
            click.echo(str(task))
        else:
            click.echo(red_text(f"'{name}' was not found... Tasks are case sensitive"))

    def add_cmd(self):
        name = self._get_unique_name()
        due_date = self._get_valid_due_date()
        priority = self._get_priority()
        description = self._get_description()

        new_task = Task(name, due_date, priority, description)
        cmd_actions.add_action(self.task_db, new_task)

    def edit_cmd(self):
        old_name = self._get_existing_name()
        click.echo(green_text(f"Task '{old_name}' found!"))
        click.echo(str(cmd_actions.get_action(self.task_db, old_name)))
        click.echo(blue_text("Make the edits below"))
        new_name = self._get_unique_name()
        new_due_date = self._get_valid_due_date()
        new_priority = self._get_priority()
        new_description = self._get_description()

        edited_task = Task(new_name, new_due_date, new_priority, new_description)
        cmd_actions.edit_action(
            self.task_db, old_name=old_name, edited_task=edited_task
        )

    def delete_cmd(self):
        name = self._get_existing_name()
        cmd_actions.delete_action(self.task_db, name)

    def unknown_cmd(self, user_input):
        click.echo(
            red_text(f"'{user_input}' is not a command... ")
            + blue_text("'help'")
            + " will list out available cmds"
        )

    def _get_unique_name(self):
        while True:
            name = click.prompt("Name").strip()
            if self.task_db.get_task(name) is None:
                return name
            click.echo(red_text("Task already exists... Enter a unique Name"))

    def _get_valid_due_date(self):
        while True:
            due_date_str = click.prompt(
                f"Due date ex: {format_date_12(datetime.now())}"
            ).strip()
            due_date = format_date_12(due_date_str)
            if due_date:
                return due_date
            click.echo(red_text(f"{due_date_str} is formatted incorrectly"))
            click.echo("The format needs to be MM/DD/YYYY HH:MM(am/pm)")

    def _get_priority(self):
        priority_choices = [priority.name for priority in Priority]
        priority_str = click.prompt(
            "Priority",
            type=click.Choice(priority_choices, case_sensitive=False),
            default="MEDIUM",
        ).strip()
        return Priority[priority_str]

    def _get_description(self):
        return click.prompt("Description", default="")

    def _get_existing_name(self):
        while True:
            name = click.prompt("Name")
            if self.task_db.get_task(name) is not None:
                return name
            click.echo(red_text(f"'{name}' was not found... Tasks are case sensitive"))
