from django.contrib import admin

from django.urls import path

from apis import views

urlpatterns = [

    path('test-endpoint-events/', views.TestEndPointEvents.as_view()),

    path('test-endpoint/', views.TestEndPoint.as_view()),

    path('add-model-regression-logistic/',views.AddModelRegressionLogistic.as_view()),

    path('get-reports/', views.GetReports.as_view()),

    path('test-iq/', views.TestIq.as_view()),

    path('test-mail-smtp/', views.TestMailSmtp.as_view()),

    path('get-data-analysis-iqoption/', views.GetDataAnalysisIqOption.as_view()),

    path('get-data-analysis-iqoption-clean/', views.GetDataAnalysisIqOptionClean.as_view()),

    path('get-data-analysis-iqoption-clean-another/', views.GetDataAnalysisIqOptionCleanAnother.as_view()),

    path('get-now-manager/', views.NowManager.as_view())

]