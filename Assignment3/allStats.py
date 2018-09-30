

def mostDeath(data, year, cause):
    state = ""
    max = 0
    for d in data:
        if d[0] == year and d[1] == cause:
            if d[3] > max:
                max = d[3]
                state = d[2]
    return print(str(year)+' '+str(state)+' had most deaths caused by '+str(cause)+' with '+str(max)+' deaths')
