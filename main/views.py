import shelve
from main.models import User, Peripheral, Rating
from main.forms import UserForm, PeripheralForm
from django.shortcuts import render, get_object_or_404
from main.recommendations import transformPrefs, calculateSimilarItems, getRecommendations, getRecommendedItems, \
    topMatches
from main.populate import populate_db


def load_dict():
    prefs = {}
    shelf = shelve.open("dataRS.dat")
    ratings = Rating.objects.all()
    for ra in ratings:
        user = int(ra.user.id)
        item_id = int(ra.peripheral.id)
        rating = float(ra.rating)
        prefs.setdefault(user, {})
        prefs[user][item_id] = rating
    shelf['Prefs'] = prefs
    shelf['ItemsPrefs'] = transformPrefs(prefs)
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


def recommended_peripheral_user(request):
    if request.method == 'GET':
        form = UserForm(request.GET, request.FILES)
        if form.is_valid():
            id_user = form.cleaned_data['id']
            user = get_object_or_404(User, pk=id_user)
            shelf = shelve.open("dataRS.dat")
            Prefs = shelf['Prefs']
            shelf.close()
            rankings = getRecommendations(Prefs, int(id_user))
            recommended = rankings[:2]
            peripherals = []
            scores = []
            for re in recommended:
                films.append(Peripheral.objects.get(pk=re[1]))
                scores.append(re[0])
            items = zip(films, scores)
            return render(request, 'recommendationItems.html', {'user': user, 'items': items})
    form = UserForm()
    return render(request, 'searchUser.html', {'form': form})


def recommended_peripheral_items(request):
    if request.method == 'GET':
        form = UserForm(request.GET, request.FILES)
        if form.is_valid():
            id_user = form.cleaned_data['id']
            user = get_object_or_404(User, pk=id_user)
            shelf = shelve.open("dataRS.dat")
            Prefs = shelf['Prefs']
            sim_items = shelf['SimItems']
            rankings= []
            items=[]
            if (int(idUser) not in Prefs):
                return render(request,'recommendationItems.html', {'user': user, 'items': items})
            SimItems = shelf['SimItems']
            shelf.close()
            rankings = getRecommendedItems(Prefs, sim_items, int(id_user))
            recommended = rankings[:2]  # Change number of similar items recommended
            peripherals = []
            scores = []
            for re in recommended:
                peripherals.append(Peripheral.objects.get(pk=re[1]))
                scores.append(re[0])
            items = zip(peripherals, scores)
            return render(request, 'recommendationItems.html', {'user': user, 'items': items})
    form = UserForm()
    return render(request, 'searchUser.html', {'form': form})


def similar_peripherals(request):
    if request.method == 'GET':
        form = PeripheralForm(request.GET, request.FILES)
        if form.is_valid():
            id_peripheral = form.cleaned_data['id']
            peripheral = get_object_or_404(Peripheral, pk=id_peripheral)
            shelf = shelve.open("dataRS.dat")
            items_prefs = shelf['ItemsPrefs']
            shelf.close()
            recommended = topMatches(items_prefs, int(id_peripheral), n=3)  # n: number of similar items
            peripherals = []
            similar = []
            for re in recommended:
                peripherals.append(Peripheral.objects.get(pk=re[1]))
                similar.append(re[0])
            items = zip(peripherals, similar)
            return render(request, 'similarPeripherals.html', {'peripheral': peripheral, 'peripherals': items})
    form = PeripheralForm()
    return render(request, 'searchPeripheral.html', {'form': form})


def recommended_users_peripherals(request):
    if request.method == 'GET':
        form = PeripheralForm(request.GET, request.FILES)
        if form.is_valid():
            id_peripheral = form.cleaned_data['id']
            peripheral = get_object_or_404(Peripheral, pk=id_peripheral)
            shelf = shelve.open("dataRS.dat")
            prefs = shelf['ItemsPrefs']
            shelf.close()
            rankings = getRecommendations(prefs, int(id_peripheral))
            recommended = rankings[:3]  # number of recommended items
            peripherals = []
            scores = []
            for re in recommended:
                peripherals.append(User.objects.get(pk=re[1]))
                scores.append(re[0])
            items = zip(peripherals, scores)
            return render(request, 'recommendationUsers.html', {'peripheral': peripheral, 'items': items})
    form = PeripheralForm()
    return render(request, 'searchPeripheral.html', {'form': form})


def search(request):
    if request.method == 'GET':
        form = UserForm(request.GET, request.FILES)
        if form.is_valid():
            id_user = form.cleaned_data['id']
            user = get_object_or_404(User, pk=id_user)
            return render(request, 'ratedPeripherals.html', {'user': user})
    form = UserForm()
    return render(request, 'searchUser.html', {'form': form})
