eachDayExpenses = {
    "Sunday" : 1000,
    "Monday" : 2000,
    "Tuesday" : 200,
    "Wednesday": 500,
    "Thursday": 700,
    "Friday": 900,
    "Saturday" : 5000
}

#totalExpenses = eachDayExpenses['Sunday']+
# eachDayExpenses["Monday"]+ 
# eachDayExpenses["Tuesday"]+ 
# eachDayExpenses["Wednesday"]+ 
# eachDayExpenses["Thursday"]+ 
# eachDayExpenses["Friday"]+ 
# eachDayExpenses["Saturday"]

#weeklyExpenses = totalExpenses / 7

weeklyExpenses = sum(eachDayExpenses.values()) / 7 
print(f"The average weekly expenses is : {weeklyExpenses}")