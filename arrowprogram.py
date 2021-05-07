import arrow

def main():
    currentDate= arrow.get(arrow.utcnow().format('DD-MM-YYYY'),'DD-MM-YYYY')
    userResponse = input("When were you born?(Format answer in DD-MM-YYYY) ")
    birthDate = arrow.get(userResponse,'DD-MM-YYYY')
    diffInDates= currentDate - birthDate
    days= diffInDates.days
    years = int(days/365)
    print("\nYou are "+str(years)+" years old!")

main()
