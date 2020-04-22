from lib.get.TimeStamps.FirstTimeStamps import getFirstTimeStamps
from lib.get.TimeStamps.LastTimeStamps import getLastTimeStamps

def getSnapshotFromTime(snapshot_time:str, all_timestamps:list, date:str):
    if snapshot_time == 'last-snapshot':
        last_timestamp_objects = getLastTimeStamps(all_timestamps)
        for i in last_timestamp_objects:
            if i.timestamp.strftime('%d-%m-%Y') == date:
                raw_url = i.raw_url
                view_url = i.view_url
    elif snapshot_time == 'first-snapshot':
        first_timestamp_objects = getFirstTimeStamps(all_timestamps)
        for i in first_timestamp_objects:
            if i.timestamp.strftime('%d-%m-%Y') == date:
                raw_url = i.raw_url
                view_url = i.view_url
    return raw_url, view_url