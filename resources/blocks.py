
blocks = {
    "0" : {
        "solid" : False, # I really don't think 'space' should be solid.
        "transparent" : 255, # I guess...
        "material" : "space.png",
        "damage" : 0,
        "health" : 1000000 # I don't know about this man.
    },
    "1" : {
        "solid" : True,
        "transparent" : 0,
        "material" : "vine.jpg",
        "damage" : 0,
        "health" : 10
    },
    "2" : {
        "solid" : True,
        "transparent" : 0,
        "material" : "stone.jpg",
        "damage" : 0,
        "health" : 40
    },
    "3" : {
        "solid" : False,
        "transparent" : 127,
        "material" : "lava.jpg", # this is actually 'cloud.jpg' with altered coloring
        "damage" : 1,
        "health" : 1000000
    }
}
