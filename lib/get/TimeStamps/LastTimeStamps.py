def getLastTimeStamps(timestamps:list):
    last_timestamp_objects = []

    timestamps.sort()
    for i in range(1, len(timestamps)):
        today = timestamps[i].timestamp.strftime('%d-%m-%Y')
        yesterday = timestamps[i-1].timestamp.strftime('%d-%m-%Y')
        if today == yesterday:
            pass
        else:
            last_timestamp_objects.append(timestamps[i-1])
    timestamps.reverse()
    last_timestamp_objects.append(timestamps[0])
    return last_timestamp_objects
