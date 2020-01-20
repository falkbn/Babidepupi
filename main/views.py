import shelve
from main.models import User, Peripheral, Rating
from main.forms import UserForm, PeripheralForm
from django.shortcuts import render, get_object_or_404
from main.recommendations import transformprefs, calculateSimilarItems, getRecommendations, getRecommendedItems, \
    topMatches
from main.populate import populate_db


def load_dict():
    prefs = {}  # matriz de usuarios y puntuaciones a cada a items
    shelf = shelve.open("dataRS.dat")
    ratings = Rating.objects.all()
    for ra in ratings:
        user = int(ra.user.id)
        item_id = int(ra.peripheral.id)
        rating = float(ra.rating)
        prefs.setdefault(user, {})
        prefs[user][item_id] = rating
    shelf['prefs'] = prefs
    shelf['ItemsPrefs'] = transformprefs(prefs)
    shelf['SimItems'] = calculateSimilarItems(prefs, n=10)
    shelf.close()


def index(request):
    return render(request, 'index.html')


def populate_db(request):
    populate_db()
    return render(request, 'populate.html')


def load_rs(request):
    load_dict()
    return render(request, 'loadRS.html')


def recommended_peripherals_users(request):
    if request.method == 'GET':
        form = UserForm(request.GET, request.FILES)
        if form.is_valid():
            id_user = form.cleaned_data['id']
            user = get_object_or_404(User, pk=id_user)
            shelf = shelve.open("dataRS.dat")
            prefs = shelf['prefs']
            shelf.close()
            rankings = getRecommendations(prefs, int(id_user))
            recommended = rankings[:2]
            peripherals = []
            scores = []
            for re in recommended:
                peripherals.append(Peripheral.objects.get(pk=re[1]))
                scores.append(re[0])
            items = zip(peripherals, scores)
            return render(request, 'recommendationItems.html', {'user': user, 'items': items})
    form = UserForm()
    return render(request, 'search_user.html', {'form': form})


def recommended_peripherals_items(request):
    if request.method == 'GET':
        form = UserForm(request.GET, request.FILES)
        if form.is_valid():
            id_user = form.cleaned_data['id']
            user = get_object_or_404(User, pk=id_user)
            shelf = shelve.open("dataRS.dat")
            prefs = shelf['prefs']
            SimItems = shelf['SimItems']
            shelf.close()
            rankings = getRecommendedItems(prefs, SimItems, int(id_user))
            recommended = rankings[:2]
            peripherals = []
            scores = []
            for re in recommended:
                peripherals.append(Peripheral.objects.get(pk=re[1]))
                scores.append(re[0])
            items = zip(peripherals, scores)
            return render(request, 'recommendationItems.html', {'user': user, 'items': items})
    form = UserForm()
    return render(request, 'search_user.html', {'form': form})


def similar_peripherals(request):
    peripheral = None
    if request.method == 'GET':
        form = PeripheralForm(request.GET, request.FILES)
        if form.is_valid():
            id_peripheral = form.cleaned_data['id']
            peripheral = get_object_or_404(Peripheral, pk=id_peripheral)
            shelf = shelve.open("dataRS.dat")
            items_prefs = shelf['Itemsprefs']
            shelf.close()
            recommended = topMatches(items_prefs, int(id_peripheral), n=3)  # n = number of similar items
            peripherals = []
            similar = []
            for re in recommended:
                peripherals.append(Peripheral.objects.get(pk=re[1]))
                similar.append(re[0])
            items = zip(peripherals, similar)
            return render(request, 'similarPeripherals.html', {'peripheral': peripheral, 'peripherals': items})
    form = PeripheralForm()
    return render(request, 'search_film.html', {'form': form})


def recommended_users_peripherals(request):
    if request.method == 'GET':
        form = PeripheralForm(request.GET, request.FILES)
        if form.is_valid():
            id_peripheral = form.cleaned_data['id']
            peripheral = get_object_or_404(Peripheral, pk=id_peripheral)
            shelf = shelve.open("dataRS.dat")
            prefs = shelf['Itemsprefs']
            shelf.close()
            rankings = getRecommendations(prefs, int(id_peripheral))
            recommended = rankings[:3]
            peripherals = []
            scores = []
            for re in recommended:
                peripherals.append(User.objects.get(pk=re[1]))
                scores.append(re[0])
            items = zip(peripherals, scores)
            return render(request, 'recommendationUsers.html', {'peripheral': peripheral, 'items': items})
    form = PeripheralForm()
    return render(request, 'search_film.html', {'form': form})


def search(request):
    if request.method == 'GET':
        form = UserForm(request.GET, request.FILES)
        if form.is_valid():
            id_user = form.cleaned_data['id']
            user = get_object_or_404(User, pk=id_user)
            return render(request, 'ratedPeripherals.html', {'user': user})
    form = UserForm()
    return render(request, 'search_user.html', {'form': form})
