import pandas as pd


def foo():
    years = ('2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012')
    res_df = pd.DataFrame()

    for year in years:
        pass
        # df = pd.read_csv('./src/RSF_Monterrey_{}.csv'.format(year))

    df = pd.read_csv('./src/RSF_Monterrey_2005.csv')
    useful_df = df[['Year', 'Month', 'Day', 'Hour', 'Minute',
                    'Temperature', 'Pressure',
                    'Relative Humidity', 'Precipitable Water',
                    'Wind Direction', 'Wind Speed']]

    # first_half = useful_df[useful_df['Month'] == 6]

    # From months 1-12
    month_zero = useful_df[useful_df['Month'] == 1]
    # Every half hour
    hour_zero = month_zero[month_zero['Hour'] == 0]
    minute_zero = hour_zero[hour_zero['Minute'] == 0]

    data = [
        'zero_wind_speed', minute_zero['Wind Speed'].mean(),
        'zero_wind_direction', minute_zero['Wind Direction'].mean(),
        'zero_temperature', minute_zero['Temperature'].mean(),
        'zero_pressure', minute_zero['Pressure'].mean(),
    ]

    res_df = pd.concat([res_df, minute_zero])

    print('For month 1, hour 0')
    print(data)
    print(res_df)


if __name__ == '__main__':
    foo()
