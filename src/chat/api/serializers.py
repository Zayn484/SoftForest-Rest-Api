from rest_framework import serializers
from chat.models import Chat, Contact
from chat.views import get_user_contact


class ContactSerializer(serializers.ModelSerializer):
    """Serializer for contacts"""

    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'

    def to_internal_value(self, data):
        return data


class ChatSerializer(serializers.ModelSerializer):
    """Serializer for chats"""

    participants = ContactSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('id', 'messages', 'participants', 'group')
        read_only = 'id'

    def create(self, validated_data):
        participants = validated_data.pop('participants')
        group = validated_data['group']
        chat = Chat(group=group)
        chat.save()
        for username in participants:
            contact = get_user_contact(username, None)
            chat.participants.add(contact)
        chat.save()
        return chat


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for chats"""

    participants = ContactSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('id', 'messages', 'participants', 'group')

    def create(self, validated_data):
        participants = validated_data.pop('participants')
        print(participants)
        group = validated_data['group']
        chat = Chat(group=group)
        chat.save()
        for id in participants:
            contact = get_user_contact(None, id)
            chat.participants.add(contact)
        chat.save()
        return chat


