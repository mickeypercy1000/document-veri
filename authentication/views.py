# from rest_framework.decorators import api_view
from authentication.models import User
from authentication.serializers import CreateUserSerializer, LoginSerializer, LogoutUserSerializer, UpdateRetrieveUserSerializer, VerifyOTPSerializer
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from django.http import Http404
from rest_framework.exceptions import AuthenticationFailed

from authentication.utils import otp_email_verification, send_verification_email
from merchant.models import MerchantAccount
from merchant.serializers import ComplianceSerializer


class CreateUser(generics.GenericAPIView):
    '''
    This endpoint creates a new user and returns appropriate responses.
    '''
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        return user

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = self.perform_create(serializer)
            pin = otp_email_verification(user)
            user.save()
            send_verification_email(user, pin)
            account = MerchantAccount.objects.create(user=user)
            account.save()
            message = {
                "message": "An OTP has been sent to your email. Please confirm",
                "user_id": user.id,
            }
            return Response(message, status=status.HTTP_201_CREATED)
        except Exception as e:
            message = {str(e)}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTP(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = VerifyOTPSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.validated_data["user_id"]
        otp = serializer.validated_data["otp"]

        try:
            user = User.objects.get(id=user_id)
            if user:
                if user.otp == otp:
                    user.otp_verified = True
                    user.save()

                    message = {
                        "message": "OTP verification successful"
                    }
                    return Response(message, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "OTP does not match"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "user does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({"message": "otp verification failed"}, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
    
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        account = MerchantAccount.objects.get(user=user)
        kyc_completed = account.kyc_completed
        # kyc = account.kyc
        # merged_kyc_data = {}
        # business_documents = {
        #     "form_a": account.form_a,
        #     "business_incorporation": account.business_incorporation,
        #     "form_three_and_four": account.form_three_and_four,
        #     "logo": account.logo
        # }
        # if not kyc:
        #     merged_kyc_data = business_documents
        # else:
        #     merged_kyc_data = {**kyc, **business_documents}

        # for key, value in merged_kyc_data.items():
        #     if not key or not value:
        #         print(key, value)
        #         kyc_completed = False  # Set to False if any value is missing
        #         break
        #     else:
        #         kyc_completed = True  # Set to True if all values exist
        # print(kyc_completed)

        # account.kyc_completed = kyc_completed
        # account.save()
        
        try:
            otp_verified = user.otp_verified
            if otp_verified is False:
                pin = otp_email_verification(user)
                send_verification_email(user, pin)

                return Response({
                    "user_id": user.id,
                    "message": "OTP not verified. A new OTP has been sent to your email. Please verify to proceed"
                    })
            else:
                refresh = RefreshToken.for_user(user)

                return Response({
                    "user": {
                        "id": user.id,
                        "firstname": user.firstname,
                        "lastname": user.lastname,
                        "access": str(refresh.access_token),
                        "kyc_completed": kyc_completed
                        # "refresh": str(refresh),
                    },
                }, status=status.HTTP_200_OK)
        except Exception:
            message = {"message": "login failed"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class GetUserByID(generics.RetrieveUpdateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UpdateRetrieveUserSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            # email = instance.get_email()
        except Http404:
            message = {"message": "User not found."}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        try:
            serializer = self.get_serializer(instance)
            return Response({"user": serializer.data}, status=status.HTTP_200_OK)
        except AuthenticationFailed as e:
            return Response({"message": str(e)}, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        # instance.kyc = serializer.validated_data
        instance.save()

        return Response({
            # "name": instance.user.get_fullname(),
            # "phone": instance.user.phone,
            # "email": instance.user.get_email(),
            "updated_data": serializer.data
            })


class LogoutUser(generics.GenericAPIView):

    serializer_class = LogoutUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        message = {"message": "Logout successful"}
        return Response(message, status=status.HTTP_204_NO_CONTENT)
