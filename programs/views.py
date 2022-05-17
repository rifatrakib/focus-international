from django.shortcuts import render, get_object_or_404
from programs.models import Program
from programs.serializers import program_serializer


def get_programs_summary(request):
    programs = Program.objects.all().order_by('id')
    context = {'programs': programs, 'count': len(programs)}
    return render(request, 'programs/programs-summary.html', context)


def get_program_details(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    item = program_serializer(program)
    context = {'program': item}
    return render(request, 'programs/program-details.html', context)
