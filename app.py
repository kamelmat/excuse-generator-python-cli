import random
excuse = "My Cat Peed on my homework this morning"

who = ["The Dog", "The Cat", "My Grandma", "My Sister", "An Alien"]
what = ["ate", "peed", "broke", "stole", "took"]
thing = ["my homework", "my snickers", "my meal", "my guitar", "my car"]
when = ["this morning", "yesterday", "before coming here"]

def generate_excuse():
    return random.choice(who) + " " +random.choice(what) + " " + random.choice(thing) +  " " + random.choice(when)
    
    
print(generate_excuse())

