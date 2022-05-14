from django.shortcuts import render
from programs.models import Program


def get_programs_summary(request):
    programs = Program.objects.all()
    context = {'programs': programs}
    return render(request, 'programs/programs-summary.html', context)


def get_program_details(request, program_id):
    program = Program.objects.get(pk=program_id)
    context = {'program': program}
    return render(request, 'programs/program-details.html', context)
