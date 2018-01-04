# uses random module to assemble fake first and last names with ages

import random

first_names = [
    "Albert", "Anne", "Bill", "Beth", "Collin", "Cindy", "Christina",
    "Daniel", "Dianne", "Emmett", "Emily", "Fred", "Franny",
    "Gus", "Gail", "Hank", "Harriet", "Ian", "Ines",
    "Joshua", "Jill", "Kevin", "Kalyn", "Lou", "Laura",
    "Miles", "Megan", "Nathan", "Naomi", "Owen", "Ophelia",
    "Peter", "Patty", "Quinten", "Queeny", "Randy", "Rachel",
    "Seth", "Sally", "Thomas", "Tatiana", "Uke", "Ursula",
    "Vincent", "Valerie", "William", "Winny", "Xander", "Xena",
    "Yogi", "Yolanda", "Zach", "Zoe"
    ]
    
last_names = [
    "Anderson", "Briggs", "Cook", "Douglas", "Everett", "Fisher",
    "Gillings", "Henderson", "Ingram", "Johnson", "Kardashian", "Louis",
    "Manning", "North", "O'Neil", "Prescott", "Quigley", "Roth",
    "Smith", "Taber", "Ulysses", "Von", "West", "Xan",
    "Young", "Ziggler", "Alberts", "Blair", "Cotton", "Duke",
    "Engel", "Fritz", "Graber", "Hallman", "Indigo", "Jacobes",
    "Kline", "Lane", "Madison", "Neighbor", "Otts", "Pinkman",
    "Queen", "Rodriquez", "Solebury", "Trevose", "Unami", "Valero",
    "Waterman", "Xtra", "Yanni", "Zep"
    ]
 
for i in range(30):    
    first = random.choice(first_names)
    last = random.choice(last_names)
    age = random.randint(1,100)
    print(
        first + " " + last + "\n"
        "Age: " + str(age)
        )
    