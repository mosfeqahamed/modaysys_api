
Here’s a sample README.md file for your project that you can use on GitHub:

Mondaysys API (Django Social Network API)
This project is a social networking API built with Django and Django REST Framework. It provides key social features such as user registration, JWT-based authentication, friend management, and visualizing friendship graphs.

Features
User Registration: Register new users with username, email, and password.
JWT Authentication: Secure login and token-based authentication using JSON Web Tokens.
Profile Management: Users can update their bio and profile picture.
Friend Management: Users can add friends, and friendships are validated to avoid duplicates.
Friendship Graph: Visualize the social connections using NetworkX.

Installation Steps

1.Clone the repository:

git clone https://github.com/mosfeqahamed/modaysys_api.git

cd modaysys_api

2. cd env/Scripts

3.Activate the activate.bat:
.\activate.bat

4.comming back to modaysys_api directory and write " cd social_network " to the terminal

5.Install dependencies: pip install -r requirements.txt

7.Set up the database: python manage.py migrate

8.Create a superuser to access the admin panel: python manage.py createsuperuser

9.Run the development server: python manage.py runserver

8.Access the application at http://127.0.0.1:8000/.


To check api:

POST http://127.0.0.1:8000: Register a new user.

Example payload:

{
    "username": "user1",
    "email": "user1@example.com",
    "password": "password123"
}

POST /token: Obtain JWT tokens (access and refresh)

Example payload:

{
    "username": "user1",
    "password": "password123"
}

POST /token/refresh: Refresh the access token.

Example payload:

{
    "refresh": "your_refresh_token"
}

GET /profile: View or update the user's profile (bio and profile picture)

POST /add_friend: Send a friend request by user ID

Example payload:

{
    "user_to_id": 2
}

GET /friendship_graph: Retrieve a friendship graph of the user’s social network.
