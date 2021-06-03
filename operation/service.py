from collections import Counter

def get_time(time_list):
    occurence_count = Counter(time_list)
    return occurence_count.most_common(1)[0][0]
