def twoSum(nums, target):
        hashMap = {} # target-nums[index], index
        diff = 0
        index = 0
        
        for nr in nums:
            diff = target - nr
            if (diff > 0):
                print(hashMap)
                print(diff)
                if nr in hashMap:
                    print([hashMap[nr],index])
                    return [hashMap[nr],index]
                else:
                    print(f"{diff} se adauga in hashMap")
                    hashMap[diff] = index
            index += 1
        return []

print(twoSum([3,3], 6))