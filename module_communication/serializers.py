from rest_framework import serializers

from module_communication.models import *

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventParticipateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventParticipate
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class DiscussionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionGroup
        fields = '__all__'

class GroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessage
        fields = '__all__'



class GroupMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMedia
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'



class StudentDiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDiscussion
        fields = '__all__'



class StudentDiscussionMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDiscussionMedia
        fields = '__all__'