from rest_framework import serializers
from .models import Student, Parent, Teacher, SchoolClass, ReferalSource


class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parent
        fields = [ 'first_name', 'last_name', 'email', 'username', 'phone', 'is_verified', 'referal_source']

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parent
        fields = [ 'first_name', 'last_name', 'email', 'username', 'phone', 'is_verified', 'referal_source']
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parent
        fields = [ 'first_name', 'last_name', 'username', 'is_verified', 'referal_source']