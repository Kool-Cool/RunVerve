import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from db_admin import df_dict

print(df_dict.keys())

# Q1) Total amount of Donnation (numerical)
# Q2) Highest Donation  (numerical)
# Q3) Total number of Donors (numerical)
# Q4) Most Contributer (decreasing bar graph for first 10)
# Q5) Location where most trees where planted (pie chart)
# Q6) Heath % of trees (piechart)


'''
Need more data for that !!!!

1. User Analytics:
    - How many users have registered each month?
    - What is the geographical distribution of users based on their addresses?
    - How many users are admins?

2. Species Analytics:
    - What are the most common species in the database?
    - How many species are there in the database?

3. Tree Analytics:
    - How many trees have been planted each month?
    - What is the average height and diameter of the trees?
    - What is the health status distribution of the trees (e.g., how many trees are in each health status category)?
    - What are the most common locations for tree planting?

4. Adoption Analytics:
    - How many adoptions have been made each month?
    - What is the total donation amount each month?
    - Which user has adopted the most trees?
    - Which tree species is most commonly adopted?
'''



users_df = df_dict['users_df']
species_df = df_dict['species_df']
trees_df = df_dict['trees_df']
adoptions_df = df_dict['adoption_df']

# DateTime
users_df['registration_date'] = pd.to_datetime(users_df['registration_date'])
trees_df['planted_date'] = pd.to_datetime(trees_df['planted_date'])
adoptions_df['adoption_date'] = pd.to_datetime(adoptions_df['adoption_date'])

#Numerical
adoptions_df['donation_amount'] = pd.to_numeric(adoptions_df['donation_amount'], errors='coerce')



# Create the directory if it doesn't exist
os.makedirs('extra', exist_ok=True)

# Q1) Total amount of Donation (numerical)
total_donation = adoptions_df['donation_amount'].sum()
# print(f"Total Donation: {total_donation}")

# Q2) Highest Donation (numerical)
highest_donation = adoptions_df['donation_amount'].max()
# print(f"Highest Donation: {highest_donation}")

# Q3) Total number of Donors (numerical)
total_donors = adoptions_df['user_id'].nunique()
# print(f"Total Number of Donors: {total_donors}")

# Q4) Most Contributor (decreasing bar graph for first 10)
most_contributors = adoptions_df.groupby('user_id')['donation_amount'].sum().nlargest(10)
most_contributors.plot(kind='bar', figsize=(10,6))
plt.title('Top 10 Contributors')
plt.xlabel('User ID')
plt.ylabel('Total Donations')
plt.savefig('extra/top_10_contributors.png')
plt.close()

# Q5) Location where most trees were planted (pie chart)
tree_locations = trees_df['location'].value_counts()
tree_locations.plot(kind='pie', figsize=(10,6), autopct='%1.1f%%')
plt.title('Tree Planting Locations')
plt.ylabel('')  # This hides the 'location' ylabel
plt.savefig('extra/tree_planting_locations.png')
plt.close()

# Q6) Health % of trees (pie chart)
health_percentage = trees_df['health_status'].value_counts(normalize=True)
health_percentage.plot(kind='pie', figsize=(10,6), autopct='%1.1f%%')
plt.title('Health Status Distribution')
plt.ylabel('')  # This hides the 'health_status' ylabel
plt.savefig('extra/health_status_distribution.png')
plt.close()

# print("done")
