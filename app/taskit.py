from app.src.cmd.TaskItCLI import TaskItCLI


def start_app():
    cli = TaskItCLI()
    cli.run()


if __name__ == "__main__":
    start_app()
