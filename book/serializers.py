from rest_framework import serializers
from book.models import Book
import datetime


class BookSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        print('data', data)
        data['published_date'] = datetime.datetime.strptime(data['published_date'], '%Y/%m/%d').date()
        print(data)
        result = super().to_internal_value(data=data)

        print(result)
        return result

    def validate(self, attrs):
        if True:
            res = super().validate(attrs=attrs)
            return res

    def to_representation(self, instance):
        response = super().to_representation(instance=instance)
        response['published_date'] = '1404-10-12'
        return response

    class Meta:
        model = Book
        fields = "__all__"
