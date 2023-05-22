pop_dict = {"The Matrix":["Keanu Reeves", "Carrie-Anne Moss", "Hugo Weaving"],
            "Jack Ryan": ["John Krasinski", "Wendell Pierce", "Abbie Cornish"],
            "Harry Potter": ["Daniel Ratcliffe", "Emma Watson", "Rupert Grint"],
            "Friends": ["Jennifer Aniston", "Courtney Cox", "Lisa Kudrow"],
            "The Office": ["Steve Carell", "Rain Wilson", "John Krasinski"]}

def get_cast(title):
    if title in pop_dict:
        return pop_dict[title]
    else:
        return []

def add_title(title, cast_list):
    pop_dict[title] = cast_list

def count_actors():
    actors = dict()
    for cast_list in pop_dict.values():
        for actor in cast_list:
            if actor in actors:
                actors[actor] += 1
            else:
                actors[actor] = 1
    return actors


#Test
print(get_cast("Star Wars"))
#add_title("Breaking Bad", ["Bryan Cranston", "Aaron Paul", "Anna Gunn"])
print(pop_dict)
print(count_actors())