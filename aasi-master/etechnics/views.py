from django.http import HttpResponse
from django.views.generic import View
from maintenance.models import *
from .utils import render_to_pdf 

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        tasks = maintenance.objects.filter(technicalrecorder=request.user).order_by('-date')
        user = request.user
        data = {
            'tasks':tasks,
            'user':user
        }
        pdf = render_to_pdf('task/page.html', data)
        return HttpResponse(pdf, content_type='application/pdf')