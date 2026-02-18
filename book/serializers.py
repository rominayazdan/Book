from rest_framework import serializers
from book.models import Book, ImageBook
import datetime



class ImageBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageBook
        fields = ['id', 'name', 'book']



class BookSerializer(serializers.ModelSerializer):
    images = ImageBookSerializer(many=True, read_only=True)
    added_by = serializers.StringRelatedField()


    def validate(self, attrs):
        if True:
            res = super().validate(attrs=attrs)
            return res

    def to_representation(self, instance):
        response = super().to_representation(instance=instance)

        return response

    class Meta:
        model = Book
        fields = "__all__"



