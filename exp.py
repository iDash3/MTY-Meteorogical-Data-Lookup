import pandas as pd

#
# MTY Meteorological Data
# Must update concat functions for performance !
# 80 lines that could be 40
#


def foo():
    # Final DataFrame Structure
    main_columns = ['Month', 'Hour', 'Minute', 'Wind Speed Average', 'Wind Direction Average',
                    'Temperature Average', 'Pressure Average', 'Humidity Average']
    final_df = pd.DataFrame({
        'Month': [],
        'Hour': [],
        'Minute': [],
        'Wind Speed Average': [],
        'Wind Direction Average': [],
        'Temperature Average': [],
        'Pressure Average': [],
        'Humidity Average': [],
    })

    years = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012']
    big_df = pd.DataFrame()
    for i in range(len(years)):
        df = pd.read_csv('./src/RSF_Monterrey_{}.csv'.format(years[i]))
        big_df = pd.concat([big_df, df])

    # All the data resides in big_df, filter parameters
    useful_df = big_df[['Year', 'Month', 'Day', 'Hour', 'Minute', 'Temperature', 'Pressure',
                        'Relative Humidity', 'Precipitable Water', 'Wind Direction', 'Wind Speed']]

    # Iterate over useful data
    for j in range(12):
        # From months 1-12 months
        month_zero = useful_df[useful_df['Month'] == j+1]
        for k in range(24):
            # For every hour 0-23
            hour_zero = month_zero[month_zero['Hour'] == k]
            # Every half hour 0 or 30
            full_hour_df = hour_zero[hour_zero['Minute'] == 0]
            half_hour_df = hour_zero[hour_zero['Minute'] == 30]

            data_full_h = {
                'Month': [j+1],
                'Hour': [k],
                'Minute': [0],
                'Wind Speed Average': [full_hour_df['Wind Speed'].mean()],
                'Wind Direction Average': [full_hour_df['Wind Direction'].mean()],
                'Temperature Average': [full_hour_df['Temperature'].mean()],
                'Pressure Average': [full_hour_df['Pressure'].mean()],
                'Humidity Average': [full_hour_df['Relative Humidity'].mean()],
            }
            data_half_h = {
                'Month': [j+1],
                'Hour': [k],
                'Minute': [30],
                'Wind Speed Average': [half_hour_df['Wind Speed'].mean()],
                'Wind Direction Average': [half_hour_df['Wind Direction'].mean()],
                'Temperature Average': [half_hour_df['Temperature'].mean()],
                'Pressure Average': [half_hour_df['Pressure'].mean()],
                'Humidity Average': [half_hour_df['Relative Humidity'].mean()],
            }

            new_row = pd.DataFrame(
                data_full_h, columns=main_columns)
            new_row_ = pd.DataFrame(
                data_half_h, columns=main_columns)
            both_rows = pd.concat([new_row, new_row_])

            final_df = pd.concat([final_df, both_rows])

    final_df.reset_index(drop=True, inplace=True)
    return final_df


if __name__ == '__main__':
    final = foo()
    final.to_csv('final.csv', index=False)
