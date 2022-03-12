from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import Krarecords, Article,Returns
from .models import Jobrequest
from django.contrib.auth import get_user_model

User=get_user_model()
class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=User
        fields=('id','email','name','password')

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Krarecords
        fields = ('id', 'names', 'profession','idno','dob','box','county','town','mobile','email','datesend','datecompleted','kratotal','jobtotal','atotal')

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobrequest
        fields = ('id', 'names','idno','message','mobile','jobtype','datecompleted','datesend')

class ReturnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Returns
        fields = ('id', 'names','yourpin','employerpin','email','mobile','p9form','datesend','datecompleted')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title','slug','body','photo','author','dateposted')