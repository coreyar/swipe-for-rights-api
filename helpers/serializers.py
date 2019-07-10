from rest_framework import serializers, relations
from typing import Optional


class PrimaryKeyRelatedField(relations.PrimaryKeyRelatedField):

    def to_representation(self, value) -> str:
        return str(super(PrimaryKeyRelatedField, self).to_representation(value))


class BaseSerializer(serializers.ModelSerializer):
    serializer_related_field = PrimaryKeyRelatedField

    id = serializers.SerializerMethodField()
    serializer_related_field = PrimaryKeyRelatedField

    def get_id(self, obj) -> Optional[str]:
        if obj.id:
            return str(obj.id)
