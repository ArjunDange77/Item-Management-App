from django.shortcuts import render
from rest_framework import viewsets
from . import models as item_models
from . import serializers as item_serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum


class ItemMaster(viewsets.ModelViewSet):
    queryset = item_models.ItemMaster.objects.all()
    serializer_class = item_serializers.ItemMasterSerializer

    @action(methods=["post"], detail=False)
    def generate_bill(self, request, *args, **kwargs):
        item_ids = request.data.get("selectedItems")
        total_price = self.queryset.filter(id__in=item_ids).aggregate(total_price=Sum('price'))['total_price'] or 0
        return Response({"Total Bill Value": total_price})
