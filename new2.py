import pandas as pd
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt


file_path = 'salaries.csv'
data = pd.read_csv(file_path)

main_table = data.groupby('work_year').agg(
    total_jobs=('job_title', 'count'),
    average_salary_usd=('salary_in_usd', 'mean')
).reset_index()

main_table.columns = ['Year', 'Number of Total Jobs', 'Average Salary in USD']

main_table = main_table.sort_values(by='Year')

output_file_path = 'main_table.csv'

main_table.to_csv(output_file_path, index=False)


def get_aggregated_job_titles(data, year):
    filtered_data = data[data['work_year'] == year]
    job_counts = filtered_data['job_title'].value_counts().reset_index()
    job_counts.columns = ['Job Title', 'Number of Jobs']
    return job_counts


year_dropdown = widgets.Dropdown(
    options=main_table['Year'].unique(),
    description='Year:',
    value=main_table['Year'].iloc[0],
)


def update_table(year):
    aggregated_data = get_aggregated_job_titles(data, year)
    display(aggregated_data)


widgets.interactive(update_table, year=year_dropdown)

display(year_dropdown)

plt.figure(figsize=(10, 6))
plt.plot(main_table['Year'], main_table['Number of Total Jobs'], marker='o')
plt.title('Number of Total Jobs from 2020 to 2024')
plt.xlabel('Year')
plt.ylabel('Number of Total Jobs')
plt.grid(True)
plt.xticks(main_table['Year'])
plt.show()
