def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    return (food in person["favourites"]["snacks"])

def add_friend(person, friend):
    person["friends"].append(friend)

def remove_friend(person, friend):
    person["friends"].pop(person["friends"].index(friend))

def total_money(peoples):
    total = 0
    for people in peoples:
        total += people["monies"]
    
    return total

def lend_money(person2, person1, lended):
    person2["monies"] -= lended
    person1["monies"] += lended

def all_favourite_foods(peoples):
    favourite_foods = []
    for people in peoples:
        favourite_foods += people["favourites"]["snacks"]
    return favourite_foods

def find_no_friends(peoples):
    return [people for people in peoples if people["friends"] == []]

def unique_favourite_tv_shows(peoples):
    favourite_shows = []
    for people in peoples:
        if people["favourites"]["tv_show"] not in favourite_shows:
            favourite_shows.append(people["favourites"]["tv_show"])
    return favourite_shows
