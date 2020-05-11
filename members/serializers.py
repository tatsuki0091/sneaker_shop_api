from rest_framework import serializers

from members.models import Member

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