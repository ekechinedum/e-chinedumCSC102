import pandas as pd

# Data for girls
girl_names = ["Evelyn", "Jessica", "Somto", "Edith", "Liza", "Madonna", "Waje", "Tola", "Aisha", "Latifa"]
girl_ages = [17, 16, 17, 18, 16, 18, 17, 20, 19, 17]
girl_heights = [5.5, 6.0, 5.4, 5.9, 5.6, 5.5, 6.1, 6.0, 5.7, 5.5]
girl_scores = [80, 85, 70, 60, 76, 66, 87, 95, 50, 49]

# Data for boys
boy_names = ["Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Wesley"]
boy_ages = [19, 16, 18, 17, 20, 19, 16, 18, 17, 19]
boy_heights = [5.7, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.8, 5.7]
boy_scores = [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]

# Combine data
names = girl_names + boy_names
ages = girl_ages + boy_ages
heights = girl_heights + boy_heights
scores = girl_scores + boy_scores

data = {
    "Name": names,
    "Age": ages,
    "Height": heights,
    "Score": scores
}

# Create DataFrame
df = pd.DataFrame(data)

# Display table
print(df)
