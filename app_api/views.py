from rest_framework.views import APIView
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

#get all details 
class StudentDetails(APIView):
    def get(self, request):
        all_details = Student.objects.all()
        serializer = StudentSerializer(all_details, many=True)
        # json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data, content_type="application/json")
        return JsonResponse({'data':serializer.data})
    

#get detail of single student    
class StudentDetail(APIView):
    def get(self, request,pk):
        all_detail = Student.objects.get(id=pk)
        serializer = StudentSerializer(all_detail)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")
    

class CreateDetails(APIView):
    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data created"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class CreateDetail(APIView):
    def post(self, request):
        user_data = {"name": "dk", "email": "e1@gmail.com","roll_num":"-5","subject":"eng","address":"ui"}
        serializer = StudentSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data created"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CreateBulkDetails(APIView):
    def post(self, request):
        bulk_data = [
            {'name': 'ankit', 'email': 'ankit@gmail.com', 'roll_num': '1', 'subject': 'Math', 'address': '123 Street'},
            {'name': 'avii', 'email': 'avii@gmail.com', 'roll_num': '2', 'subject': 'Science', 'address': '456 Avenue'},
        ]
        serializer = StudentSerializer(data=bulk_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Bulk data created"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Updatedata(APIView):
     def put(self, request,pk):
        student_instance = Student.objects.get(id=pk)
        user_data = {'name': "dk", 'email': "email@gmail.com","roll_num":"5","subject":"eng","address":"ui"}
        serializer = StudentSerializer(student_instance,data=user_data)
        # serializer = StudentSerializer(student_instance,data=request.data)# from serializers file
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class DeleteStudent(APIView):
    def delete(self, request, pk):
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({"msg": "Student does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        student.delete()
        return Response({"msg": "Student deleted successfully"})