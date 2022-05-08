from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from maintenance.models import *
from .utils import render_to_pdf 

# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         tasks = maintenance.objects.filter(technicalrecorder=request.user).order_by('-date')
#         user = request.user
#         data = {
#             'tasks':tasks,
#             'user':user
#         }
#         pdf = render_to_pdf('task/page.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')

def printPdf(request,id):
    user = get_object_or_404(User,id=id)
    tasks = maintenance.objects.filter(technicalrecorder=user).order_by('-date')
    data = {
        'tasks':tasks,
        'user':user,
    }
    pdf = render_to_pdf('task/page.html',data)
    return HttpResponse(pdf, content_type='application/pdf')