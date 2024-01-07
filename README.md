# Blog-App


## Overview

Welcome to Flask-Bootstrap-blog-App! This project is a feature-rich web application built with Flask, SQLAlchemy, and Bootstrap. It provides a secure user authentication system, a dynamic dashboard for post management, and a visually appealing user interface.

## Technologies Used

- **Backend:**
  - [Flask](https://flask.palletsprojects.com/): A Python web framework.
  - [SQLAlchemy](https://www.sqlalchemy.org/): A SQL toolkit and Object-Relational Mapping (ORM) library.

- **Frontend:**
  - [Bootstrap](https://getbootstrap.com/): A popular CSS framework for responsive and modern web design.

## Key Features

### User Authentication:

- **Secure Registration:** Users can register and create accounts securely.
- **Password Hashing:** Passwords are hashed using Werkzeug's security functions.
- **Login Functionality:** Implemented login functionality with session management to keep users authenticated.

### Dashboard:

- **User-Centric Dashboard:** Upon login, users are directed to a dashboard.
- **Post Creation:** Users can create new posts with a title and content.
- **Post Display:** Each post on the dashboard includes a title, content, and the username of the author.

### Post Management:

- **Post Creation:** Users can create new posts with a title and content.
- **Post Deletion:** Posts are displayed on the dashboard with options to delete them. Users can only delete their own posts.

### Styling with Bootstrap:

- **Modern Design:** The project's UI is enhanced with Bootstrap, providing a clean and modern design.
- **Responsive Design:** Bootstrap's responsive design ensures a seamless experience across various devices.

## Code Structure

- **Backend Structure:** The backend is structured using Flask, with a SQLAlchemy model for user information and posts.
- **Frontend Templates:** Frontend templates are rendered using Jinja2.
- **MVC Pattern:** The overall structure follows a Model-View-Controller (MVC) pattern.

