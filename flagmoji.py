# imports flags database
from data import flags

# initializes two dictonaries that will store the emoji flags for each name/code
dataCode = {}
dataName = {}

# fills dictonaries with flags for each name/code
for flag in flags:
    dataCode[flag['code']] = flag['emoji']
    dataName[flag['name']] = flag['emoji']

# function to return emoji flag for given country code
def byCode(country_code):
    if country_code in dataCode:
        return dataCode[country_code]
    return None

# function to return emoji flag for given country name
def byName(country_name):
    if country_name in dataName:
        return dataName[country_name]
    return None
