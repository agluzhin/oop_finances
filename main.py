class Finances:

    # Class methods
    data = {}

    def show_data():
        for key, value in Finances.data.items():
            print(key, ':', value)

    def show_user_total_balance():
        for key in Finances.data.keys():
            print(f"The total balance of {key} is equal: {
                Finances.data[key]["income"] - Finances.data[key]["expenditure"]}")

        # Object methods
    def __init__(self, name, income, expenditure):
        self.name = name
        self.income = income
        self.expenditure = expenditure

    def add_information(self):
        Finances.data[f"{self.name}"] = {
            "income": self.income, "expenditure": self.expenditure}

    def delete_information(self):
        Finances.data.pop(self.name, None)

    def change_information(self, other_profits, other_losses):
        Finances.data[f"{self.name}"]["income"] += other_profits
        Finances.data[f"{self.name}"]["expenditure"] += other_losses


# Create objects
first_user = Finances('alex', 10000, 5000)
second_user = Finances('efim', 10000, 3000)
third_user = Finances('alyona', 15000, 1000)

# Add infrotmation about users to the storage "data"
first_user.add_information()
second_user.add_information()
third_user.add_information()

# Show the whole storage information
Finances.show_data()

# Show information about user's total balance
Finances.show_user_total_balance()

# Change some information about user's icome and expenditures
first_user.change_information(1200, 700)
second_user.change_information(8700, 4600)
third_user.change_information(3900, 2800)

# Show information from "data" after changing
Finances.show_data()
