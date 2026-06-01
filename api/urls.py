from django.urls import path

from .views import (
    home,
    students,
    teachers,
    course,
    add_student,
    products,
    ProductAPIView,
    ProductDetailAPIView,
    DashboardAPIView,
    ProfileAPIView,
    ReportAPIView,
    UploadProfileAPIView,
    UploadResumeAPIView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('', home),

    path('students/', students),

    path('teachers/', teachers),

    path('course/', course),

    path('add-student/', add_student),

    # FUNCTION BASED
    # path('products/', products),

    # CLASS BASED
    path(
        'products/',
        ProductAPIView.as_view()
    ),

    path(
        'products/<int:id>/',
        ProductDetailAPIView.as_view()
    ),

    # JWT TOKEN
    path(
        'token/',
        TokenObtainPairView.as_view()
    ),

    path(
        'token/refresh/',
        TokenRefreshView.as_view()
    ),

    # DASHBOARD
    path(
        'dashboard/',
        DashboardAPIView.as_view()
    ),

    # PROFILE
    path(
        'profile/',
        ProfileAPIView.as_view()
    ),

    # REPORT
    path(
        'upload-report/',
        ReportAPIView.as_view()
    ),

    # UPLOAD PROFILE
    path(
        'upload-profile/',
        UploadProfileAPIView.as_view()
    ),

    # UPLOAD RESUME
    path(
        'upload-resume/',
        UploadResumeAPIView.as_view()
    ),

]