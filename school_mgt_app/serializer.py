from rest_framework import serializers

from school_mgt_app.models import SchoolAdmin


class SchoolAdminSerializer(serializers.ModelSerializer):
    class meta:
        model = SchoolAdmin
        fields = ['first_name', 'last_name', 'email']