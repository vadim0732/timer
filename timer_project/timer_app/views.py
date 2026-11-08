from django.shortcuts import render

def start_page(request):
    """Страница настройки и запуска таймера"""
    return render(request, 'start.html')

def timer_page(request):
    """Страница с обратным отсчетом"""
    seconds = request.GET.get('seconds', 0)
    
    # Проверка, что ввели число
    try:
        seconds = int(seconds)
    except ValueError:
        seconds = 0
        
    return render(request, 'timer.html', {'initial_seconds': seconds})