import time 
import pandas as pd 
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    months=["january","february","march","april","may","june","all"]
    days=["sat","sun","mon","tues","wed","thru","fri","all"]  
    city=input("To view the avaliable bikeshare data, type:\n chicago\n or new york city\n or washington\n ").lower()
   
    while city not in CITY_DATA.keys():
        print("That\'s invalid input")
        city=input("To view the avaliable bikeshare data, type:\n chicago\n or new york city\n or washington\n\n ").lower()
    month=input("\n\nTo filter data by a particular month, please type the month or all for not filtering by month:\n-January\n-February\n-March\n-April\n-May\n-June\n-all\n\n ").lower()
    while month not in months:
        print("That's invalid input")
        month=input("\n\nTo filter data by a particular month, please type the month or all for not filtering by month:\n-January\n-February\n-March\n-April\n-May\n-June\n-all\n\n ").lower()
    
    day=input("\n\n to filter data by day,type the day name such(Sat,Sun,Mon,Tues,Wed,Thur,Fri) or all\n").lower()
    while day not in days:
        print("That's invalid input")
        day=input("\n\n to filter data by day,type the day name such(Sat,Sun,Mon,Tues,Wed,Thur,Fri) or all\n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city,month,day

def load_data(city, month, day):
    df=pd.read_csv(CITY_DATA[city])
    df["Start Time"]=pd.to_datetime(df["Start Time"])
    df["month"]=df["Start Time"].dt.month_name()
    df["day_of_week"]=df["Start Time"].dt.day_name()
    
    if month!="all":
        months=["janurary","february","march","april","may","june"]
        df=df[df["month"]==month.title()]
    if day !="all":
        df=df[df["day_of_week"].str.startswith(day.title())]

    return df

def time_stats(df):
  

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    com_month=df["month"].mode()[0]
    print("most common month is {}".format(com_month))
    com_day=df["day_of_week"].mode()[0]
    print("most common day is {}".format(com_day))
    df["start_hour"]=df["Start Time"].dt.hour
    com_hour= df["start_hour"].mode()[0]
    print("most start hour is {}".format(com_hour))
   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    com_stastation=df["Start Station"].mode()[0]
    print("Most common start station is {}".format(com_stastation))

    # TO DO: display most commonly used end station
    com_endstation=df["End Station"].mode()[0]
    print("Most common end station is {}".format(com_endstation))

    # TO DO: display most frequent combination of start station and end station trip
    df["combination_station"]=df["Start Station"]+" # "+df["End Station"]
    com_combine=df["combination_station"].mode()[0]
    print("Most frequent combination of start station and end station is {}".format(com_combine))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    toal_trav=df["Trip Duration"].sum()
    print("Total travel time is {} seconds".format(toal_trav))

    # TO DO: display mean travel time
    avg_travel=df["Trip Duration"].mean()
    print("Average travel time is {}".format(avg_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count =df["User Type"].value_counts()
    print("Counts of user type is:\n {}".format(user_count))

    # TO DO: Display counts of gender
    if "Gender" in df:
        gender_count=df["Gender"].value_counts()
        print("Counts of gender is:\n {}".format(gender_count))

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        
        ear_birth=df["Birth Year"].min()
        print("Earliset birth year is {}".format(ear_birth))
        rec_birth=df["Birth Year"].max()
        print("Recent birth year is {}".format(rec_birth))
        com_birth=df["Birth Year"].mode()[0]
        print("Most common year of birth is {}".format(com_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city,month,day = get_filters()
        print(city,month,day)
        df = load_data(city, month, day)
        print(df.head())
      
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        while True:
            viewdata=input("Would you like to see the raw data? Type 'Yes' or 'No'.").lower()
            if viewdata=="yes":
                row=0
                print(df[row:row+5])
                row+=5
                break
            else:
                break
            

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            
            break


if __name__ == "__main__":
	main()
