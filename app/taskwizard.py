from app.src.cmd.TaskWizardCLI import TaskWizard


def start_app():
    cli = TaskWizard()
    cli.run()


if __name__ == "__main__":
    start_app()
