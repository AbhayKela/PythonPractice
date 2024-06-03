from countryinfo import CountryInfo
#countryinfo - library
country = CountryInfo(input("Enter Country Name: "))

#CountryInfo - class
#various infromation about the country
#name, capital etc. - method definition
print("Country Name: ", country.name())
print("Country Capital: ", country.capital())
print("Country Population: ", country.population())
print("Area (in sq.km.): ", country.area())
print("Region: ", country.region())
print("Subregion: ", country.subregion())
print("Denonyms: ", country.demonym())
print("Currency: ",country.currencies())
print("Language: ", country.languages())
print("Borders: ", country.borders())