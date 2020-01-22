import shelve
from main.models import User, Peripheral, Rating
from main.forms import UserForm, PeripheralForm
from django.shortcuts import render, get_object_or_404
from main.recommendations import transformPrefs, getHybridRecommendation, calculateSimilarItems, getRecommendations, \
    getRecommendedItems, topMatches
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


def populate_db_view(request):
    populate_db()
    msg = "Database loaded correctly"
    return render(request, 'index.html', {'msg': msg})


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
            prefs = shelf['Prefs']
            items = []
            if int(id_user) not in prefs:
                return render(request, 'recommendationItems.html', {'user': user, 'items': items})
            shelf.close()
            rankings = getRecommendations(prefs, int(id_user))
            recommended = rankings[:20]  # Change number of similar items recommended
            peripherals = []
            scores = []
            for re in recommended:
                peripherals.append(Peripheral.objects.get(pk=re[1]))
                scores.append(re[0])
            items = zip(peripherals, scores)
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
            prefs = shelf['Prefs']
            sim_items = shelf['SimItems']
            items = []
            if int(id_user) not in prefs:
                return render(request, 'recommendationItems.html', {'user': user, 'items': items})
            shelf.close()
            getHybridRecommendation(prefs, int(id_user), sim_items)
            rankings = getRecommendedItems(prefs, sim_items, int(id_user))
            recommended = rankings[:20]  # Change number of similar items recommended
            peripherals = []
            scores = []
            for re in recommended:
                peripherals.append(Peripheral.objects.get(pk=re[1]))
                scores.append(re[0])
            items = zip(peripherals, scores)
            return render(request, 'recommendationItems.html', {'user': user, 'items': items})
    form = UserForm()
    return render(request, 'searchUser.html', {'form': form})


def recommended_hybrid(request):
    if request.method == 'GET':
        form = UserForm(request.GET, request.FILES)
        if form.is_valid():
            id_user = form.cleaned_data['id']
            user = get_object_or_404(User, pk=id_user)
            shelf = shelve.open("dataRS.dat")
            prefs = shelf['Prefs']
            sim_items = shelf['SimItems']
            items = []
            if int(id_user) not in prefs:
                return render(request, 'recommendationItems.html', {'user': user, 'items': items})
            shelf.close()
            rankings = getHybridRecommendation(prefs, int(id_user), sim_items)
            recommended = rankings[:20]  # Change number of similar items recommended
            peripherals = []
            scores = []
            for re in recommended:
                peripherals.append(Peripheral.objects.get(pk=re[1]))
                scores.append(re[0])
            items = zip(peripherals, scores)
            return render(request, 'recommendationItems.html', {'user': user, 'items': items})
    form = UserForm()
    return render(request, 'searchUser.html', {'form': form})


def recommended_peripheral_user(request):
    if request.method == 'GET':
        form = UserForm(request.GET, request.FILES)
        if form.is_valid():
            id_user = form.cleaned_data['id']
            user = get_object_or_404(User, pk=id_user)
            shelf = shelve.open("dataRS.dat")
            prefs = shelf['Prefs']
            items = []
            if int(id_user) not in prefs:
                return render(request, 'recommendationItems.html', {'user': user, 'items': items})
            shelf.close()
            rankings = getRecommendations(prefs, int(id_user))
            recommended = rankings[:20]  # Change number of similar items recommended
            peripherals = []
            scores = []
            for re in recommended:
                peripherals.append(Peripheral.objects.get(pk=re[1]))
                scores.append(re[0])
            items = zip(peripherals, scores)
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
            prefs = shelf['Prefs']
            sim_items = shelf['SimItems']
            items = []
            if int(id_user) not in prefs:
                return render(request, 'recommendationItems.html', {'user': user, 'items': items})
            shelf.close()
            getHybridRecommendation(prefs, int(id_user), sim_items)
            rankings = getRecommendedItems(prefs, sim_items, int(id_user))
            recommended = rankings[:20]  # Change number of similar items recommended
            peripherals = []
            scores = []
            for re in recommended:
                peripherals.append(Peripheral.objects.get(pk=re[1]))
                scores.append(re[0])
            items = zip(peripherals, scores)
            return render(request, 'recommendationItems.html', {'user': user, 'items': items})
    form = UserForm()
    return render(request, 'searchUser.html', {'form': form})


