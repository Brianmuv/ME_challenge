from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return render(request, 'pairs_sum_app/home.html')



def find_pairs_with_sum(numbers, target):
    seen = set()
    pairs = []

    for num in numbers:
        complement = target - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)

    return pairs



@csrf_exempt
def find_number_pairs(request):
    print("---------->",request.method)
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            numbers = [int(num) for num in data.get('numbers', '').split(',')]
            target_sum = int(data.get('target_sum', 0))

           
            pairs = find_pairs_with_sum(numbers, target_sum)

            # Return the pairs as a JSON response
            return JsonResponse({'pairs': pairs})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)





