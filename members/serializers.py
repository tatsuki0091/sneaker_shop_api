from rest_framework import serializers
import datetime
from members.models import Member
import logging

# パスワードハッシュ化のためのライブラリ
from django.contrib.auth.hashers import make_password


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
            'id',
            'first_name',
            'last_name',
            'mail_address',
            'prefecture',
            'address1',
            'address2',
            'phone_number',
            'password',
            'insert_date',
            'update_date',
        )

    def validate_password(self, value):
        logfile = r"/Users/Tatsuki/projects/django/book_shop_api/book_shop_api/development.log"
        logging.basicConfig(filename=logfile, level=logging.DEBUG)
        data = self.initial_data

        password = data.get("password")
        password_confirmation = data.get("password_confirmation")

        if password != password_confirmation:
            raise serializers.ValidationError(
                "Password and password confirmation do not match")

        # パスワードハッシュ化
        hash_password = make_password(password)

        return hash_password


class MemberAuthSerializer(serializers.Serializer):
    mail_address = serializers.EmailField()
    password = serializers.CharField(max_length=200)
