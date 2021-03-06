from rest_framework import serializers
from api.models import Answer, Survey, JournalStub
from django.contrib.auth.models import User


class AnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["user", "survey", "question_ordinal", "answer", "timestamp"]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["question_ordinal", "answer", "timestamp"]


class SurveyListSerializer(serializers.ModelSerializer):
    answers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Survey
        fields = ["user", "ordinal", "timestamp", "answers"]


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class UserSerializer(serializers.ModelSerializer):
    answers = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ["username", "answers"]

class JournalStubSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JournalStub
        fields = [
            "title",
            "authors_date",
            "relevant_questions",
            "summary",
            "subject_group",
            "other_findings",
            "task_mindfullness",
            "task_wellness",
            "task_clinical",
        ]
