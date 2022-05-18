from django.core import serializers
import json


def process_item_data(data):
    item = {}
    listed_fields = {'academic_history', 'advantages', 'scholarships', 'institutions'}
    
    for key, value in data.items():
        field_name = key.replace('_', ' ').title()
        if value:
            if key in listed_fields:
                item[field_name] = value.split('|')
            else:
                item[field_name] = value
    
    return item


def program_serializer(model_instance):
    serialized_item = serializers.serialize('json', [model_instance])
    data = json.loads(serialized_item)[0]['fields']
    item = process_item_data(data)
    return item
