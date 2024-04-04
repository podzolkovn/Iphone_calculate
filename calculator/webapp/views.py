from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
import json


# Create your views here.

@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


def index_api_view(request, *args, **kwargs):
    return render(request, 'index.html')


def add_api_view(request, *args, **kwargs):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
            a = float(request_data['a'])
            b = float(request_data['b'])

            if a is not None and b is not None:
                result = a + b

                result_response = {
                    'status': 'ok',
                    'result': result
                }
                return JsonResponse(result_response)
            else:
                return JsonResponse({'status': 'error', 'message': 'Values for "a" and "b" are required.'})

        except KeyError:
            return JsonResponse({'status': 'error', 'message': 'Values for "a" and "b" are required.'})

        except ValueError:
            return JsonResponse(
                {'status': 'error', 'message': 'Invalid input. Please provide numeric values for "a" and "b".'})

    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed.'})


def subtract_api_view(request, *args, **kwargs):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)

            a = float(request_data['a'])
            b = float(request_data['b'])

            if a is not None and b is not None:
                result = a - b

                result_response = {
                    'status': 'ok',
                    'result': result
                }
                return JsonResponse(result_response)
            else:
                return JsonResponse({'status': 'error', 'message': 'Values for "a" and "b" are required.'})

        except KeyError:
            return JsonResponse({'status': 'error', 'message': 'Values for "a" and "b" are required.'})

        except ValueError:
            return JsonResponse(
                {'status': 'error', 'message': 'Invalid input. Please provide numeric values for "a" and "b".'})

    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed.'})


def multiply_api_view(request, *args, **kwargs):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)

            a = float(request_data['a'])
            b = float(request_data['b'])

            if a is not None and b is not None:
                result = a * b

                result_response = {
                    'status': 'ok',
                    'result': result
                }
                return JsonResponse(result_response)
            else:
                return JsonResponse({'status': 'error', 'message': 'Values for "a" and "b" are required.'})

        except KeyError:
            return JsonResponse({'status': 'error', 'message': 'Values for "a" and "b" are required.'})

        except ValueError:
            return JsonResponse(
                {'status': 'error', 'message': 'Invalid input. Please provide numeric values for "a" and "b".'})

    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed.'})


def divide_api_view(request, *args, **kwargs):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
            a = float(request_data['a'])
            b = float(request_data['b'])

            if a is not None and b is not None:
                result = a / b

                result_response = {
                    'status': 'ok',
                    'result': result
                }

                return JsonResponse(result_response)
            else:
                return JsonResponse({'status': 'error', 'message': 'Values for "a" and "b" are required.'})

        except KeyError:
            return JsonResponse({'status': 'error', 'message': 'Values for "a" and "b" are required.'})

        except ValueError:
            return JsonResponse(
                {'status': 'error', 'message': 'Invalid input. Please provide numeric values for "a" and "b".'})

        except ZeroDivisionError:
            return JsonResponse({'status': 'error', 'message': 'ZeroDivisionError'})

    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed.'})
