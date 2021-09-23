# Programmers: Callie Walker and Lesdy Galvez
# Course: CS151, Dr. Rajeev
# Date: 9/23/21
# Lab Number: 2
# Program Inputs: Births, Deaths, Migrations, and total population
# Program Outputs: Estimated population

population = float(input("Enter the current population: "))
births = float(input("Enter the amount of births per second: "))
deaths = float(input("Enter the amount of deaths  per second: "))
migration = float(input("Enter the amount of migrations per second: "))
years = float(input("Enter the future amount of years: "))

daysInYear = 365 * years
totalBirths = (((births*60) * 60) * 24) * daysInYear
totalDeaths = (((deaths*60) * 60) * 24) * daysInYear
totalMigrations = (((migration*60) * 60) * 24) * daysInYear
estimatedPop =  estimatedPop = population + totalBirths - totalDeaths + totalMigrations
if estimatedPop < 0:
    print("The population has died out")
elif estimatedPop > 0:
    print("Estimated population in ", years, " years is ", estimatedPop)





