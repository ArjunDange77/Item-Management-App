from rest_framework import serializers
from . import models as item_models


class ItemMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = item_models.ItemMaster
        fields = ("id","name","price","description")