from rest_framework import serializers
# from .models import File
# class FileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = File
#         fields = (
#             'id','UR'
#         )


class YourSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   
   TxnDate=serializers.CharField(max_length=50)

   Description=serializers.CharField(max_length=500)
   #Chequenumber=serializers.CharField(max_length=500)
   Debit=serializers.CharField(default=0)
   Credit=serializers.CharField(default=0)
   Balance=serializers.CharField(default=0)

from . import models

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ('id', 'name', 'email')
  

class EntrySerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    class Meta:
        model = models.Entry
        fields = ('id', 'headline','authors')
        

    def create(self, validated_data):
        author_data = validated_data.pop('authors')
        validated_data['authors'] = models.Author.objects.create(**author_data)
        entry = models.Entry.objects.create(**validated_data)
        return entry
    # def create(self, validated_data):
    #    author_data = validated_data.pop('authors')
    #    entry = models.Entry.objects.create(**validated_data)
    #    for category in author_data:
    #     entry.authors.create(**category)
    #    return entry


# class PortfolioSerializer(serializers.ModelSerializer):
#     authors = serializers.SerializerMethodField()
#     class Meta:
#         model = models.Entry
#         fields = ('id', 'headline','authors')

#     def get_authors(self, obj):
#         return_data = None
#         if type(obj.authors) == list:
#             embedded_list = []
#             for item in obj.authors:
#                 embedded_dict = item.__dict__
#                 for key in list(embedded_dict.keys()):
#                     if key.startswith('_'):
#                         embedded_dict.pop(key)
#                 embedded_list.append(embedded_dict)
#             return_data = embedded_list
#         else:
#             embedded_dict = obj.authors
#             print(embedded_dict)
#             for key in list(embedded_dict.keys()):
#                 if key.startswith('_'):
#                     embedded_dict.pop(key)
#             return_data = embedded_dict
#         return return_data
