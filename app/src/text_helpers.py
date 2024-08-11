import click, random
from datetime import datetime

colors = ["red", "green", "yellow", "blue", "magenta", "cyan"]
random_color = random.choice(colors)


def format_date_12(date: str | datetime) -> datetime | None:
    try:
        if isinstance(date, str):
            return datetime.strptime(date, "%m/%d/%Y %I:%M%p")
        elif isinstance(date, datetime):
            return date.strftime("%m/%d/%Y %I:%M%p")
    except ValueError:
        return None


def print_commands():
    cmds = {
        "exit": "Exit TaskIt",
        "help": "List all available commands",
        "clear": "Clear cmd",
        "list": "List all tasks",
        "get": "List a specific task",
        "add": "Add a new task",
        "edit": "Edit an existing task",
        "delete": "Delete a task",
    }
    click.echo("Avaliable Commands:")
    for cmd, description in cmds.items():
        click.echo(f" {cmd:<10} - {description}")


def print_logo():
    click.clear()
    logo = """
████████╗ █████╗ ███████╗██╗  ██╗██╗████████╗
╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝██║╚══██╔══╝
   ██║   ███████║███████╗█████╔╝ ██║   ██║   
   ██║   ██╔══██║╚════██║██╔═██╗ ██║   ██║   
   ██║   ██║  ██║███████║██║  ██╗██║   ██║   
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   
           """

    click.echo(click.style(logo, fg=random_color))


def red_text(text):
    return click.style(text, fg="red", bold=True)


def green_text(text):
    return click.style(text, fg="green", bold=True)


def blue_text(text):
    return click.style(text, fg="blue", bold=True)
