from rest_framework import serializers
from .models import user_register, admin_register


class user_registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_register
        fields = '__all__'













    # Male = 'M'
    # Female = 'F'
    # Transgender = 'TRANS'

    # gender_choices = [
    #     (Male, 'Male'),
    #     (Female, 'Female'),
    #     (Transgender, 'Transgender'),
    # ]
    
    # member_id = serializers.CharField(max_length= 6, allow_null= True)
    # uid = serializers.UUIDField()
    # #name_of_org = serializers.ForeignKey(on_delete=serializers.DO_NOTHING, allow_null= True) 
    # otp = serializers.CharField(max_length=50)
    # name = serializers.CharField(max_length=30)
    # gender = serializers.CharField(max_length=12)
    # username = serializers.CharField(max_length= 10)
    # date_of_birth = serializers.DateField(allow_null= True)
    # contact = serializers.CharField(max_length=10)
    # email = serializers.EmailField()
    # verify = serializers.BooleanField(default=False)


    # class admin_registerSerializer(serializers.Serializer):
    #     id = serializers.UUIDField(primary_key = True)
    #     otp = serializers.CharField(max_length=50)
    #     name_of_org = serializers.CharField(max_length=30)
    #     year_of_foundation = serializers.IntegerField()
    #     contact_number = serializers.IntegerField()
    #     username = serializers.CharField(max_length= 10)
    #     email = serializers.EmailField()
    #     verify = serializers.BooleanField(default=False)