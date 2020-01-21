import shelve
from main.models import User, Peripheral, Rating
from main.forms import UserForm, PeripheralForm
from django.shortcuts import render, get_object_or_404
from main.recommendations import  transformPrefs, calculateSimilarItems, getRecommendations, getRecommendedItems, topMatches
from main.populate import populate_db


# Funcion que carga en el diccionario Prefs todas las puntuaciones de usuarios a peliculas.´
#  Tambien carga el diccionario inverso y la matriz de similitud entre items.
# Serializa los resultados en dataRS.dat
def loadDict():
    Prefs={}   # matriz de usuarios y puntuaciones a cada a items
    shelf = shelve.open("dataRS.dat")
    ratings = Rating.objects.all()
    for ra in ratings:
        user = int(ra.user.id)
        itemid = int(ra.peripheral.id)
        rating = float(ra.rating)
        Prefs.setdefault(user, {})
        Prefs[user][itemid] = rating
    shelf['Prefs']=Prefs
    shelf['ItemsPrefs']=transformPrefs(Prefs)
    shelf['SimItems']=calculateSimilarItems(Prefs, n=10)
    shelf.close()
    


    
#  CONJUNTO DE VISTAS

def index(request): 
    return render(request,'index.html')

def populateDB(request):
    populate_db() 
    return render(request,'populate.html')

def loadRS(request):
    loadDict()
    return render(request,'loadRS.html')
 
# APARTADO A
def recommended_peripherals_user(request):
    if request.method=='GET':
        form = UserForm(request.GET, request.FILES)
        if form.is_valid():
            idUser = form.cleaned_data['id']
            user = get_object_or_404(User, pk=idUser)
            shelf = shelve.open("dataRS.dat")
            Prefs = shelf['Prefs']
            shelf.close()
            rankings = getRecommendations(Prefs,int(idUser))
            recommended = rankings[:2]
            peripherals = []
            scores = []
            for re in recommended:
                peripherals.append(Peripheral.objects.get(pk=re[1]))
                scores.append(re[0])
            items= zip(peripherals,scores)
            return render(request,'recommendationItems.html', {'user': user, 'items': items})
    form = UserForm()
    return render(request,'search_user.html', {'form': form})

# APARTADO B
def recommended_peripherals_items(request):
    if request.method=='GET':
        form = UserForm(request.GET, request.FILES)
        if form.is_valid():
            idUser = form.cleaned_data['id']
            user = get_object_or_404(User, pk=idUser)
            shelf = shelve.open("dataRS.dat")
            Prefs = shelf['Prefs']
            rankings= []
            items=[]
            print("Prefs:"+ str(Prefs))
            if (int(idUser) not in Prefs):
                return render(request,'recommendationItems.html', {'user': user, 'items': items})
            SimItems = shelf['SimItems']
            shelf.close()
            rankings = getRecommendedItems(Prefs, SimItems, int(idUser))
            recommended = rankings[:2]
            peripherals = []
            scores = []
            for re in recommended:
                peripherals.append(Peripheral.objects.get(pk=re[1]))
                scores.append(re[0])
            items= zip(peripherals,scores)
            return render(request,'recommendationItems.html', {'user': user, 'items': items})
    form = UserForm()
    return render(request,'search_user.html', {'form': form})

# APARTADO C
def similar_peripherals(request):
    peripheral = None
    if request.method=='GET':
        form = PeripheralForm(request.GET, request.FILES)
        if form.is_valid():
            idPeripheral = form.cleaned_data['id']
            peripheral = get_object_or_404(Peripheral, pk=idPeripheral)
            shelf = shelve.open("dataRS.dat")
            ItemsPrefs = shelf['ItemsPrefs']
            shelf.close()
            recommended = topMatches(ItemsPrefs, int(idPeripheral),n=3)
            peripherals = []
            similar = []
            for re in recommended:
                peripherals.append(Peripheral.objects.get(pk=re[1]))
                similar.append(re[0])
            items= zip(peripherals,similar)
            return render(request,'similarPeripherals.html', {'peripheral': peripheral,'peripherals': items})
    form = PeripheralForm()
    return render(request,'search_peripheral.html', {'form': form})

# APARTADO D
def recommended_users_peripherals(request):
    if request.method=='GET':
        form = PeripheralForm(request.GET, request.FILES)
        if form.is_valid():
            idPeripheral = form.cleaned_data['id']
            peripheral = get_object_or_404(Peripheral, pk=idPeripheral)
            shelf = shelve.open("dataRS.dat")
            Prefs = shelf['ItemsPrefs']
            shelf.close()
            rankings = getRecommendations(Prefs,int(idPeripheral))
            recommended = rankings[:3]
            peripherals = []
            scores = []
            for re in recommended:
                peripherals.append(User.objects.get(pk=re[1]))
                scores.append(re[0])
            items= zip(peripherals,scores)
            return render(request,'recommendationUsers.html', {'peripheral': peripheral, 'items': items})
    form = PeripheralForm()
    return render(request,'search_peripheral.html', {'form': form})
#APARTADO E
def search(request):
    if request.method=='GET':
        form = UserForm(request.GET, request.FILES)
        if form.is_valid():
            idUser = form.cleaned_data['id']
            user = get_object_or_404(User, pk=idUser)
            return render(request,'ratedPeripherals.html', {'usuario':user})
    form=UserForm()
    return render(request,'search_user.html', {'form':form })
