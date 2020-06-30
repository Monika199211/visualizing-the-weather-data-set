# --------------
# Import the required Libraries
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import calendar
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

weather_df=pd.read_csv(path,parse_dates=True,index_col="Date/Time")
categorical=weather_df.select_dtypes(include='object')
numerical=weather_df.select_dtypes(exclude='object')
# Generate a line chart that visualizes the readings in the months


def line_chart(df,period,col):
    """ A line chart that visualizes the readings in the months
    
    This function accepts the dataframe df ,period(day/month/year) and col(feature), which plots the aggregated value of the feature based on the periods. Ensure the period labels are properly named.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    period - Period of time over which you want to aggregate the data
    col - Feature of the dataframe
    
    """
    if period == "Month":
        data = df.groupby(df.index.month).mean()
    elif period == "Day":
        data = df.groupby(df.index.day).mean()
    elif period == "Year":
        data = df.groupby(df.index.year).mean()
    months = calendar.month_name[1:]
    x = months
    y  = data[col]
    plt.plot(x,y)
    plt.ylabel("Temp (C)")
    plt.xlabel("Month")
    plt.title("Temperature Trend, 2012")
    
line_chart(weather_df,'Month','Temp (C)')  


# Function to perform univariate analysis of categorical columns
def plot_categorical_columns(df):
    """ Univariate analysis of categorical columns
    
    This function accepts the dataframe df which analyzes all the variable in the data and performs the univariate analysis using bar plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    
    """
    plt.figure(figsize=(10,20))
    df["Weather"].value_counts(normalize=True).plot(kind='bar')
    
    
    
plot_categorical_columns(categorical)  

# Function to plot continous plots
import seaborn as sns
def plot_cont(df,plt_typ):
    """ Univariate analysis of Numerical columns
    
    This function accepts the dataframe df, plt_type(boxplot/distplot) which analyzes all the variable in the data and performs the univariate analysis using boxplot or distplot plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    plt_type - type of plot through which you want to visualize the data
    
    """

    sns.distplot(df[plt_typ])
    plt.show()
plot_cont(numerical,'Temp (C)') 
plot_cont(numerical,'Dew Point Temp (C)') 
plot_cont(numerical,'Rel Hum (%)') 
plot_cont(numerical,'Wind Spd (km/h)') 
plot_cont(numerical,'Visibility (km)') 
plot_cont(numerical,'Stn Press (kPa)') 
   

# Function to plot grouped values based on the feature
def group_values(df,col1,agg1,col2):
    """ Agrregate values by grouping
    
    This function accepts a dataframe, 2 column(feature) and aggregated function(agg1) which groupby the dataframe based on the column and plots the bar plot.
   
    Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - Feature of the dataframe on which values will be aggregated.
    agg1 - Dictionary of aggregate functions with feature as the key and func as the value
    col2 - Feature of the dataframe to be plot against grouped data.
    
    Returns:
    grouping - Dataframe with all columns on which it is grouped on.
    """
    aggregate = {'mean':np.mean,'max':np.max,'min':np.min}
    plt.figure(figsize=(10,10))
    b=df.groupby(col1).agg(aggregate[agg1])
    b[col2].plot(kind='bar')
group_values(weather_df,"Weather",'mean',"Visibility (km)")

# Read the Data and pass the parameter as parse_dates=True, index_col='Date/Time'



# Lets try to generate a line chart that visualizes the temperature readings in the months.
# Call the function line_chart() with the appropriate parameters.



# Now let's perform the univariate analysis of categorical features.
# Call the "function plot_categorical_columns()" with appropriate parameters.



# Let's plot the Univariate analysis of Numerical columns.
# Call the function "plot_cont()" with the appropriate parameters to plot distplot



# Call the function "plot_cont()" with the appropriate parameters to plot boxplot


# Groupby the data by Weather and plot the graph of the mean visibility during different weathers. Call the function group_values to plot the graph.
# Feel free to try on diffrent features and aggregated functions like max, min.




