from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .tokens import create_jwt_pair_for_user


    
    

@api_view(['POST'])
def login(request):
    #you are getting the user's details
    username=request.data.get('username')
    password=request.data.get('password')
    # you are checking if the username matches with the one already created
    user=get_object_or_404(User, username=username)
    #checking if the password matches
    if not user.check_password(request.data['password']):
        return Response({"detail": "Invalid Credentials"},status=status.HTTP_404_NOT_FOUND)
    # token,created=Token.objects.get_or_create(user=user)-----This is for normal Token authentiation
    #you are creating refresh and access tokens for the user
    tokens=create_jwt_pair_for_user(user)
    serializer=UserSerializer(instance=user, context={"request":request})
    
    return Response({"token":tokens, "user":serializer.data})



@api_view(['POST'])
def signup(request):
    # you are serializing data being sent as a request
    serializer=UserSerializer(data=request.data)
    #checking if the serializer data is valid
    if serializer.is_valid():
        serializer.save()
        #you are collecting the data passed into the username field
        user=User.objects.get(username=request.data['username'])
        # you are setting and hashing the password
        user.set_password(request.data['password'])
        user.save()
        token=Token.objects.create(user=user)
        return Response({'token': token.key, 'user':serializer.data},status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed for {}". format(request.user.email))

