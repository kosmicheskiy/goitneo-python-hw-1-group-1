from datetime import datetime
from collections import defaultdict 

users = [{"name": "Bill Two", "birthday": datetime(1955, 3, 2)}, 
         {"name": "Bill Three", "birthday": datetime(1955, 3, 3)}, 
         {"name": "Bill Four", "birthday": datetime(1955, 3, 4)},
         {"name": "Bill Five", "birthday": datetime(1955, 3, 5)}, 
         {"name": "Bill Six", "birthday": datetime(1955, 3, 6)}, 
         {"name": "Bill Seven", "birthday": datetime(1955, 3, 7)},  
         {"name": "Bill Eight", "birthday": datetime(1954, 3, 8)},
         {"name": "Bill Nine", "birthday": datetime(1954, 3, 9)},
         {"name": "Bill Ten", "birthday": datetime(1954, 3, 10)},
         {"name": "Bill Eleven", "birthday": datetime(1954, 3, 10)},
         {"name": "Bill Twelve", "birthday": datetime(1954, 3, 12)}
         ] 

def get_birthdays_per_week(users):
    result = defaultdict(list) 
    today = datetime.today().date()
    
    for user in users:
        name = user["name"]
        birthday_this_year = user["birthday"].date().replace(year=today.year)

        if(birthday_this_year < today):
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                   
        delta_days = (birthday_this_year - today).days       

        if(delta_days < 7):     
            week_day = birthday_this_year.strftime("%A")              
            if (week_day.lower() in ["saturday", "sunday"]): 
                result['Monday'].append(name)
            else:               
                result[week_day].append(name)

        
    for day, names in result.items():
        print(f"{day}: {names}")             


get_birthdays_per_week(users=users)
