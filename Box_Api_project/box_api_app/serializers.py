from rest_framework import serializers
from .models import Box
# from django.contrib.auth.models import User

class BoxSerializers(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ['id','length','width','height','area','vol','creator']
    
    
    
    
    def to_representation(self, instance):
        rep = super(BoxSerializers, self).to_representation(instance)
        if self.context['request'].user:
            rep['creator'] = instance.creator.username
        return rep 