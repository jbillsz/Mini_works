def City_country(city,country, population=""):
    """Takes string input city and country and prints together"""
    if population:
        city = f"{city}"
        country = f"{country}"
        population = f"{population}"
        return f"{city}, {country}: {population}".title()
    else:
        city = f"{city}"
        country = f"{country}"
        return f"{city}, {country}".title()


print(City_country("accra", "ghana", 5000))
