# PAul Fralix, 06/28/2025, Assignment 7.2
# city_functions.py

def city_country(city, country, population=None, language=None):
    """Return string like:
       'Santiago, Chile - population 5000000, Spanish'
       or 'Santiago, Chile - population 5000000'
       or 'Santiago, Chile, Spanish'
       or just 'Santiago, Chile' depending on which optional args are provided.
    """
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result

# Example calls
print(city_country("santiago", "chile"))
print(city_country("paris", "france", 2148000))
print(city_country("tokyo", "japan", 13960000, "japanese"))
