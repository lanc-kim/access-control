# Python Access Control Script

A simple access control script that will allow access based on pre-determioned authorized users and their respective roles.

## About This Project

This project began as an exploration of conditional expressions but quickly evolved into my first real experience with functions and file handling. I implemented the `open` function to read from a `users.txt` file, enabling support for multiple users and roles. It led to a significant amount of trial and error, but overall I'm satisfied with its functionality.

# How To Use

Ensure that both `access-control.py` and `users.txt` are in the same directory. If they are not in the same location, the program will not function as intended.


## Technologies Used

- **Python 3.13.3**: The programming language used to implement the logic and conditionals.
- **PyCharm**: The Integrated Development Environment (IDE) used to write and debug the code.

## What I Learned

- **Conditional Expressions**: I learned how to use Python's conditional expressions (`X if condition else Y`) to make concise decisions based on user input, such as verifying roles and PINs.
- **File Handling**: I gained experience in reading from a file using the `open()` function, allowing me to check usernames and roles in a `users.txt` file.
- **Functions**: I practiced organizing the code into functions (like `get_users_from_file()`) to improve code modularity and reuse.
- **Error Handling**: I learned how to handle potential errors, such as missing files and invalid input, to improve the robustness of the program.


## Next Steps

- **Refactor the program** to improve security, such as replacing the hardcoded PIN with a more secure, dynamic authentication method (e.g., hashed passwords or integrating an authentication service).
- **Extend functionality** by allowing users to modify their credentials or add new users to the `users.txt` file dynamically.
- **Improve error handling** to provide more detailed feedback for the user, such as specific error messages for invalid input or file-related issues.
- **Explore a graphical user interface (GUI)** using a library like `Tkinter` or a web-based interface using frameworks like `Flask` or `Django`.

---
