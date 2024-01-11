from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField() #custom serializer field

    class Meta:
        model = Movie
        fields = '__all__'
        #fields = ['name','discription'] to include only these fields
        #exclude = ['active']

    # create , update function automatically handled by ModelSerializer
    # Two Validations Available : 1) field level 2) object level 

    def get_len_name(self,object): #method for custom serializer field 
        return len(object.name)

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short.')
        else:
            return value
        
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and Discription cannot be same.")
        else:
            return data 






