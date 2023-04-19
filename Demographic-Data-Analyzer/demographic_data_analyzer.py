import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby(['race'])['race'].count()

    # What is the average age of men?
    average_age_men = df[df.sex == 'Male'].mean()
    average_age_men = round(average_age_men['age'],1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(((df[df.education == 'Bachelors']['education'].count()) / len(df)) * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    her = df[df.salary == '>50K'].query("education == 'Bachelors' or education == 'Masters' or education == 'Doctorate'").count()
    her = her.iloc[0]
    her_total = df.query("education == 'Bachelors' or education == 'Masters' or education == 'Doctorate'").count()
    her_total = her_total.iloc[0]
    higher_education = round((her/her_total) * 100, 1)
    ler = df[df.salary == '>50K'].query("education != 'Bachelors' and education != 'Masters' and education != 'Doctorate'").count()
    ler = ler.iloc[0]
    ler_total = df.query("education != 'Bachelors' and education != 'Masters' and education != 'Doctorate'").count()
    ler_total = ler_total.iloc[0]
    lower_education = round((ler/ler_total) * 100, 1)

    # percentage with salary >50K
    higher_education_rich = higher_education
    lower_education_rich = lower_education

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df.sort_values(by='hours-per-week').iloc[0,12]

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df = df.rename(columns={"hours-per-week" : "hours_per_week"})
    hpw = df[df.salary == '>50K'].query('hours_per_week == 1').count()
    hpw = hpw.iloc[0]
    hpw_total = df.query('hours_per_week == 1').count()
    hpw_total = hpw_total.iloc[0]
  
    num_min_workers = hpw
    rich_percentage = (hpw / hpw_total) * 100

    # What country has the highest percentage of people that earn >50K?
    df = df.rename(columns={"native-country" : "native_country"})
    hec = df[df.salary == '>50K'].groupby(['native_country'])[['salary']].count()
    hec_total = df.groupby(['native_country'])[['salary']].count()
    aux = (hec/ hec_total)*100
    aux = aux.sort_values(by='salary',ascending=False).reset_index()
    aux1 = aux.iloc[0,1]
    
    highest_earning_country = aux.iloc[0,0]
    highest_earning_country_percentage = round(aux1,1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_india = df[df.native_country == 'India'].groupby(['salary','occupation'])['occupation'].count().reset_index(name='QTD')
    top_india  = top_india.sort_values(by='QTD', ascending=False)
    top_IN_occupation = top_india.iloc[0,1]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
