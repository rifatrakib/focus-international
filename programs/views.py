from django.shortcuts import render
from programs.models import Program


def get_programs(request):
    programs = Program.objects.all()
    context = {'programs': programs}
    return render(request, 'programs/programs-summary.html', context)
