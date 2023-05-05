# Travel log dict
# List in dictionary or dict in dict

from pickle import APPEND


travel_log = [
 {
    "country" : "France" ,
    "visits" : 12,
    "cities" : ["Paris","Lille", "Djon"]
 },
 {
    "country": "Germany",
    "visits" : 5,
    "cities" : ["Berlin","Hamburg", "Stuttgart"]
 },
]


def add_new_country(str,nmr,lst):

    d = {}
    d["country"] = str
    d["visits"] = nmr
    d["cities"] = lst
    
    travel_log.append(d)


add_new_country("Russia",2,["Moscow","Saint Petersburg"])
print(travel_log)