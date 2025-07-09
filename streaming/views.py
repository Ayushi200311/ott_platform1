from django.shortcuts import render
from .models import User

def home(request):
    return render(request, 'home.html')


from django.shortcuts import render
from .models import User

def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f"Signup attempt: {name}, {email}")

        if User.objects.filter(email=email).exists():
            return render(request, 'home.html', {'error': 'email_exists'})

        User.objects.create(name=name, email=email, password=password)
        print("User created successfully")

        return render(request, 'home.html', {'signup_success': True})

    return render(request, 'home.html')




from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signin_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if user.password == password:
                # You can add session login logic here if needed
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'message': 'Invalid password'})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User not found'})











from django.shortcuts import render
from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    # Hero carousel data
    hero_slides = [
        {
            'id': 1,
            'image': 'images/ss6.jpg',
            'title': 'The Last Kingdom',
            'description': 'A warrior torn between his Saxon heritage and Viking upbringing fights for his homeland in this epic tale of honor, loyalty, and survival.',
            'rating': 4.8,
            'year': 2024,
            'is_vip': True,
            'genre': 'Traditional Costume'
        },
        {
            'id': 2,
            'image': 'images/ss7.jpg',
            'title': 'Stranger Minds',
            'description': 'Secrets of the town unravel through supernatural mysteries as a group of friends uncover dark forces beyond their imagination.',
            'rating': 4.9,
            'year': 2024,
            'is_vip': True,
            'genre': 'Supernatural Thriller'
        },
        {
            'id': 3,
            'image': 'images/ss16.jpg',
            'title': 'Wild North',
            'description': 'Nature\'s beauty meets human survival in the wilderness where every decision can mean the difference between life and death.',
            'rating': 4.7,
            'year': 2024,
            'is_vip': True,
            'genre': 'Adventure Drama'
        }
    ]

    hot_items = [
        {'id': 1, 'image': 'images/p1.jpg', 'title': 'The Princess Weiyoung', 'rating': 4.8, 'year': 2024, 'is_vip': True},
        {'id': 2, 'image': 'images/p2.jpeg', 'title': 'Perfect World', 'rating': 4.6, 'year': 2024, 'is_vip': False},
        {'id': 3, 'image': 'images/p3.jpg', 'title': 'Go Ahead', 'rating': 4.9, 'year': 2024, 'is_vip': True},
        {'id': 4, 'image': 'images/p4.jpg', 'title': 'Denied Love Story', 'rating': 4.5, 'year': 2024, 'is_vip': False},
        {'id': 5, 'image': 'images/p5.jpg', 'title': 'You Are My Destiny', 'rating': 4.7, 'year': 2024, 'is_vip': True},
        {'id': 6, 'image': 'images/p6.jpg', 'title': 'Knock Out', 'rating': 4.4, 'year': 2024, 'is_vip': False},
        {'id': 7, 'image': 'images/p7.jpg', 'title': 'Romance Chronicles', 'rating': 4.6, 'year': 2024, 'is_vip': False},
        {'id': 8, 'image': 'images/p8.jpeg', 'title': 'Eternal Journey', 'rating': 4.8, 'year': 2024, 'is_vip': True},
    ]

    new_items = [
        {'id': 9, 'image': 'images/p15.jpeg', 'title': 'Academy of Superpower', 'rating': 4.9, 'year': 2024, 'is_vip': True},
        {'id': 10, 'image': 'images/p14.jpeg', 'title': 'The Prisoner of Beauty', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 11, 'image': 'images/p13.jpeg', 'title': 'My Name is Zhao Chuxi', 'rating': 4.5, 'year': 2024, 'is_vip': False},
        {'id': 12, 'image': 'images/p12.webp', 'title': 'Filter (English Ver.)', 'rating': 4.6, 'year': 2024, 'is_vip': False},
        {'id': 13, 'image': 'images/p11.webp', 'title': 'Wild and Sweet', 'rating': 4.8, 'year': 2024, 'is_vip': True},
        {'id': 14, 'image': 'images/p10.jpeg', 'title': 'Moonlight Romance', 'rating': 4.4, 'year': 2024, 'is_vip': False},
        {'id': 15, 'image': 'images/p9.jpg', 'title': 'Secret Garden', 'rating': 4.7, 'year': 2024, 'is_vip': True},
        {'id': 16, 'image': 'images/p8.jpeg', 'title': 'Phoenix Rising', 'rating': 4.9, 'year': 2024, 'is_vip': False},
    ]

    context = {
        'hero_slides': hero_slides,
        'hot_items': hot_items,
        'new_items': new_items,
    }

    return render(request, 'streaming/home.html', context)










from django.shortcuts import render

