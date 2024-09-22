from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import UserSerializer, ProfileSerializer
from .models import Profile, Friend
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import networkx as nx
from PIL import Image

# Create your views here.

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Create profile after user registration
            Profile.objects.create(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile

    def perform_update(self, serializer):
        profile = serializer.save()
        if profile.profile_picture:
            # Open and resize the image
            img = Image.open(profile.profile_picture)
            img = img.resize((300, 300))
            # Save the resized image
            img.save(profile.profile_picture.path)


class AddFriend(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Retrieve the user to add as a friend
        user_to = get_object_or_404(User, id=request.data.get('user_to_id'))
        
        # Check if friendship already exists (in both directions)
        if Friend.objects.filter(user_from=request.user, user_to=user_to).exists() or \
           Friend.objects.filter(user_from=user_to, user_to=request.user).exists():
            return Response({"message": "Friendship already exists"}, status=status.HTTP_400_BAD_REQUEST)

        # Create friendship
        Friend.objects.create(user_from=request.user, user_to=user_to)
        return Response({"message": "Friend request sent"}, status=status.HTTP_201_CREATED)


class FriendshipGraph(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve all friends where the current user is the source
        friends = Friend.objects.filter(user_from=request.user)
        
        # Create a graph using networkx
        G = nx.Graph()

        for friend in friends:
            # Add edges between the user and their friends
            G.add_edge(request.user.username, friend.user_to.username)
        
        # Convert graph edges to a list of tuples
        graph_data = list(G.edges())
        
        # Return the friendship graph data as a response
        return Response({"graph": graph_data}, status=status.HTTP_200_OK)
