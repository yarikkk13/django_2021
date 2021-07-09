from django.shortcuts import render

users_list = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "email": "Sincere@april.biz"
    },
    {
        "id": 2,
        "name": "Ervin Howell",
        "email": "Shanna@melissa.tv",
    },
    {
        "id": 3,
        "name": "Clementine Bauch",
        "email": "Nathan@yesenia.net"
    },
    {
        "id": 4,
        "name": "Patricia Lebsack",
        "email": "Julianne.OConner@kory.org"
    },
    {
        "id": 5,
        "name": "Chelsey Dietrich",
        "email": "Lucio_Hettinger@annie.ca"
    },
    {
        "id": 6,
        "name": "Mrs. Dennis Schulist",
        "email": "Chaim_McDermott@dana.io"

    },
    {
        "id": 7,
        "name": "Kurtis Weissnat",
        "email": "Telly.Hoeger@billy.biz"
    },
    {
        "id": 8,
        "name": "Nicholas Runolfsdottir V",
        "email": "Sherwood@rosamond.me"
    },
    {
        "id": 9,
        "name": "Glenna Reichert",
        "email": "Chaim_McDermott@dana.io"
    }
]


# Create your views here.


def home(request):
    return render(request, 'index.html', {'users': users_list})


def add_user(request, id, name):
    users_list.append({'id': id, 'name': name})
    return render(request, 'index.html', {'users': users_list})


def delete_user(request, id):
    for user in users_list:
        if user.get('id') == id:
            users_list.remove(user)
    return render(request, 'index.html', {'users': users_list})
