from django.shortcuts import render
import requests
base_url = 'https://api.jikan.moe/v4/anime/'

animeID_dir = {
    'One_Piece': '21',
    'Gintama': '918',
    'Dragon_Ball_Z': '813',
    'Attack_on_Titan': '48583',
    'Grand_Blue': '37105',
    'Death_Note': '1535',
    'Hunter_x_Hunter': '11061',
    'Full_Metal_Alchemist__Brotherhood': '5114',
    'Naruto': '20',
    'Steins_Gate': '9253',
}


def home_view(request):
    if request.method == 'POST':
        print(request.POST)

    context = {}

    for anime in animeID_dir:
        try:
            x = base_url + animeID_dir[anime]
            fin_data = requests.get(x).json()
            context[anime] = fin_data['data']['score']
        except:
            context[anime] = '8.77'

    return render(request, "index.html", context)
