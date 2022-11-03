import json
import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
)
from rest_framework_mongoengine import viewsets
from django_rest_telegram.api.authentication import SessionCsrfExemptAuthentication
from django_rest_telegram.api.utils import (
    MF_FIELDS_KEYS,
    filter_json,
)


logger = logging.getLogger(__name__)


@api_view(["POST"])
@authentication_classes([SessionCsrfExemptAuthentication])
def webhookView(request):
    # Arrives in bytes, have to decode
    content = filter_json(request.body, MF_FIELDS_KEYS)
    print("view", content)
    return Response(status=status.HTTP_201_CREATED)
