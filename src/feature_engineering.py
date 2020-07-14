import numpy as np
import pandas as pd

def temporal_features(df):
    # duration in minutes
    df['duration_min']  = df['duration_sec'] / 60

    # order of days for use in categorical plot.
    # chosen to keep saturday and sunday next to eachother to have weekend stand out
    day_order = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

    # temporal features
    df['week'] = pd.to_datetime(df['start_time']).dt.week
    df['day'] = pd.to_datetime(df['start_time']).dt.day
    df['dow'] = pd.Categorical(pd.to_datetime(df['start_time']).dt.day_name().str.lower(), ordered = True, categories = day_order)
    df['hour'] = pd.to_datetime(df['start_time']).dt.hour
    df['end_hour'] = pd.to_datetime(df['end_time']).dt.hour

    # parameter for weekend
    weekend_days = ['saturday', 'sunday']
    df['day_type'] = df['dow'].isin(weekend_days).replace({True : 'weekend', False : 'weekday'})

    return df
