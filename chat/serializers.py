from rest_framework import serializers
from .models import Message, Ticket
from .tasks import status_update_notification


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ticket
        fields = "__all__"


class TicketUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("status",)

    def update(self, instance, validated_data):
        changed_status = validated_data.get('status', instance.status)

        if instance.status != changed_status:
            instance.status = changed_status
            instance.save()
            status_update_notification.delay(instance.title,
                                             instance.user.email,
                                             changed_status)
        return instance


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = "__all__"
