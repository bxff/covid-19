def getFirstTimeStamps(timestamps:list):
    last_timestamp_objects = []

    timestamps.sort()
    last_timestamp_objects.append(timestamps[0])
    for i in range(0, len(timestamps)-1):
        today = timestamps[i].timestamp.strftime('%d-%m-%Y')
        tomorrow = timestamps[i+1].timestamp.strftime('%d-%m-%Y')
        if today == tomorrow:
            pass
        else:
            last_timestamp_objects.append(timestamps[i+1])
    return last_timestamp_objects 