def free_page(request):
    hero_slides = [
        {
            'id': 101,
            'image': 'images/ss10.jpg',
            'title': 'Free Warrior',
            'description': 'Epic free content begins here.',
            'rating': 4.5,
            'year': 2024,
            'is_vip': False,
            'genre': 'Action'
        },
        {
            'id': 102,
            'image': 'images/ss11.jpg',
            'title': 'Budget Binge',
            'description': 'Great stories for no cost.',
            'rating': 4.4,
            'year': 2024,
            'is_vip': False,
            'genre': 'Comedy'
        },
    ]

    free_items = [
        {'id': 201, 'image': 'images/p1.jpg', 'title': 'Public Drama', 'rating': 4.6, 'year': 2024, 'is_vip': False},
        {'id': 202, 'image': 'images/p3.jpg', 'title': 'Open Road', 'rating': 4.5, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
    ]

    return render(request, 'streaming/category.html', {
        'section_title': 'FREE',
        'hero_slides': hero_slides,
        'media_items': free_items
    })




def kdrama_page(request):
    hero_slides = [
        {
            'id': 101,
            'image': 'images/ss7.jpg',
            'title': 'Free Warrior',
            'description': 'Epic free content begins here.',
            'rating': 4.5,
            'year': 2024,
            'is_vip': False,
            'genre': 'Action'
        },
        {
            'id': 102,
            'image': 'images/ss11.jpg',
            'title': 'Budget Binge',
            'description': 'Great stories for no cost.',
            'rating': 4.4,
            'year': 2024,
            'is_vip': False,
            'genre': 'Comedy'
        },
    ]

    free_items = [
        {'id': 201, 'image': 'images/p1.jpg', 'title': 'Public Drama', 'rating': 4.6, 'year': 2024, 'is_vip': False},
        {'id': 202, 'image': 'images/p3.jpg', 'title': 'Open Road', 'rating': 4.5, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
    ]

    return render(request, 'streaming/category.html', {
        'section_title': 'FREE',
        'hero_slides': hero_slides,
        'media_items': free_items
    })


def cdrama_page(request):
    hero_slides = [
        {
            'id': 101,
            'image': 'images/ss6.jpg',
            'title': 'Free Warrior',
            'description': 'Epic free content begins here.',
            'rating': 4.5,
            'year': 2024,
            'is_vip': False,
            'genre': 'Action'
        },
        {
            'id': 102,
            'image': 'images/ss11.jpg',
            'title': 'Budget Binge',
            'description': 'Great stories for no cost.',
            'rating': 4.4,
            'year': 2024,
            'is_vip': False,
            'genre': 'Comedy'
        },
    ]

    free_items = [
        {'id': 201, 'image': 'images/p1.jpg', 'title': 'Public Drama', 'rating': 4.6, 'year': 2024, 'is_vip': False},
        {'id': 202, 'image': 'images/p3.jpg', 'title': 'Open Road', 'rating': 4.5, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
    ]

    return render(request, 'streaming/category.html', {
        'section_title': 'FREE',
        'hero_slides': hero_slides,
        'media_items': free_items
    })

def thaidrama_page(request):
    hero_slides = [
        {
            'id': 101,
            'image': 'images/ss5.jpg',
            'title': 'Free Warrior',
            'description': 'Epic free content begins here.',
            'rating': 4.5,
            'year': 2024,
            'is_vip': False,
            'genre': 'Action'
        },
        {
            'id': 102,
            'image': 'images/ss11.jpg',
            'title': 'Budget Binge',
            'description': 'Great stories for no cost.',
            'rating': 4.4,
            'year': 2024,
            'is_vip': False,
            'genre': 'Comedy'
        },
    ]

    free_items = [
        {'id': 201, 'image': 'images/p1.jpg', 'title': 'Public Drama', 'rating': 4.6, 'year': 2024, 'is_vip': False},
        {'id': 202, 'image': 'images/p3.jpg', 'title': 'Open Road', 'rating': 4.5, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
    ]

    return render(request, 'streaming/category.html', {
        'section_title': 'FREE',
        'hero_slides': hero_slides,
        'media_items': free_items
    })

def reality_show_page(request):
    hero_slides = [
        {
            'id': 101,
            'image': 'images/ss4.jpg',
            'title': 'Free Warrior',
            'description': 'Epic free content begins here.',
            'rating': 4.5,
            'year': 2024,
            'is_vip': False,
            'genre': 'Action'
        },
        {
            'id': 102,
            'image': 'images/ss11.jpg',
            'title': 'Budget Binge',
            'description': 'Great stories for no cost.',
            'rating': 4.4,
            'year': 2024,
            'is_vip': False,
            'genre': 'Comedy'
        },
    ]

    free_items = [
        {'id': 201, 'image': 'images/p1.jpg', 'title': 'Public Drama', 'rating': 4.6, 'year': 2024, 'is_vip': False},
        {'id': 202, 'image': 'images/p3.jpg', 'title': 'Open Road', 'rating': 4.5, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
    ]

    return render(request, 'streaming/category.html', {
        'section_title': 'FREE',
        'hero_slides': hero_slides,
        'media_items': free_items
    })




def movies_page(request):
    hero_slides = [
        {
            'id': 101,
            'image': 'images/ss3.jpg',
            'title': 'Free Warrior',
            'description': 'Epic free content begins here.',
            'rating': 4.5,
            'year': 2024,
            'is_vip': False,
            'genre': 'Action'
        },
        {
            'id': 102,
            'image': 'images/ss11.jpg',
            'title': 'Budget Binge',
            'description': 'Great stories for no cost.',
            'rating': 4.4,
            'year': 2024,
            'is_vip': False,
            'genre': 'Comedy'
        },
    ]

    free_items = [
        {'id': 201, 'image': 'images/p1.jpg', 'title': 'Public Drama', 'rating': 4.6, 'year': 2024, 'is_vip': False},
        {'id': 202, 'image': 'images/p3.jpg', 'title': 'Open Road', 'rating': 4.5, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
    ]

    return render(request, 'streaming/category.html', {
        'section_title': 'FREE',
        'hero_slides': hero_slides,
        'media_items': free_items
    })


def anime_page(request):
    hero_slides = [
        {
            'id': 101,
            'image': 'images/ss12.jpg',
            'title': 'Free Warrior',
            'description': 'Epic free content begins here.',
            'rating': 4.5,
            'year': 2024,
            'is_vip': False,
            'genre': 'Action'
        },
        {
            'id': 102,
            'image': 'images/ss11.jpg',
            'title': 'Budget Binge',
            'description': 'Great stories for no cost.',
            'rating': 4.4,
            'year': 2024,
            'is_vip': False,
            'genre': 'Comedy'
        },
    ]

    free_items = [
        {'id': 201, 'image': 'images/p1.jpg', 'title': 'Public Drama', 'rating': 4.6, 'year': 2024, 'is_vip': False},
        {'id': 202, 'image': 'images/p3.jpg', 'title': 'Open Road', 'rating': 4.5, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
    ]

    return render(request, 'streaming/category.html', {
        'section_title': 'FREE',
        'hero_slides': hero_slides,
        'media_items': free_items
    })

def all_page(request):
    hero_slides = [
        {
            'id': 101,
            'image': 'images/ss12.jpg',
            'title': 'Free Warrior',
            'description': 'Epic free content begins here.',
            'rating': 4.5,
            'year': 2024,
            'is_vip': False,
            'genre': 'Action'
        },
        {
            'id': 102,
            'image': 'images/ss11.jpg',
            'title': 'Budget Binge',
            'description': 'Great stories for no cost.',
            'rating': 4.4,
            'year': 2024,
            'is_vip': False,
            'genre': 'Comedy'
        },
    ]

    free_items = [
        {'id': 201, 'image': 'images/p1.jpg', 'title': 'Public Drama', 'rating': 4.6, 'year': 2024, 'is_vip': False},
        {'id': 202, 'image': 'images/p3.jpg', 'title': 'Open Road', 'rating': 4.5, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
    ]

    return render(request, 'streaming/category.html', {
        'section_title': 'FREE',
        'hero_slides': hero_slides,
        'media_items': free_items
    })


def sort_series_page(request):
    hero_slides = [
        {
            'id': 101,
            'image': 'images/ss7.jpg',
            'title': 'Free Warrior',
            'description': 'Epic free content begins here.',
            'rating': 4.5,
            'year': 2024,
            'is_vip': False,
            'genre': 'Action'
        },
        {
            'id': 102,
            'image': 'images/ss11.jpg',
            'title': 'Budget Binge',
            'description': 'Great stories for no cost.',
            'rating': 4.4,
            'year': 2024,
            'is_vip': False,
            'genre': 'Comedy'
        },
    ]

    free_items = [
        {'id': 201, 'image': 'images/p1.jpg', 'title': 'Public Drama', 'rating': 4.6, 'year': 2024, 'is_vip': False},
        {'id': 202, 'image': 'images/p3.jpg', 'title': 'Open Road', 'rating': 4.5, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p1.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p1.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
        {'id': 203, 'image': 'images/p5.jpg', 'title': 'Free Flow', 'rating': 4.7, 'year': 2024, 'is_vip': False},
    ]

    return render(request, 'streaming/category.html', {
        'section_title': 'FREE',
        'hero_slides': hero_slides,
        'media_items': free_items
    })

