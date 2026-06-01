from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import (
    Product,
    Report,
    Profile,
    Resume
)

from .serializers import (
    StudentSerializer,
    ProductSerializer,
    ReportSerializer,
    ProfileSerializer,
    ResumeSerializer
)


# ---------------- HOME API ----------------

@api_view(['GET'])
def home(request):

    return Response({
        "message": "welcome to DRF",
        "status": "Python Full Stack"
    })


# ---------------- STUDENTS API ----------------

@api_view(['GET'])
def students(request):

    data = [
        {"id": 1, "name": "Rahul", "course": "MERN"},
        {"id": 2, "name": "ANU", "course": "PYTHON"}
    ]

    return Response(data)


# ---------------- TEACHERS API ----------------

@api_view(['GET'])
def teachers(request):

    data = [
        {"name": "Arjun", "course": "Python"},
        {"name": "Nimal", "course": "React"}
    ]

    return Response(data)


# ---------------- COURSE API ----------------

@api_view(['GET'])
def course(request):

    data = [
        {
            "course_name": "Python Full Stack",
            "duration": "6 Months"
        },
        {
            "course_name": "MERN Stack",
            "duration": "5 Months"
        }
    ]

    return Response(data)


# ---------------- ADD STUDENT API ----------------

@api_view(['POST'])
def add_student(request):

    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

        return Response({
            "message": "Student Added Successfully"
        })

    return Response(serializer.errors)


# ---------------- FUNCTION BASED PRODUCT API ----------------

@api_view(['GET', 'POST'])
def products(request):

    # GET PRODUCTS
    if request.method == 'GET':

        products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    # ADD PRODUCT
    elif request.method == 'POST':

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({
                "message": "Product Added Successfully"
            })

        return Response(serializer.errors)


# ---------------- PRODUCT API VIEW ----------------

class ProductAPIView(APIView):

    # GET ALL PRODUCTS
    def get(self, request):

        products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    # ADD PRODUCT
    def post(self, request):

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({
                "message": "Product Added Successfully"
            })

        return Response(serializer.errors)


# ---------------- PRODUCT DETAIL API VIEW ----------------

class ProductDetailAPIView(APIView):

    # GET SINGLE PRODUCT
    def get(self, request, id):

        product = get_object_or_404(Product, id=id)

        serializer = ProductSerializer(product)

        return Response(serializer.data)

    # UPDATE PRODUCT
    def put(self, request, id):

        product = get_object_or_404(Product, id=id)

        serializer = ProductSerializer(
            product,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response({
                "message": "Product Updated Successfully"
            })

        return Response(serializer.errors)

    # DELETE PRODUCT
    def delete(self, request, id):

        product = get_object_or_404(Product, id=id)

        product.delete()

        return Response({
            "message": "Product Deleted Successfully"
        })


# ---------------- DASHBOARD API VIEW ----------------

class DashboardAPIView(APIView):

    def get(self, request):

        data = {
            "message": "Welcome to Dashboard"
        }

        return Response(data)


# ---------------- PROFILE API VIEW ----------------

class ProfileAPIView(APIView):

    def get(self, request):

        data = {
            "message": "Welcome to Profile API"
        }

        return Response(data)


# ---------------- REPORT API VIEW ----------------

class ReportAPIView(APIView):

    # GET REPORTS
    def get(self, request):

        reports = Report.objects.all()

        serializer = ReportSerializer(
            reports,
            many=True
        )

        return Response(serializer.data)

    # ADD REPORT
    def post(self, request):

        serializer = ReportSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response({
                "message": "Report Uploaded Successfully"
            })

        return Response(serializer.errors)


# ---------------- UPLOAD PROFILE API VIEW ----------------

class UploadProfileAPIView(APIView):

    # GET PROFILES
    def get(self, request):

        profiles = Profile.objects.all()

        serializer = ProfileSerializer(
            profiles,
            many=True
        )

        return Response(serializer.data)

    # ADD PROFILE
    def post(self, request):

        serializer = ProfileSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response({
                "message": "Profile Uploaded Successfully"
            })

        return Response(serializer.errors)


# ---------------- UPLOAD RESUME API VIEW ----------------

class UploadResumeAPIView(APIView):

    # GET RESUMES
    def get(self, request):

        resumes = Resume.objects.all()

        serializer = ResumeSerializer(
            resumes,
            many=True
        )

        return Response(serializer.data)

    # ADD RESUME
    def post(self, request):

        serializer = ResumeSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response({
                "message": "Resume Uploaded Successfully"
            })

        return Response(serializer.errors)