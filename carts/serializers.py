from rest_framework import serializers
import datetime
from carts.models import Cart
import logging


class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            'id',
            'purchase_date',
            'insert_date',
            'update_date',
            'member_id',
            'product_id',
            'quantity',
        )
    
    # member = serializers.ReadOnlyField()
    # product = serializers.ReadOnlyField()
    # quantity = serializers.IntegerField()
    #purchase_date = serializers.DateTimeField(null=True)
    # def save(self, *args, **kwargs):
    #     logfile = r"/Users/Tatsuki/projects/django/book_shop_api/book_shop_api/development.log"
    #     logging.basicConfig(filename=logfile, level=logging.DEBUG)
    #     logging.info('test')
    #     #member_id = self.data.member_id
    #     logging.info(self)
        
        

