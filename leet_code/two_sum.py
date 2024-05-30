def twosum(nums,target):
    list_num = {} #criando um dicionário

    for i,num in enumerate(nums):
        complement = target - num
        if complement in list_num:
            return [list_num[complement],i]
        list_num[num] = i
    return []