from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from phonenumber_field.serializerfields import PhoneNumberField

# https://stackoverflow.com/questions/36910373/django-rest-auth-allauth-registration-with-email-first-and-last-name-and-witho
# https://stackoverflow.com/questions/57496154/how-to-add-extra-fields-to-registration-end-point-of-rest-auth
class RegistrationSerializer(RegisterSerializer):
    phone_number = PhoneNumberField()

    # This method is called at save
    def custom_signup(self, request, user):
        user.phone_number = self.validated_data.get('phone_number', '')
        user.save(update_fields=['phone_number',])