def recommended_hybrid(request):
    if request.method == 'GET':
        form = UserForm(request.GET, request.FILES)
        if form.is_valid():
            id_user = form.cleaned_data['id']
            user = get_object_or_404(User, pk=id_user)
            shelf = shelve.open("dataRS.dat")
            prefs = shelf['Prefs']
            sim_items = shelf['SimItems']
            items = []
            if int(id_user) not in prefs:
                return render(request, 'recommendationItems.html', {'user': user, 'items': items})
            shelf.close()
            rankings = getHybridRecommendation(prefs, int(id_user), sim_items)
            recommended = rankings[:20]  # Change number of similar items recommended
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
            recommended = topMatches(items_prefs, int(id_peripheral), n=20)  # n: number of similar items
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
            items = []
            if int(id_peripheral) not in prefs:
                return render(request, 'recommendationUsers.html', {'peripheral': peripheral, 'items': items})
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


def __vista2_users(username):
    user = User.objects.get(username=username)
    user_id = user.pk

    shelf = shelve.open("dataRS.dat")
    prefs = shelf['Prefs']
    shelf.close()

    rankings = getRecommendations(prefs, int(user_id))
    recommended = rankings[:10]  # Change number of similar items recommended

    scores = []
    peripherals = []
    for re in recommended:
        peripherals.append(Peripheral.objects.get(pk=re[1]))
        scores.append(re[0])
    items = zip(peripherals, scores)
    return items


def __vista2_items(username):
    user = User.objects.get(username=username)
    user_id = user.pk

    shelf = shelve.open("dataRS.dat")
    prefs = shelf['Prefs']
    sim_items = shelf['SimItems']
    shelf.close()

    rankings = getRecommendedItems(prefs, sim_items, int(user_id))
    recommended = rankings[:10]  # Change number of similar items recommended

    scores = []
    peripherals = []
    for re in recommended:
        peripherals.append(Peripheral.objects.get(pk=re[1]))
        scores.append(re[0])
    items = zip(peripherals, scores)
    return items


def __vista2_hybrid(username):
    user = User.objects.get(username=username)
    user_id = user.pk

    shelf = shelve.open("dataRS.dat")
    prefs = shelf['Prefs']
    sim_items = shelf['SimItems']
    shelf.close()

    rankings = getHybridRecommendation(prefs, int(user_id), sim_items)
    recommended = rankings[:10]  # Change number of similar items recommended

    scores = []
    peripherals = []
    for re in recommended:
        peripherals.append(Peripheral.objects.get(pk=re[1]))
        scores.append(re[0])
    items = zip(peripherals, scores)
    return items


def vista2(request):
    recommendation_type = request.POST.get('select-recommendation-type')
    username = request.POST.get('username')

    items = []
    if recommendation_type == 'users':
        items = __vista2_users(username)
    if recommendation_type == 'items':
        items = __vista2_items(username)
    if recommendation_type == 'hybrid':
        items = __vista2_hybrid(username)

    list_items = list(items)
    return render(request, 'vista2.html', {'user': username, 'items': list_items})


def similar_items(request):
    peripheral_id = request.POST.get('id')
    peripheral = get_object_or_404(Peripheral, pk=peripheral_id)

    shelf = shelve.open("dataRS.dat")
    items_prefs = shelf['ItemsPrefs']
    shelf.close()

    recommended = topMatches(items_prefs, int(peripheral_id), n=9)  # n: number of similar items

    similar = []
    peripherals = []
    for re in recommended:
        peripherals.append(Peripheral.objects.get(pk=re[1]))
        similar.append(re[0])
    items = zip(peripherals, similar)

    list_items = list(items)
    return render(request, 'vista2.html', {'user': peripheral.name, 'items': list_items})
