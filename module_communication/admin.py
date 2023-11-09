from django.contrib import admin

from module_communication.models import Contact, DiscussionGroup, Event, EventParticipate, Group, GroupMedia, GroupMessage, Information, StudentDiscussion, StudentDiscussionMedia

# Register your models here.
admin.site.register(Information)
admin.site.register(Event)
admin.site.register(EventParticipate)
admin.site.register(Group)
admin.site.register(DiscussionGroup)
admin.site.register(GroupMessage)
admin.site.register(GroupMedia)
admin.site.register(Contact)
admin.site.register(StudentDiscussion)
admin.site.register(StudentDiscussionMedia)