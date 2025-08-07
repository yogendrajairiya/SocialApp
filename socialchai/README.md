# Social Chai

Social Chai is a feature-rich, Twitter-like social media application built with Django. It allows users to create accounts, post tweets with text and images, interact with other users' content, and manage their own profiles.

## Features

*   **User Authentication:** A complete user authentication system allowing users to register for a new account, log in, and log out.
*   **Tweet Management:**
    *   **Create:** Users can create new tweets, which can include up to 240 characters of text and an optional image.
    *   **Read:** The main feed displays all tweets in reverse chronological order.
    *   **Update:** Users can edit their own tweets after they have been posted.
    *   **Delete:** Users have the ability to delete their own tweets.
*   **User Profiles:**
    *   Each user has a customizable profile with a profile photo, bio, location, birthdate, and more.
    *   Tweets are clearly associated with the user who created them, and clicking on a username takes you to their profile page.
*   **Social Interaction:**
    *   **Liking:** Users can like and unlike tweets.
    *   **Commenting:** Users can comment on tweets, creating conversation threads.
*   **User-Specific Feeds:** In addition to the main feed, users can view a feed of tweets from a specific user.

## Technology Stack

*   **Backend:** Django
*   **Frontend:** HTML, CSS (via Django Templates)
*   **Database:** SQLite (default)
*   **Dependencies:**
    *   asgiref
    *   Pillow
    *   sqlparse

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   Python 3.x
*   pip

### Installation

1.  **Clone the repo:**
    ```sh
    git clone https://github.com/your_username/your_project_name.git
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd your_project_name
    ```
3.  **Install Python packages:**
    ```sh
    pip install -r requirements.txt
    ```
4.  **Apply database migrations:**
    ```sh
    python manage.py migrate
    ```
5.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```
6.  **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000/`

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request
