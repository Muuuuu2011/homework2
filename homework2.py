#要求一
def caculate(min,max):
    sum = 0
    nums= min
    for _ in range(max+1-min):
        sum = nums+sum
        nums+=1
        
    print(sum)
caculate(1,3)
caculate(4,8)


#要求二
def avg(data):
# 請用你的程式補完這個函式的區塊
    employees = data['employees']
    count = data['count']
    sum = 0
    for item in employees:
        a = item["salary"]
        sum = a + sum
    avgSalary = sum/count
    print(avgSalary)
avg({"count":3,"employees":[{"name":"John","salary":30000},{"name":"Bob","salary":60000},{"name":"Jenny","salary":50000}]}) 


#要求三
def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
    bigNum = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            else:
                smallNum =nums[i]*nums[j]
                if smallNum > bigNum:
                    bigNum = smallNum
                elif smallNum < bigNum:
                    continue
    print(bigNum)    
maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值
maxProduct([10, 10, 20, 20])


#要求四
def twoSum(nums, target):
# your code here
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            else:
                if nums[i]+nums[j]==target:
                    result = [i,j]
                    return result
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


#要求五
def maxZeros(nums):
# 請用你的程式補完這個函式的區塊
    sum = 0
    bigSum = 0
    for i in nums:
        if i == 0:
            sum = sum + 1
            if sum > bigSum :
                bigSum = sum 
        else :
            sum = 0
    print(bigSum)
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0