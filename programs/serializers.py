from django.core import serializers
import json


def ignore_blank_fields(data):
    item = {}
    for key, value in data.items():
        if value:
            item[key.replace('_', ' ').title()] = value
    
    return item


def program_serializer(model_instance):
    serialized_item = serializers.serialize('json', [model_instance])
    data = json.loads(serialized_item)[0]['fields']
    item = ignore_blank_fields(data)
    return item
