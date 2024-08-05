from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from users.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse


@login_required
def home(request):
    games = Game.objects.all()
    cart = Cart.objects.filter(user=request.user).first() if request.user.is_authenticated else None
    cart_count = CartItem.objects.filter(cart=cart).count() if request.user.is_authenticated else 0
    return render(request, 'site/home.html', {'games': games, 'cart_count': cart_count})

def index(request):
    user = request.user
    games = Game.objects.all()
    data_game = []
    cart = Cart.objects.filter(user=user).first() if user.is_authenticated else None
    cart_count = CartItem.objects.filter(cart=cart).count() if user.is_authenticated else 0
    form = LoginForm
    vorm = UserRegistrationForm
    for games in games:
        data_game.append(    
            {
            'games': games,
            'liked': games.user_liked(user) if user.is_authenticated else False,
            'comments': Comment.objects.filter(game=games),
            'commented': games.user_commented(user) if user.is_authenticated else False,
            }
        )
    return render(request, 'site/index.html', {'games': data_game, 'cart_count': cart_count, 'form': form, 'vorm': vorm})



@login_required
def like_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    like, created = Like.objects.get_or_create(user=request.user, game=game)
    if not created:
        like.delete()
    return redirect('index')

@login_required
def comment_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(user=request.user, game=game, content=content)
    return redirect('index')


@login_required
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Game cadastrada com sucesso!')
            return redirect('home')
    else:
        form = GameForm()
    return render(request, 'site/add_game.html', {'form': form})

@login_required
def edit_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            messages.success(request, 'Game editada com sucesso!')
            return redirect('home')
    else:
        form = GameForm(instance=game)
    return render(request, 'site/edit_game.html', {'form': form})

@login_required
def delete_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == 'POST':
        game.delete()
        messages.success(request, 'Game deletada com sucesso!')
        return redirect('home')
    return render(request, 'site/delete_game.html', {'game': game})


def add_to_cart(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, game=game, quantity=1)
    cart_count = CartItem.objects.filter(cart=cart).count() if request.user.is_authenticated else 0
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return JsonResponse({'success': 'true', 'quantity': cart_item.quantity, 'cart_count': cart_count})

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return JsonResponse({'success': 'true'})

def view_cart(request):
    total_price = 0
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    user = request.user
    cart_count = CartItem.objects.filter(cart=cart).count() if request.user.is_authenticated else 0
    for item in items:
        total_price += item.price_total()
    return render(request, 'site/cart.html', {'cart': cart, 'items': items, 'cart_count': cart_count, 'total_price': total_price, 'user': user})

def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    total_price = 0
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'increase':
            cart_item.quantity += 1
        elif action == 'decrease' and cart_item.quantity > 1:
            cart_item.quantity -= 1
        cart_item.save()
        items = CartItem.objects.filter(cart=cart_item.cart)
        for item in items:
            total_price += item.price_total()

        return JsonResponse({'success': 'true', 'quantity': cart_item.quantity, 'total_price': total_price})


def checkout(request, id_user):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    total_price = sum( item.quantity * item.game.price for item in items)
    if request.method == 'POST':
        cart.delete()
        buy = compras.objects.create(user_id=id_user, quantity=total_price)
        buy.save()
        messages.success(request, 'Compra realizada com sucesso!')
        return redirect('index')
    return render(request, 'site/checkout.html', {'cart': cart, 'total_price': total_price})


@login_required
def address(request, id_user):
    user = User.objects.get(id=id_user)
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user_id = id_user
            address.save()
            messages.success(request, 'Endereço cadastrado com sucesso!')
            return redirect('view_cart')
    else:
        form = AddressForm()
    return render(request, 'site/address.html', {'form': form})