from rest_framework import serializers

from academics.models.subject import Subject
from academics.models.subject_enrolled import SubjectEnrolled
from users.models import User,Teacher


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name')  # replace 'name' with the actual field name for user's name

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = ('id', 'user')


class SubjectSerializerList(serializers.ModelSerializer):
        teacher_id = TeacherSerializer(read_only=True)

        class Meta:
            model = Subject
            fields = ["id", "sub_title", "sub_description", "sub_code","teacher_id","updated_at","created_at"]
            
class ListEnrollmentSerializer(serializers.ModelSerializer):
    subject_title = serializers.CharField(source='sub_id.sub_title', read_only=True)
    subject_description = serializers.CharField(source='sub_id.sub_description', read_only=True)
    teacher_name = serializers.CharField(source='sub_id.teacher_id.user.name', read_only=True)
    sub_id = serializers.IntegerField(source='sub_id.id', read_only=True)

    class Meta:
        model = SubjectEnrolled
        fields = ('id', 'sub_id', 'subject_title', 'subject_description', 'teacher_name', 'joined_at')
        extra_kwargs = {
            'id': {'read_only': True, 'label': 'enrollment_id'},
        }
        