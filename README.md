# Meteorogical Data lookup for Monterrey, NL

Data analysis for metorogical sets
Current sets: MTY, NL

## Requirements

### pandas

`pip install pandas`

### numpy

`pip install numpy`

### xlsxwriter

`pip install xlsxwriter`

## Structure

### Current dataframe support

For Eolic Energy

```
  final_df = pd.DataFrame({
    'Year': [],
    'Month': [],
    'Hour': [],
    'Minute': [],
    'Wind Speed Average': [],
    'Wind Direction Average': [],
    'Temperature Average': [],
    'Pressure Average': [],
    'Humidity Average': [],
    'Density Average': [],
  })
```

For Solar Energy

```
   final_df = pd.DataFrame({
      'Month': [],
      'Hour': [],
      'Minute': [],
      'Clearsky GHI Average': [],
      'Clearsky DNI + DHI Average': [],
      'Clearsky DNI Average': [],
      'Clearsky DHI Average': [],
      'Solar Height Angle': [],
      'Azimut Angle': [],
  })
```
