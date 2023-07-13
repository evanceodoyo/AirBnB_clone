# AirBnB Clone
![AirBnB Clone Screenshot](./airbnb_clone.png)

This project is a simplified clone of the popular website AirBnB. It aims to replicate some of the core functionality of AirBnB, allowing users to create, manage, and book accommodations.

## Command Interpreter
The command interpreter is a command-line interface (CLI) that allows users to interact with the AirBnB clone application. It provides a set of commands to perform various actions, such as creating objects, updating data, and displaying information.

### How to Start the Command Interpreter
To start and run the command interpreter:
   ```shell
   ./console.py
   ```

### How to Use the Command Interpreter
Once the command interpreter is running, you can use the following commands to interact with the application:

- **help**: list all commands.
   ```shell
   Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update
   ```
- **help <command>**: Help on a specific command.
   ```shell
   (hbnb) help <command>
   ```

- **create**: Create a new object instance (e.g., a new user or a new place).
   ```shell
   (hbnb) create <class_name>
   ```

- **show**: Display information about a specific object.
   ```shell
   (hbnb) show <class_name> <object_id>
   ```

- **all**: Display information about all objects or all objects of a specific class.
   ```shell
   (hbnb) all
   (hbnb) all <class_name>
   ```

- **update**: Update attributes of an object.
   ```shell
   (hbnb) update <class_name> <object_id> <attribute_name> "<attribute_value>"
   ```

- **destroy**: Delete an object.
   ```shell
   (hbnb) destroy <class_name> <object_id>
   ```

- **quit**: Exit the command interpreter.
   ```shell
   (hbnb) quit
   ```

### Examples
Here are some examples of how to use the command interpreter:
- Help on a specific command:
  ```shell
  (hbnb) help create
  Creates a new instance of a class, saves it (to the JSON file) and prints the id.
  
  Args:
    arg (str): Argument to enter with command: <class_name>
    Example: create User
  ```
- Create a new user:
  ```shell
  (hbnb) create User
  c6621392-cefe-4c86-b85b-09c171b749f4
  ```

- Display information about a place with ID `c6621392-cefe-4c86-b85b-09c171b749f4`:
  ```shell
  (hbnb) show User c6621392-cefe-4c86-b85b-09c171b749f4
  [User] (c6621392-cefe-4c86-b85b-09c171b749f4) {'id': 'c6621392-cefe-4c86-b85b-09c171b749f4', 'created_at': datetime.datetime(2023, 7, 13, 17, 52, 51, 232830), 'updated_at': datetime.datetime(2023, 7, 13, 17, 52, 51, 232948)}
  ```

- Display information about all objects of the Place class:
  ```shell
  (hbnb) all User
  ["[User] (c6621392-cefe-4c86-b85b-09c171b749f4) {'id': 'c6621392-cefe-4c86-b85b-09c171b749f4', 'created_at': datetime.datetime(2023, 7, 13, 17, 52, 51, 232830), 'updated_at': datetime.datetime(2023, 7, 13, 17, 52, 51, 232948)}"]
  ```

- Update the name attribute of a user with ID `c6621392-cefe-4c86-b85b-09c171b749f4`:
  ```shell
  (hbnb) update User  c6621392-cefe-4c86-b85b-09c171b749f4 name "John Doe"
  ```
  
- Confirm the name is changed
  ```shell
  (hbnb) show c6621392-cefe-4c86-b85b-09c171b749f4
  [User] (c6621392-cefe-4c86-b85b-09c171b749f4) {'id': 'c6621392-cefe-4c86-b85b-09c171b749f4', 'created_at': datetime.datetime(2023, 7, 13, 17, 52, 51, 232830), 'updated_at': datetime.datetime(2023, 7, 13, 17, 52, 51, 232948), 'name': 'John'}
  ```
- Delete a review with ID `c6621392-cefe-4c86-b85b-09c171b749f4`:
  ```shell
  (hbnb) destroy User c6621392-cefe-4c86-b85b-09c171b749f4
  (hbnb) all
  []
  ```
- To quit the command intepreter/console:
   ```shell
  (hbnb) quit
  ```
  or use `Ctrl + D`.