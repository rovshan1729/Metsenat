from django.urls import path
from . import views

urlpatterns = [
    #LOGIN PATH
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    #DASHBOARD PATH
    path('dashboard/',views.DashboardListCreateAPIView.as_view(), name='dashboard'),
    path('dashboard/<pk>/', views.DashboardRetrieveUpdateDestroyAPIView.as_view(), name='dashboard-RUD'),
    #SPONSORSHIP PATH
    path('sponsors/',views.SponsorsListCreateAPIView.as_view(), name='sponsor-LC'),
    path('sponsors/<pk>/',views.SponsorsRetrieveUpdateDestroyAPIView.as_view(), name='sponsor-RUD'),
    #SPONSOR'S FILTER PATH
    path('sponsor-filter/',views.SponsorsFilterListCreateAPIView.as_view(), name='sponsor-filter-LC'),
    path('sponsor-filter/<pk>',views.SponsorsFilterRetrieveUpdateDestroyAPIView.as_view(), name='sponsor-filter-RUD'),
    #ABOUT SPONSOR PATH
    path('about-sponsor/', views.AboutSponsorListCreateAPIView.as_view(), name='about-sponsor-LC'),
    path('about-sponsor/<pk>/', views.AboutSponsorRetrieveUpdateDestroy.as_view(), name='about-sponsor-RUD'),
    #EDITING INDIVIDUAL PATH
    path('edit-individual/', views.EditingIndividualListCreateAPIView.as_view(), name='edit-individual-LC'),
    path('edit-individual/<pk>/', views.EditingIndividualRetrieveUpdateDestroyAPIView.as_view(), name='edit-individual-RUD'),
    #EDITING LEGAL ENTITY PATH
    path('edit-legal-entity/', views.EditingLegalEntityListCreateAPIView.as_view(), name='edit-legal-entity-LC'),
    path('edit-legal-entity/<pk>/', views.EditingLegalEntityRetrieveUpdateDestroyAPIView.as_view(), name='edit-legal-entity-RUD'),
    #STUDENTS PATH
    path('students/', views.StudentListCreateAPIView.as_view(), name='student-LC'),
    path('student/<pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-RUD'),
    #STUDENT'S FILTER PATH
    path('student-filter/', views.StudentFilterListCreateAPIView.as_view(), name='student-filter-LC'),
    path('student-filter/<pk>/', views.StudentFilterRetrieveUpdateDestroyAPIView.as_view(), name='student-filter-RUD'),
    #ADD STUDENT PATH
    path('add-student/', views.AddStudentListCreateAPIView.as_view(), name='add-student-LC'),
    path('add-student/<pk>/', views.AddStudentRetrieveUpdateDestroyAPIView.as_view(), name='add-student-RUD'),
    #ABOUT STUDENT PATH
    path('about-student/', views.AboutStudentListCreateAPIView.as_view(), name='about-student-LC'),
    path('about-student/<pk>/', views.AboutStudentRetrieveUpdateDestroyAPIView.as_view(), name='about-student-RUD'),
    #EDIT STUDENT PATH
    path('edit-student/', views.EditStudentListCreateAPIView.as_view(), name='edit-student-LC'),
    path('edit-student/<pk>/', views.EditStudentRetrieveUpdateDestroyAPIView.as_view(), name='edit-student-RUD'),
    #EDIT SPONSOR PATH
    path('edit-sponsor/', views.EditSponsorListCreateAPIView.as_view(), name='edit-sponsor-LC'),
    path('edit-sponsor/<pk>/', views.EditSponsorRetrieveUpdateDestroyAPIView.as_view(), name='edit-sponsor-RUD'),
    #ADD SPONSOR PATH
    path('add-sponsor/', views.AddSponsorListCreateAPIView.as_view(), name='add-sponsor-LC'),
    path('add-sponsor/<pk>/', views.AddStudentRetrieveUpdateDestroyAPIView.as_view(), name='add-sponsor-RUD'),
]