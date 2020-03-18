import pandas as pd
import xlsxwriter


#
# MTY Meteorological Data
# Must update concat functions for performance !
# 80 lines that could be 40
#


def foo(energy):

    # Big DF (combined data from every single year)
    years = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012']
    big_df = pd.DataFrame()
    for i in range(len(years)):
        df = pd.read_csv('./src/RSF_Monterrey_{}.csv'.format(years[i]))
        big_df = pd.concat([big_df, df])

    # EOLIC ENERGY
    if energy == 1:
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

                print('{}m, {}h, added'.format(j+1, k))

        final_df.reset_index(drop=True, inplace=True)
        return final_df

    # SOLAR ENERGY
    if energy == 2:
        # Final DataFrame Structure
        main_columns = ['Month', 'Hour', 'Minute',
                        'Clearsky DHI Average', 'Clearsky DNI Average', 'Clearsky GHI Average', ]
        final_df = pd.DataFrame({
            'Month': [],
            'Hour': [],
            'Minute': [],
            'Clearsky DHI Average': [],
            'Clearsky DNI Average': [],
            'Clearsky GHI Average': [],
        })

        # All the data resides in big_df, filter parameters
        useful_df = big_df[['Year', 'Month', 'Day', 'Hour', 'Minute',
                            'Clearsky DHI', 'Clearsky DNI', 'Clearsky GHI', ]]

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
                    'Clearsky DHI Average': [full_hour_df['Clearsky DHI'].mean()],
                    'Clearsky DNI Average': [full_hour_df['Clearsky DNI'].mean()],
                    'Clearsky GHI Average': [full_hour_df['Clearsky GHI'].mean()],
                }
                data_half_h = {
                    'Month': [j+1],
                    'Hour': [k],
                    'Minute': [30],
                    'Clearsky DHI Average': [half_hour_df['Clearsky DHI'].mean()],
                    'Clearsky DNI Average': [half_hour_df['Clearsky DNI'].mean()],
                    'Clearsky GHI Average': [half_hour_df['Clearsky GHI'].mean()],
                }

                new_row = pd.DataFrame(
                    data_full_h, columns=main_columns)
                new_row_ = pd.DataFrame(
                    data_half_h, columns=main_columns)
                both_rows = pd.concat([new_row, new_row_])

                final_df = pd.concat([final_df, both_rows])
                # new_row.reset_index(drop=True, inplace=True)

                print('{}m, {}h, added'.format(j+1, k))

        final_df.reset_index(drop=True, inplace=True)
        return final_df


# Function to prettify output
def pretty(df, name):
    writer = pd.ExcelWriter(
        './final/{}_pretty.xlsx'.format(name), engine='xlsxwriter')
    for i in range(12):
        pretty_df = df[df['Month'] == i+1]
        pretty_df.to_excel(writer, sheet_name='Sheet_{}'.format(i+1))
    writer.save()


if __name__ == '__main__':
    # 1 for eolic, 2 for solar
    final = foo(2)
    # print(final)
    # final.to_csv('./final/final.csv', index=False)
    pretty(final, 'lab_solar')
