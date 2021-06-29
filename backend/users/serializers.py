from rest_framework import fields
from machina.core.db.models import get_model
from rest_framework.serializers import ModelSerializer, RelatedField, CharField
from django.contrib.auth.models import User

ForumReadTrack = get_model('forum_tracking', 'ForumReadTrack')
Forum = get_model('forum', 'Forum')


class ForumSerializer(ModelSerializer):
    class Meta:
        model = Forum
        fields  = ('name',)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields  = ('username',)
        # fields  = '__all__'


class ForumReadTrackSerializer(ModelSerializer):
    forum = ForumSerializer()
    user = UserSerializer()
    # forum = CharField(source='get_forum_display', read_only=True)

    class Meta:
        model = ForumReadTrack
        fields  = ('forum', 'user')
        # depth = 1
