import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *


# class LuminaireModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class LuminaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Luminaire
        # fields = ('title', 'content', 'cat')
        fields = "__all__"

# def encode():
#     model = LuminaireModel('Versace Gold', 'content:Versace Mramor')
#     model_sr = LuminaireSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Versace Gold","content":"content:Versace Mramor"}')
#     data = JSONParser().parse(stream)
#     serializer = LuminaireSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
