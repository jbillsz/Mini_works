def City_country(city,country):
    """Takes string input city and country and prints together"""

    city = f"{city}"
    country = f"{country}"
    return f"{city}, {country}".title()

print(City_country("accra", "ghana"))
