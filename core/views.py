from django.http import JsonResponse
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    return JsonResponse({'message': 'Welcome to KilimaHub - African Social Hub'})

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                return JsonResponse({'status': 'Post created successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
