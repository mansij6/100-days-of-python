captials = {
    "france": "paris",
    "germany": "berlin,"
}

travel_log = {
    "france": ["paris", "lille", "dijon"],
    "germany": ["stuttgart", "berlin"],

}

print(travel_log["france"][1])

travel_log = {
    "france": {
        "num_times_visited": 8,
        "cities_visited": ["paris", "lille", "dijon"],
        "total_visited": 12
    } ,
    "germany": {
        "cities_visited": ["berlin", "hamburg", "stuttgart"],
        "total_visited": 5
    },
}
print(travel_log["germany"]["cities_visited"][2])
