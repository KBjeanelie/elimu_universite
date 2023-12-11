from rest_framework import viewsets
from module_communication.models import *
from module_communication.serializers import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import *


class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def participants_count(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    participants_count = EventParticipate.objects.filter(event=event).count()
    return JsonResponse({'participants_count': participants_count})

def participate_event(request, event_id, student_id, start_hours, end_hours, amount):
    event_participation = EventParticipate.objects.create(
        event_id=event_id,
        student_id=student_id,
        start_hours=start_hours,
        end_hours=end_hours,
        amount=amount
    )
    return JsonResponse({'message': 'Student successfully registered for the event' , 'event_participation':event_participation})


def last_discussion_message(request, sender_id, receiver_id):
    discussion = StudentDiscussion.objects.filter(sender_id=sender_id, receiver_id=receiver_id).last()
    if discussion:
        return JsonResponse({'last_message': discussion.content})
    else:
        return JsonResponse({'last_message': 'No messages found'})
    
def last_group_message(request, student_id, group_id):
    group = get_object_or_404(DiscussionGroup, id=group_id, student_id=student_id)
    last_message = GroupMessage.objects.filter(discussion_group=group).last()
    if last_message:
        return JsonResponse({'last_message': last_message.content})
    else:
        return JsonResponse({'last_message': 'No messages found in the group'})
    


def all_group_messages(request, student_id): 
    current_group = get_object_or_404(Group, student_id=student_id)
    group_messages = GroupMessage.objects.filter(discussion_group__group=current_group)
    
    messages_list = [{'content': message.content, 'created_at': message.created_at} for message in group_messages]
    
    return JsonResponse({'group_messages': messages_list})


def all_student_messages(request, sender_id, receiver_id):
    discussions = StudentDiscussion.objects.filter(sender_id=sender_id, receiver_id=receiver_id) | \
                   StudentDiscussion.objects.filter(sender_id=receiver_id, receiver_id=sender_id)
    
    messages_list = [{'content': discussion.content, 'created_at': discussion.created_at} for discussion in discussions]
    
    return JsonResponse({'student_messages': messages_list})



def all_users(request):
    all_users = Student.objects.all()
    
    users_list = [{'username': user.username, 'email': user.email} for user in all_users]
    
    return JsonResponse({'users': users_list})