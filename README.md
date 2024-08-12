# TaskWizard

TaskWizard is a command-line interface (CLI) task management application that allows users to create, manage, and track their tasks efficiently.

## Features

- Add new tasks with names, due dates, priorities, and descriptions
- List all tasks
- Get details of a specific task
- Edit existing tasks
- Delete tasks
- User-friendly command-line interface

## Installation

To install TaskWizard, follow these steps:

1. Ensure you have Python 3.6 or higher installed on your system.
2. pip install taskwizard
3. If you cloned the repository already : pip install .
4. run 'taskwizard'

## Usage

After installation, you can start TaskWizard by running:

### Available Commands

- `help`: Display a list of available commands
- `add`: Add a new task
- `list`: Display all tasks
- `get`: Retrieve details of a specific task
- `edit`: Modify an existing task
- `delete`: Remove a task
- `clear`: Clear the screen (functionality not implemented in the provided code)
- `exit`: Exit the application

### Adding a Task

To add a new task, use the `add` command and follow the prompts:

1. Enter a unique name for the task
2. Provide a due date in the format MM/DD/YYYY HH:MM(am/pm)
3. Select a priority (LOW, MEDIUM, HIGH)
4. Enter a description (optional)

### Get a Task

To see all the details of an existing task, use the `get` command and follow the prompts:

1. Enter an existing name for the task (They are case sensitive)

### Editing a Task

To edit a task, use the `edit` command:

1. Enter the name of the existing task
2. Follow the prompts to update the task details

### Deleting a Task

To delete a task, use the `delete` command and enter the name of the task you wish to remove.

## Note

- Task names are case-sensitive
- The application uses a local database file (`taskwizard.db`) to store tasks
