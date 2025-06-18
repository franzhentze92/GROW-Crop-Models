from django.shortcuts import render, redirect
from crops.models import CropGroup, LabType, Crop

from common.views import validate_token

@validate_token
def index_view(request):
    # Get the 'role' query parameter from the URL handle this by checking for the query parameters
    role = request.GET.get('role')
    token = request.GET.get('token')

    # Ensure role is valid or set to 'agronomist'
    if role not in ['user', 'agronomist']:
        role = 'agronomist'

    # If the URL doesn't already include a valid role, redirect with the role
    if request.GET.get('role') != role:
        return redirect(f"{request.path}?role={role}")

    return render(
        request,
        "index.html",
        {'role': role,
         "token": token
        }
    )
