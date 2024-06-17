# from rest_framework import generics, permissions
# from rest_framework.parsers import FormParser, MultiPartParser
# from rest_framework.response import Response
# from rest_framework import status
# from common.models import Country, DocumentType
# from machina import face_verification
# from verify_document.document_response import doc_response
# from verify_document.serializers import CountrySerializer, DucumentTypeSerializer, VerifyGhanaCardSerializer


# validations = face_verification.VerificationsAndValidations


# class BaseVerifyGhanaCard(generics.GenericAPIView):
#     serializer_class = VerifyGhanaCardSerializer
#     parser_classes = (FormParser, MultiPartParser)


# class VerifyGhanaCard(BaseVerifyGhanaCard):
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data = self.request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         data = dict(serializer.data)
#         image = validations.compare_images(data["ghana_card_front"], data["passport_pic"])
#         document = validations.extract_text(data["ghana_card_back"])
#         if image and document["country"] == "GHA" and document["mrz_type"] == "TD1":
#             get_response = doc_response(image, document)
#             return Response(get_response)
#         return Response({
#             "status": False,
#             "verification_status": image["verified"],
#         })
    
from rest_framework.decorators import api_view
@api_view(["GET"]) 
def Test(request):
    return {
        "message": True
    }