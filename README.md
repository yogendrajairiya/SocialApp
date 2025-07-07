# Social Chai

A simple, yet full-featured, Twitter-like social media application built with Django. This project allows users to create accounts, post tweets with text and images, and manage their own content.

## Features

*   **User Authentication:** A complete user authentication system allowing users to register for a new account, log in, and log out.
*   **Tweet Management:**
    *   **Create:** Users can create new tweets, which can include up to 240 characters of text and an optional image.
    *   **Read:** The main feed displays all tweets in reverse chronological order.
    *   **Update:** Users can edit their own tweets after they have been posted.
    *   **Delete:** Users have the ability to delete their own tweets.
*   **User Profiles:** Every tweet is clearly associated with the user who created it, forming an implicit user profile.

## Technology Stack

*   **Backend:** Django
*   **Frontend:** HTML, CSS (via Django Templates)
*   **Database:** SQLite (default)
*   **Dependencies:**
    *   `asgiref`
    *   `Pillow`
    *   `sqlparse`

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   Python 3.x
*   pip

### Installation

1.  **Clone the repo**
    ```sh
    git clone https://github.com/your_username/your_project_name.git
    ```
2.  **Navigate to the project directory**
    ```sh
    cd your_project_name
    ```
3.  **Install Python packages**
    ```sh
    pip install -r requirements.txt
    ```
4.  **Apply database migrations**
    ```sh
    python socialchai/manage.py migrate
    ```
5.  **Run the development server**
    ```sh
    python socialchai/manage.py runserver
    ```
6.  **Access the application**
    Open your web browser and go to `http://127.0.0.1:8000/`
