import numpy as np
import pandas as pd

def durationStatsByGroup(duration_subset, group, cnt_group = 'user_type'):
    """Get median duration stats over a group and compare this to the overall median"""
    # get some stats for comparison
    r1 = duration_subset.groupby(group).agg({cnt_group : 'count',
                                           'duration_min' : 'median',
                                           'duration_sec' : 'median'})
    r1.columns = ['trips', 'median duration (min)', 'median duration (sec)']

    # add overall duration for comparison
    r1['overall_duration (sec)'] = duration_subset['duration_sec'].median()
    r1['diff (sec)'] = r1['median duration (sec)'] - r1['overall_duration (sec)']
    r1['trips_perc'] = r1['trips']/len(duration_subset)

    return r1[['trips', 'trips_perc', 'median duration (min)',
          	   'median duration (sec)',	'overall_duration (sec)', 'diff (sec)']]


def weekGrowthBreakdown(weekly_growth_subset, grouper, options):
    """
    Calculate week-on-week growth by 'grouper'

    Parameters:
    grouper: the parameter to group by
    options: the values (categories) the grouper parameter can take

    Returns:
    grouped_set: growth per week over grouper
    grouped_total: trip-count per grouper
    """
    # breakdown of growth per grouper
    agg = []
    for val in options:
            tmp = weekly_growth_subset.groupby(['week',grouper]).size().to_frame('cnt').reset_index()
            tmp = tmp[tmp[grouper]==val].reset_index(drop=True) # needed - categorical when grouped get 0
            tmp['growth'] = (tmp['cnt']*100/tmp['cnt'].shift())-100
            agg.append(tmp)

    grouped_set = pd.concat(agg).sort_values('week').reset_index(drop=True)

    # total
    grouped_total = weekly_growth_subset[grouper].value_counts().to_frame('cnt').reset_index()

    return grouped_set, grouped_total
