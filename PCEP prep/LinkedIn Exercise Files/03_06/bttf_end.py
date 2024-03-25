back_to_the_future = {
    "title": "Back to the Future",
    "release_year": 1985,
    "director": "Robert Zemeckis",
    "producer": "Bob Gale",
    "lead_actors": ["Michael J. Fox", "Christopher Lloyd", "Lea Thompson", "Crispin Glover"],
    "genre": "Sci-Fi, Adventure, Comedy",
    "runtime_minutes": 116
}

keys = back_to_the_future.keys()
values = back_to_the_future.values()

items = back_to_the_future.items()
back_to_the_future.pop("plot_summary")

print(items)
# for k in keys:
#     print(k, back_to_the_future[k], sep="=")




# print(back_to_the_future)