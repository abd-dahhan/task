from rest_framework import serializers
from .models import Job, Resume, Skill, EducationHistory

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["id", "title", "description", "resume"]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name", "skill_level"]

class EducationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationHistory
        fields = ["id", "name", "qualification"]



class ResumeSerializer(serializers.ModelSerializer):
    job_history = JobSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    education_history = EducationHistorySerializer(many=True, read_only=True)
    class Meta:
        model = Resume
        fields = ["id", "job_history", "name", "bio", "skills", "address", "education_history"]