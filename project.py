zodiac1 = {1: ['Capricorn','Aquarius',19],
        2: ['Aquarius','Pisces',18],
        3: ['Pisces','Aries',20],
        4: ['Aries','Taurus',19],
        5: ['Taurus','Gemini',20],
        6: ['Gemini','Cancer',20],
        7: ['Cancer','Leo',22],
        8: ['Leo','Virgo',22],
        9: ['Virgo','Libra',22],
        10: ['Libra','Scorpio',21],
        11: ['Scorpio','Sagittarius',21],
        12: ['Sagittarius','Capricorn',21]
        }

water = ['Cancer', 'Scorpio', 'Pisces']
earth = ['Capricorn', 'Taurus', 'Virgo']
fire = ['Aries', 'Leo', 'Sagittarius']
air = ['Gemini', 'Aquarius', 'Libra']

zodiac2 = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse",
         "Sheep", "Monkey", "Rooster", "Dog", "Pig"]

group100 = [['Rat','Dragon','Monkey'],['Ox', 'Snake', 'Rooster'],
        ['Tiger','Horse','Dog'],['Rabbit','Sheep','Pig']]
group25 = [['Horse','Rooster'],['Tiger','Dragon','Horse','Sheep'],
        ['Ox','Tiger','Snake','Monkey'],['Snake','Rooster'],['Ox','Sheep','Dog'],
        ['Tiger','Rabbit','Snake','Sheep','Pig'],['Rat','Ox','Rooster','Horse'],
        ['Ox','Tiger','Dog'],['Tiger','Pig'],['Rat','Rabbit','Horse','Rooster','Dog'],
        ['Dragon','Sheep','Rooster'],['Snake','Monkey']]

mylist = []
partnerlist = []
def zodiac_sign(day, month, year): 
    index1 = lambda x:0 if int(x) <zodiac1[month][2] else 1
    index2 = (year - 1900) % 12
    z_sign = zodiac1[month][index1(day)]
    ch_sign = zodiac2[index2]
    print(z_sign, ch_sign)
    
    if not mylist:
        mylist.append(ch_sign)
        mylist.append(z_sign)
    else:
        partnerlist.append(ch_sign)
        partnerlist.append(z_sign)
        
        
        
    return z_sign, ch_sign



user_day, user_month, user_year = input("Your day/month/year of birth: ").split()
user_day = int(user_day)
user_month = int(user_month)
user_year = int(user_year)
user_signs = zodiac_sign(user_day, user_month, user_year)


partner_day, partner_month, partner_year = input("Your partner's day/month/year of birth: ").split()
parner_day = int(partner_day)
partner_month = int(partner_month)
partner_year = int(partner_year)
partner_signs = zodiac_sign(partner_day, partner_month, partner_year)

#compatibility test

z_compatibility = 0
ch_compatibility = 0


if mylist[1] in earth:
    if partnerlist[1] in water:
        z_compatibility = 100
    elif partnerlist[1] in earth:
        z_compatibility = 75
    elif partnerlist[1] in air:
        z_compatibility = 50
    else:
        z_compatibility = 25
elif mylist[1] in water:
    if partnerlist[1] in earth:
        z_compatibility = 100
    elif partnerlist[1] in water:
        z_compatibility = 75
    elif partnerlist[1] in fire:
        z_compatibility = 50
    else:
        z_compatibility = 25
elif mylist[1] in fire:
    if partnerlist[1] in air:
        z_compatibility = 100
    elif partnerlist[1] in fire:
        z_compatibility = 75
    elif partnerlist[1] in water:
        z_compatibility = 50
    else:
        z_compatibility = 25
elif mylist[1] in air:
    if partnerlist[1] in fire:
        z_compatibility = 100
    elif partnerlist[1] in air:
        z_compatibility = 75
    elif partnerlist[1] in earth:
        z_compatibility = 50
    else:
        z_compatibility = 25

if mylist[0] in group100[0] and partnerlist[0] in group100[0] or mylist[0] in group100[1] and partnerlist[0] in group100[1] or mylist[0] in group100[2] and partnerlist[0] in group100[2] or mylist[0] in group100[3] and partnerlist[0] in group100[3]:
        ch_compatibility = 100
        print ("Compatibility = ", (z_compatibility + ch_compatibility)/2, "%")

elif partnerlist[0] in group25[zodiac2.index(mylist[0])]:
        ch_compatibility = 33
        print ("Compatibility = ", (z_compatibility + ch_compatibility)/2, "%")
else:
        ch_compatibility = 66
        print ("Compatibility = ", (z_compatibility + ch_compatibility)/2, "%")

