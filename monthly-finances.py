monthly_expenses = {}
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
def monthly_finances():
    month = (input(f"Please input the month for where you want to store your salary: "))
    while month not in months:
        print(f"Please enter a valid month From this list {months}")
        month = input(f"Please input the month for where you want to store your salary: ")
    while month !="exit":
        if month in monthly_expenses:
            print(f"Data for {month} has already been entered. Please enter a different month.")
            month = input(f"Please input the next month (or type 'exit' to stop): ")
            continue
        salary = int(input(f"Please input the salary for {month}: "))
        savings_percentage = float(input(f"Please input the savings percentage for {month}: "))
        rent_percentage = float(input(f"Please input the rent percentage for {month}: "))
        electricity_percentage = float(input(f"Please input the electricity bill percentage for {month}: "))

        savings = (savings_percentage / 100) * salary
        rent = (rent_percentage / 100) * salary
        electricity = (electricity_percentage / 100) * salary
        monthly_expenses[month] = {
            "salary": salary,
            "savings": savings,
            "rent": rent,
            "electricity": electricity,
        }
        month = input("Please input the next month (or type 'exit' to stop): ")
        while month in monthly_expenses or month not in months and month !="exit" :
            print(f"Please enter a valid month From this list {months}")
            print("Months entered so far:")
            for month in monthly_expenses:
                print(month)
            month = input(f"Please input the month for where you want to store your salary: ")
    return monthly_expenses

def amount_allocated():
    total_amount_allocated_savings = 0
    total_amount_allocated_rent = 0
    total_amount_allocated_electricity = 0

    for details in monthly_expenses.values():
        total_amount_allocated_savings += details["savings"]
        total_amount_allocated_rent += details["rent"]
        total_amount_allocated_electricity += details["electricity"]
    print("\n==============================================")
    print("            ALLOCATED AMOUNTS          ")
    print("==============================================")
    print(f"Total allocated savings: ${total_amount_allocated_savings}")
    print(f"Total allocated rent: ${total_amount_allocated_rent}")
    print(f"Total allocated electricity: ${total_amount_allocated_electricity}")
    print(f"Total amount spent on savings, rent, and electricity combined: ${total_amount_allocated_savings + total_amount_allocated_rent + total_amount_allocated_electricity}")
    print("==============================================\n")
    return total_amount_allocated_savings + total_amount_allocated_rent + total_amount_allocated_electricity

def remainder_amount(allocated):
    total_salary = 0
    for details in monthly_expenses.values():
        total_salary += details["salary"]
    remainder_from_salary = total_salary - allocated
    print("\n==============================================")
    print("            REMAINING AMOUNT           ")
    print("==============================================")
    print(f"Total remainder amount: ${remainder_from_salary}")
    print("==============================================\n")

def yearly_rent_electricity():
    total_rent_electricity = 0
    num_months = len(monthly_expenses)
    for details in monthly_expenses.values():
        total_rent_electricity += details["rent"] + details["electricity"]
    if num_months == 12:
        return total_rent_electricity
    average_monthly_rent_electricity = total_rent_electricity / num_months
    projected_yearly_rent_electricity = average_monthly_rent_electricity * 12
    print("\n==============================================")
    print("    ESTIMATED ANNUAL RENT & ELECTRICITY  ")
    print("==============================================")
    print(f"Estimate annual cost for rent & electricity ${projected_yearly_rent_electricity}")
    print("==============================================\n")

def hopeful_salary():
    month = (input(f"Please input the month for where you want to square your salary: "))
    while month not in monthly_expenses:
        for month in monthly_expenses:
            print(month)
        month = (input(f"Please input valid month for where you want to square your salary: "))
    total_salary = monthly_expenses.get(month, {}).get("salary")
    squared_salary = total_salary ** 2
    print("\n==============================================")
    print(f"           HOPEFUL SALARY ({month})         ")
    print("==============================================")
    print(f"Squared salary: ${squared_salary}")
    print("==============================================\n")

def additional_random_amount():
    total_savings = 0
    for details in monthly_expenses.values():
        total_savings += details["savings"]
    rand_number = int((input(f"Please enter a random number you want to save from your saving: ")))
    allocated_savings = total_savings/rand_number
    print("\n==============================================")
    print("      RANDOM ALLOCATED SAVINGS         ")
    print("==============================================")
    print(f"Random amount allocated for ${rand_number}: {allocated_savings}")
    print("==============================================\n")

monthly_finances()
allocated_amount = amount_allocated()
remainder_amount(allocated_amount)
yearly_rent_electricity()
hopeful_salary()
additional_random_amount()

