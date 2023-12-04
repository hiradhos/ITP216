# Hirad Hosseini, hiradhos@usc.edu
# ITP 216, Fall 2023
# Section: 32081
# HW 13
# Description:
# Describe what this program does in your own words such as:
'''
This program utilizes our learnings from the Scientific Visualization module (including Pandas and Matplotlib) in order
to construct two plots of NOAA historical daily temperature data for a particular ZIP code of our choosing. The top line
plot shows trendlines for the ten most recent years in the database while the bottom barplot shows the daily temps for the
most current year compared to the historical average for that given day.
'''

import pandas as pd
import matplotlib.pyplot as plt


def main():
    # reading in the dataset
    df = pd.read_csv("UPDATED_weather.csv")
    '''
    My dataset represents the same ZIP code of 17701 from the HW demo but is updated to include the most current year
    of 2023. My other datasets for Little Rock, AR and Los Angeles, CA had faults that precluded proper pre-processing
    and plotting.
    '''

    # removing rows of data where the observed temp is null
    df = df[df["TOBS"].notnull()]

    # making a column for year: allows us to easily get the last 10 years
    df["YEAR"] = df["DATE"].str[0:4]
    years_list = list(df["YEAR"].unique())

    # making a column for month: allows us to group by month
    df["MONTH_DAY"] = df["DATE"].str[-5:]
    df = df[df['MONTH_DAY'] != '02-29']  # drop leap years
    month_days_list = list(df["MONTH_DAY"].unique())

    df.sort_values(inplace=True, by='MONTH_DAY')
    print(df[['DATE', 'YEAR', 'MONTH_DAY', 'TOBS']])

    # list of months to label the x-axis of both graphs
    month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    fig, ax = plt.subplots(2,1) #Contains two subplots, with top plot showing trendlines for temperature across most recent 10 years and the bottom plot showing barplots comparing current
    #year daily temps to historical averages
    #I had to utilize the updated ZIP code dataset for 17701 since my initial dataset for Little Rock, AR and Los Angeles, CA had some pre-processing issues
    fig.suptitle("Yearly climatological data for ZIP Code 17701 from 1911 to 2023")
    xtickrange = range(0,365,31) #Represents each month on the x-axis

    #Top plot showing temperature trends across past 10 years
    ax[0].set_xticks(xtickrange)
    ax[0].set_xticklabels(month_list) #Labels the x-axis with the months
    ax[0].set(title="Most recent 10 recorded years", xlabel="Month", ylabel="Temp (°F)")
    colors = ["red", "blue", "green", "black", "pink", "yellow", "orange", "purple", "cyan", "brown"] #will be used for constructing legend
    year_groups = df.groupby('YEAR')
    years_list_num = [int(yr) for yr in years_list] #creates numerical list to allow for sorting
    years_list_num_sorted = sorted(years_list_num) #sorts the list of numerical years available in the dataset
    recent_years_list = years_list_num_sorted[-10:] #filters the dataset to include only ten most recent years
    for year, year_group in year_groups:
        if int(year) in recent_years_list: #checks if df grouping is among the ten most recent years
            color = colors.pop(0) #assigns a color to the particular year for legend construction
            ax[0].plot(year_group['MONTH_DAY'], year_group['TOBS'], label=f"{year}", color=color) #plots year trendline
    ax[0].legend()
    ax[0].grid()

    #Bottom plot showing current year vs. historical averages for temperature
    current_year = "2023" #can change this script yearly if desired
    ax[1].set_xticks(xtickrange)
    ax[1].set_xticklabels(month_list)
    ax[1].set(title="Comparing current year and historical averages", xlabel="Month", ylabel="Temp (°F)")
    current_year_df = df[df['YEAR'] == current_year].drop_duplicates() #contains current year data
    historical_df = df[df['YEAR'] != current_year].drop_duplicates() #contains historical data
    historical_averages = []
    ''' 
    NOTE: Typically we could use the snippet "current_year_temps = list(current_year_df)" to construct a list
    of all month dates for the current year. However, if we only have a limited subset of these dates (i.e. the year
    isn't over), then we have to use the alternative approach below. 
    '''
    current_year_temps = []
    current_year_groups = current_year_df.groupby("MONTH_DAY")
    current_month_days_list = [monthday for monthday in month_days_list if monthday in current_year_df['MONTH_DAY'].unique()]
    #we have to filter the current_month_days to include only dates up to the last collection day of the dataset
    #to prevent interference from historical data

    #This for loop checks if a particular month_day is missing in the current_year dataset and assigns a value of 0
    #if that is the case to allow for easy plotting
    for month_day in current_month_days_list:
        try:
            month_day_group = current_year_groups.get_group(month_day)
            day_temp = month_day_group['TOBS'].mean()
        except Exception:
            day_temp = 0
        current_year_temps.append(day_temp)
    while len(current_year_temps) < 365: #fills out the remainder of the year with values of 0 to allow for plotting
        current_year_temps.append(0)

    #This for loops obtains the historical average temp values across all month-days; if a given month-day were to be
    #missing from the historical data for some reason, it assigns a value of 0 to allow for plotting
    historical_groups = historical_df.groupby("MONTH_DAY")
    for month_day in month_days_list:
        month_day_group = historical_groups.get_group(month_day)
        if len(month_day_group) == 0:
            average_temp = 0
        else:
            average_temp = month_day_group['TOBS'].mean()
        historical_averages.append(average_temp)
    ax[1].bar(month_days_list, historical_averages, color="red", label="historical average")
    ax[1].bar(month_days_list, current_year_temps, color="blue", label=current_year)
    ax[1].legend()
    ax[1].grid()
    fig.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
