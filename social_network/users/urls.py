from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterUser, ProfileView, AddFriend, FriendshipGraph  # Import the necessary views

urlpatterns = [
    # JWT Token Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # User Registration
    path('', RegisterUser.as_view(), name='register_user'),

    # Profile Management
    path('profile/', ProfileView.as_view(), name='profile'),

    # Friend Management
    path('add_friend/', AddFriend.as_view(), name='add_friend'),

    # Friendship Graph
    path('friendship_graph/', FriendshipGraph.as_view(), name='friendship_graph'),
]
