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
    city = input('Please enter the city name from these cities (chicago, washington, new york city) : ')
    city = city.lower()
    
    #ask th user to enter a city
    while city not in ['chicago' ,'washington' , 'new york city']:
        print(' Please enter the correct city')
        city = input('Please enter the city name from these cities (chicago, washington, new york city) ')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please enter a month from january to june please write the full word or write  all if you want all months: ')
    month = month.lower()
    
    # ask th user to enter a month
    while month not in ['january', 'february', 'march', 'april', 'may', 'june','all']:
        print(' Please enter the correct month')
        month = input('Please enter a month from january to june please write the full word or write  all if you want all months: ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter a day from a week like(sunday,monday) or write all if you want all days: ')
    day = day.lower()
    
    # ask th user to enter a day
    while day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday','all']:
        print(' Please enter the correct day')
        day = input('Please enter a day from a week like(sunday,monday) or write all if you want all days: ')

    print('-'*40)
    return city, month, day

# loading the data
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df
    #The above solution from practice problem 3

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    print('most common month: ',df['month'].value_counts())
    
    # Display the most common day of week
    print('most common day: ',df['day_of_week'].value_counts())

    # Display the most common start hour
    print('most common start hour: ',df['Start Time'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #  Display most commonly used start station
    print('most commonly used start station: ',df['Start Station'].value_counts().index[0])


    #  Display most commonly used end station
    print('most commonly used end station',df['End Station'].value_counts().index[0])


    #  Display most frequent combination of start station and end station trip
    print('most frequent combination of start station and end station trip: ',df.groupby(['Start Station','End Station']).size())
                                                                     


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    print('total travel time: ',df['Trip Duration'].sum())


    # Display mean travel time
    print('mean travel time: ',df['Trip Duration'].mean())



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('counts of user types: ',df['User Type'].count())


    # Display counts of gender
    if city != 'washington':
        print('counts of gender: ',df['Gender'].count())
        

    # Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print('earliest year: ',df['Birth Year'].min()) 
        print('most recent: ',df['Birth Year'].max())
        print('most common year of birth: ',df['Birth Year'].value_counts())
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        count=0
        while True:
            rawData = input('if you want to see the raw data type yes, if not type no')
            if rawData.lower() != 'yes':
                break
            print(df[count:count+5])
            count += 5
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
