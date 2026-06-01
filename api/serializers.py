from rest_framework import serializers

from .models import (
    Student,
    Product,
    Report,
    Profile,
    Resume
)


# ---------------- STUDENT SERIALIZER ----------------

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


# ---------------- PRODUCT SERIALIZER ----------------

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


# ---------------- REPORT SERIALIZER ----------------

class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = '__all__'

    def validate_image(self, value):

        allowed_extensions = ['jpg', 'jpeg', 'png']

        extension = value.name.split('.')[-1].lower()

        if extension not in allowed_extensions:

            raise serializers.ValidationError(
                "Only JPG, JPEG and PNG files allowed"
            )

        if value.size > 2 * 1024 * 1024:

            raise serializers.ValidationError(
                "Image size should be below 2MB"
            )

        return value

    def validate_pdf(self, value):

        extension = value.name.split('.')[-1].lower()

        if extension != 'pdf':

            raise serializers.ValidationError(
                "Only PDF file allowed"
            )

        return value


# ---------------- PROFILE SERIALIZER ----------------

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

    def validate_profile_image(self, value):

        allowed_extensions = ['jpg', 'jpeg', 'png']

        extension = value.name.split('.')[-1].lower()

        if extension not in allowed_extensions:

            raise serializers.ValidationError(
                "Only JPG, JPEG and PNG files allowed"
            )

        if value.size > 1 * 1024 * 1024:

            raise serializers.ValidationError(
                "Image size should be below 1MB"
            )

        return value


# ---------------- RESUME SERIALIZER ----------------

class ResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume
        fields = '__all__'

    def validate_resume_pdf(self, value):

        extension = value.name.split('.')[-1].lower()

        if extension != 'pdf':

            raise serializers.ValidationError(
                "Only PDF file allowed"
            )

        return value