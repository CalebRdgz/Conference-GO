from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Attendee, ConferenceVO
import json

from common.json import ModelEncoder
from .models import Attendee

class ConferenceVODetailEncoder(ModelEncoder):
    model = ConferenceVO
    properties = ["name", "import_href"]



def api_list_attendees(request, conference_vo_id=None):
    """
    Lists the attendees names and the link to the attendee
    for the specified conference id.

    Returns a dictionary with a single key "attendees" which
    is a list of attendee names and URLS. Each entry in the list
    is a dictionary that contains the name of the attendee and
    the link to the attendee's information.

    {
        "attendees": [
            {
                "name": attendee's name,
                "href": URL to the attendee,
            },
            ...
        ]
    }
    """
    # response = []
    # attendees = Attendee.objects.all()
    # for attendee in attendees:
    #     response.append(
    #         {
    #             "name": attendee.name,
    #             "href": attendee.get_api_url(),
    #         }
    #     )
    # return JsonResponse({"attendees": response})
    if request.


def api_show_attendee(request, pk):
    """
    Returns the details for the Attendee model specified
    by the pk parameter.

    This should return a dictionary with email, name,
    company name, created, and conference properties for
    the specified Attendee instance.

    {
        "email": the attendee's email,
        "name": the attendee's name,
        "company_name": the attendee's company's name,
        "created": the date/time when the record was created,
        "conference": {
            "name": the name of the conference,
            "href": the URL to the conference,
        }
    }
    """
    attendee = Attendee.objects.get(id=pk)
    return JsonResponse({
        "email": attendee.email,
        "name": attendee.name,
        "company_name": attendee.company_name,
        "created": attendee.created,
        "conference": {
            "name": attendee.location.name,
            "href": attendee.location.get_api_url(),
        }
    })
