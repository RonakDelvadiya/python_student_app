from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from student_app.serializers import *
from django.views.decorators.csrf import csrf_exempt
from student_app.models import *

@csrf_exempt
@api_view(['POST'])
def school_create(request):
	serializer = SchoolSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
def school_list(request):
	schools = School.objects.filter(is_active=True)
	serializer = SchoolListSerializer(schools, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
def student_list(request):
	students = Students.objects.filter(is_active=True)
	serializer = StudentsListSerializer(students, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
def post_details(request, pk):
	try:
		post = Post.objects.get(id=pk)
	except:
		return Response({'error': 'Post id not found'}, status=status.HTTP_400_BAD_REQUEST)

	serializer = PostListSerializer(post, many=False)
	return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['PUT'])
def school_update(request, pk):
	try:
		school = School.objects.get(id=pk)
	except:
		return Response({'error': 'School id not found'}, status=status.HTTP_400_BAD_REQUEST)

	serializer = SchoolListSerializer(school, data=request.data, patch=True, many=False)

	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['PUT'])
def school_update(request, pk):
	try:
		school = School.objects.get(id=pk)
	except:
		return Response({'error': 'School id not found'}, status=status.HTTP_400_BAD_REQUEST)

	serializer = SchoolListSerializer(school, data=request.data, patch=True, many=False)

	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['DELETE'])
def post_delete(request, pk):
	try:
		post = Post.objects.get(id=pk)
	except:
		return Response({'error': 'Post id not found'}, status=status.HTTP_400_BAD_REQUEST)
	post.delete()
	return Response({'success': 'Post deleted successfully'}, status=status.HTTP_200_OK)
