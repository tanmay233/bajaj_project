from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def bfhl_view(request):
    if request.method == 'POST':
        try:
            # Sample User Details
            full_name = "john_doe"
            dob = "17091999"
            email = "john@xyz.com"
            roll_number = "ABCD123"

            # Parse the JSON data from the request
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)
            data = body_data.get("data", [])

            # Separate numbers and alphabets
            numbers = [item for item in data if item.isdigit()]
            alphabets = [item for item in data if item.isalpha()]

            # Find the highest lowercase alphabet
            lowercase_alphabets = [item for item in alphabets if item.islower()]
            highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

            # Prepare response
            response = {
                "is_success": True,
                "user_id": f"{full_name}_{dob}",
                "email": email,
                "roll_number": roll_number,
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
            }

        except Exception as e:
            response = {
                "is_success": False,
                "error": str(e)
            }

        return JsonResponse(response)

    elif request.method == 'GET':
        response = {
            "operation_code": "200"
        }
        return JsonResponse(response)

    else:
        return JsonResponse({"is_success": False, "error": "Invalid HTTP method"}, status=405)
