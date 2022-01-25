def luhn(n):
    temp_list=list(str(n))
    my_list=[]
    list1 = temp_list[-2::-2]
    list2=temp_list[::-2]
    list2 = [int (n) for n in list2]
    my_list=[int(n) for n in list1]
    list1 = [int(n)*2 for n in list1]
    t_list=list1
    for el in list1:
        sum_res=0
        if el>9:
            idx = list1.index(el)
            t_list.pop(idx)
            while el:
                rem = el%10
                sum_res+=rem
                el = el//10 
            t_list.insert(idx, sum_res)
    list1_sum=sum(t_list)
    list2_sum = sum(list2)
    final_sum = list1_sum+ list2_sum
    if final_sum%10==0:
        return True
    return False