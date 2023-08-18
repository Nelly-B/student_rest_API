from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework import status
from .serializers import StudentSerializer
from . models import Student


# Create your views here.
@api_view(['GET','POST'])
def home(request:Request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        response = {
            'message':'God is good ooooo hmmmmmmmmm',
            'students': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            response = {'data': serializer.data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    
@api_view(['GET','PUT'])
def list_details(request:Request, id):
    student = get_object_or_404(Student,pk=id)
    if request.method == 'GET':
        serializer =StudentSerializer(instance=student, many=False)
        response = {
            'student': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializerput = StudentSerializer(instance=student, data=request.data, many=False)
        if serializerput.is_valid():
            serializerput.save()
            response = {
                'student':serializerput.data
            }
            return Response(response, status=status.HTTP_200_OK)     
    
@api_view(['GET','DESTROY'])
def delete(request:Request,id):
    student = Student.objects.get(pk=id)
    serializerdelete = StudentSerializer(instance=student, many=False)
    
    response = {
        "student": serializerdelete.data
    }
    return Response(response, status=status.HTTP_200_OK)



