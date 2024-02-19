from django.urls import path
from api.views.views import AssessmentList, FinancialCommitmentList, SchedulesList, StudentSchoolCareer, eBookList, InvoiceList, InformationList, EventList


urlpatterns = [
    path('schedules/', SchedulesList.as_view(), name='schedule-list'),
    path('assessments/', AssessmentList.as_view(), name='assessment-list'),
    path('invoices/', InvoiceList.as_view(), name='invoice-list'),
    path('ebooks/', eBookList.as_view(), name='ebook-list'),
    path('informations/', InformationList.as_view(), name='informations-list'),
    path('events/', EventList.as_view(), name='events-list'),
    path('engagements/', FinancialCommitmentList.as_view(), name='engagements-list'),
    path('parcours/', StudentSchoolCareer.as_view()),
]