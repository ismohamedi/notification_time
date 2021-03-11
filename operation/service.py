from collections import Counter

def get_time(time_list):
    occurence_count = Counter(time_list)
    return occurence_count.most_common(1)[0][0]

get_time([34,45,45,2,3,4,4,4,4,5,5,7,8])