import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("Would you like to see data for Chicago,New York, or Washington?\n")
    month="no"
    day="no"
    while(1):
        if(city not in ['Chicago','New York','Washington']):
            print("\nChiRecheck the city you entered\n")
            city=input("Would you like to see data for Chicago,New York, or Washington?\n")
        else:
            fil=input("\nWould you like to filter the data  by month,day, both or not at all?Type none for no filter.\n")
            if(fil=="month"):
                month=input("\nWhich month?Jan ,Feb, Mar,Apr,May,June?Please type as shown.\n")
                while(month not in ['Jan','Feb','Mar','Apr','May','June']):
                    print("\nplease re-enter month\n")
                    month=input("\nWhich month?Jan ,Feb, Mar,Apr,May,June?Please type as shown.\n")
            elif(fil=="day"):
                day=input("\nWhich day?Please Type as Sunday\n")
                while(day not in ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']):
                    print("\nplease re-enter day\n")
                    day=input("\nWhich day?Please type as Sunday\n")
            elif(fil=="both"):
                month=input("Which month?Jan, Feb, Mar, Apr, May, June?Please type out as shown\n")
                while(month not in ['Jan','Feb','Mar','Apr','May','June']):
                    print("\nplease re-enter month\n")
                    month=input("\nWhich month?Jan ,Feb, Mar,Apr,May,June?Please type as shown.\n")
                day=input("Which day?Please type as Sunday\n")
                while(day not in ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']):
                    print("\nplease re-enter day\n")
                    day=input("\nWhich day?Please type as  Sunday\n")
            else:
                print("NO filter is applied\n")
        break
    print('-'*40.center(20))
    return city, month, day
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if(month!='no'):
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if(day!='no'):
        df = df[df['day_of_week'] == day.title()]
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print("What is the most popular month for travelling?")
    print(popular_month)
    # TO DO: display the most common day of week
    popular_day=df['day_of_week'].mode()[0]
    print("What is the most popular day for travelling?")
    print(popular_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print("What is the most popular hour for travelling?")
    print(popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40.center(20))

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("What was the most popular start station for travelling?")
    
    
    popular_start_station=df['Start Station'].mode()[0]
    print(popular_start_station)


    # TO DO: display most commonly used end station
    print("What was the most popular end station for travelling?")
    popular_end_station=df['End Station'].mode()[0]
    print(popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    print("What was the most popular trip?")
    df['trip']=df['Start Station']+'-'+df['End Station']
    popular_trip=str(df['trip'].mode()[0])
    l=popular_trip.split("-")
    print("Start station :  " ,l[0])
    print("End Station :   ", l[1])
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40.center(20))
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()
    print("\n Total travel time:  ",total_time)
    # TO DO: display mean travel time
    avg_time=df['Trip Duration'].mean()
    print("\n Average travel time:  ",avg_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40.center(20))
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("What is the breakdown  of users?" ,user_types)

    # TO DO: Display counts of gender
    if('Gender' in df):
        gender_count = df['Gender'].value_counts()
    else:
        gender_count="No Gender Data to Share"
    print("What is the breakdown  of gender?\n" ,gender_count)


    # TO DO: Display earliest, most recent, and most common year of birth
    print("What is the oldest , youngest, and most popular year of birth,respectively?\n")
    if('Birth Year' in df):
        oldest_year=int(df['Birth Year'].min())
        youngest_year=int(df['Birth Year'].max())
        popular_year=int(df['Birth Year'].mode()[0])
        print(oldest_year,youngest_year,popular_year)
    else:
        print("No Birth year data to share")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40.center(20))
#main function calls other functions
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
