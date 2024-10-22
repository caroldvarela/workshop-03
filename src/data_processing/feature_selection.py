import pandas as pd
import os
from sklearn.model_selection import train_test_split

def prepare_data():
    """
    Prepares the happiness data for modeling.

    Returns:
        pd.DataFrame: The test features DataFrame (X_test).
    """

    # Define the directory containing the CSV files
    data_dir = "../data/"

    # Define the file names for each year
    file_names = [
        "2015.csv",
        "2016.csv",
        "2017.csv",
        "2018.csv",
        "2019.csv"
    ]

    # Load the datasets for each year
    dfs = [pd.read_csv(os.path.join(data_dir, file_name)) for file_name in file_names]

    # Remove records with NaN values in the 2018 dataset
    nan_record_index = dfs[3][dfs[3].isna().any(axis=1)].index
    dfs[3].drop(nan_record_index, inplace=True)

    # Rename columns for consistency and add 'Year' column
    for i, df in enumerate(dfs):
        if i == 0:  # 2015
            df.rename(columns={
                'Happiness Rank': 'Happiness_Rank',
                'Happiness Score': 'Score',
                'Economy (GDP per Capita)': 'Economy',
                'Family': 'Social_support',
                'Health (Life Expectancy)': 'Healthy_life_expectancy',
                'Freedom': 'Freedom_to_make_life_choices',
                'Trust (Government Corruption)': 'Perceptions_of_corruption',
                'Generosity': 'Generosity',
                'Dystopia Residual': 'Dystopia_Residual' 
            }, inplace=True)
            df['Year'] = 2015
        elif i == 1:  # 2016
            df.rename(columns={
                'Happiness Rank': 'Happiness_Rank',
                'Happiness Score': 'Score',
                'Lower Confidence Interval': 'Lower_Confidence_Interval',
                'Upper Confidence Interval': 'Upper_Confidence_Interval',
                'Economy (GDP per Capita)': 'Economy',
                'Family': 'Social_support',
                'Health (Life Expectancy)': 'Healthy_life_expectancy',
                'Freedom': 'Freedom_to_make_life_choices',
                'Trust (Government Corruption)': 'Perceptions_of_corruption',
                'Generosity': 'Generosity',
                'Dystopia Residual': 'Dystopia_Residual'
            }, inplace=True)
            df['Year'] = 2016
        elif i == 2:  # 2017
            df.rename(columns={
                'Happiness.Rank': 'Happiness_Rank',
                'Happiness.Score': 'Score',
                'Whisker.high': 'Whisker_high',
                'Whisker.low': 'Whisker_low',
                'Economy..GDP.per.Capita.': 'Economy',
                'Family': 'Social_support',
                'Health..Life.Expectancy.': 'Healthy_life_expectancy',
                'Freedom': 'Freedom_to_make_life_choices',
                'Generosity': 'Generosity',
                'Trust..Government.Corruption.': 'Perceptions_of_corruption',
                'Dystopia.Residual': 'Dystopia_Residual'
            }, inplace=True)
            df['Year'] = 2017
        elif i == 3:  # 2018
            df.rename(columns={
                'Overall rank': 'Happiness_Rank',
                'Country or region': 'Country',
                'Score': 'Score',
                'GDP per capita': 'Economy',
                'Social support': 'Social_support',
                'Healthy life expectancy': 'Healthy_life_expectancy',
                'Freedom to make life choices': 'Freedom_to_make_life_choices',
                'Generosity': 'Generosity',
                'Perceptions of corruption': 'Perceptions_of_corruption'
            }, inplace=True)
            df['Year'] = 2018
        elif i == 4:  # 2019
            df.rename(columns={
                'Overall rank': 'Happiness_Rank',
                'Country or region': 'Country',
                'Score': 'Score',
                'GDP per capita': 'Economy',
                'Social support': 'Social_support',
                'Healthy life expectancy': 'Healthy_life_expectancy',
                'Freedom to make life choices': 'Freedom_to_make_life_choices',
                'Generosity': 'Generosity',
                'Perceptions of corruption': 'Perceptions_of_corruption'
            }, inplace=True)
            df['Year'] = 2019

    # Create a dictionary for regions based on the 2016 dataset
    region_dict_2016 = dfs[1][['Country', 'Region']].drop_duplicates().set_index('Country').to_dict()['Region']

    # Initialize 'Region' column as NA for later filling in 2017, 2018, and 2019 datasets
    for i in range(2, 5):
        dfs[i]['Region'] = pd.NA
        dfs[i]['Region'] = dfs[i]['Region'].fillna(dfs[i]['Country'].map(region_dict_2016))

    # Combine all yearly datasets into a single DataFrame
    df = pd.concat(dfs, ignore_index=True)

    # Specify the common columns to keep across all datasets
    common_columns = ['Score', 'Happiness_Rank', 'Healthy_life_expectancy', 'Social_support', 
                      'Country', 'Economy', 'Generosity', 'Year', 
                      'Freedom_to_make_life_choices', 'Region', 'Perceptions_of_corruption']

    # Filter each dataset to retain only common columns
    for i in range(len(dfs)):
        dfs[i] = dfs[i][common_columns]

    # Combine the filtered datasets again
    df = pd.concat(dfs, ignore_index=True)

    # Mapping for regions not found in the 2016 dataset
    region_mapping = {
        'Taiwan Province of China': 'Eastern Asia',
        'Hong Kong S.A.R., China': 'Eastern Asia',
        'Mozambique': 'Sub-Saharan Africa',
        'Lesotho': 'Sub-Saharan Africa',
        'Central African Republic': 'Sub-Saharan Africa',
        'Trinidad & Tobago': 'Latin America and Caribbean',
        'Northern Cyprus': 'Western Europe',
        'North Macedonia': 'Central and Eastern Europe',
        'Gambia': 'Sub-Saharan Africa',
        'Swaziland': 'Sub-Saharan Africa'
    }

    # Fill remaining 'Region' values using the additional mapping
    df['Region'] = df['Region'].fillna(df['Country'].map(region_mapping))

    # Ensure the 'Score' column is the last column in the DataFrame
    score = df.pop('Score')
    df['Score'] = score

    # Drop the 'Happiness_Rank' column as it's not needed for modeling
    df.drop('Happiness_Rank', axis=1, inplace=True) 

    # One-hot encode the 'Region' categorical variable
    df = pd.get_dummies(df, columns=['Region'], drop_first=True)

    # Drop the 'Country' column as it's not needed for modeling
    df.drop(columns=['Country'], axis=1, inplace=True)

    # Define features (X) and target variable (y)
    X = df.drop(columns=['Score'])  # Features
    y = df['Score']  # Target variable

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Return the test features
    return X_test

