# List in dictionary or dict in dict

travel_log = {
    "France" : ["Paris","Lille", "Djon"],
    "Germany" : ["Berlin","Hamburg", "Stuttgart"],
}


#travel_log = {
#    "France" : ["cities_visited" : ["Paris","Lille", "Djon"], "total_visit" : 12,],
#    "Germany" : ["Berlin","Hamburg", "Stuttgart"],
#}

dict_visit = {}
dict_visit["cities_visited"] = travel_log["France"]
dict_visit["total_visit"] = 12

travel_log["France"] = dict_visit

print(travel_log)