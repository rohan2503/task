def minCostDif(gifts, M):
    gifts.sort()
    start = 0
    end = M-1
    minDif = float('inf')
    l,r = 0,0
    N = len(gifts)
    while end < N:
        if gifts[end][0] - gifts[start][0] < minDif:
            minDif = gifts[end][0] - gifts[start][0]
            l,r = start, end
        start +=1
        end +=1
    return (minDif, l)

if __name__=="__main__":
    fd = open("sample_input.txt", "r")
    lines = fd.readlines()

    emp = 1
    n = -3
    goodies = []

    for each_line in lines:
        if(emp):
            m = int(each_line.split(":")[1])
            emp = 0
        if(n>0):
            val = each_line.split(":")
            goodies.append([int(val[1]), val[0]])
        n+=1
    # print(goodies)
    ans, ind = minCostDif(goodies, m)

    output = ["The goodies selected for distribution are:\n", "\n"]

    for i in range(ind, ind+m):
        val = goodies[i][1] + ": " + str(goodies[i][0]) + "\n"
        output.append(val)

    diff = "\n" + "And the difference between the chosen goodie with highest price and the lowest price is " + str(ans)
    output.append(diff)
    opFile = open("sample_output.txt", "w")
    opFile.writelines(output)
    opFile.close()


