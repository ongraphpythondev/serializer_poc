from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'email', 'roll_num', 'subject', 'address']
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.roll_num = validated_data.get('roll_num', instance.roll_num)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
    def validate_email(self, value):
        if self.instance:
            existing_emails = Student.objects.exclude(id=self.instance.id).filter(email=value)
        else:
            existing_emails = Student.objects.filter(email=value)

        if existing_emails.exists():
            raise serializers.ValidationError("This email is already in use.")
        return value
    def validate_roll_num(self, value):
        if value < 0:
            raise serializers.ValidationError("Roll number cannot be negative")
        return value