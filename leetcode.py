if __name__ == '__main__':
        n = int(input().strip())
        if n % 2 != 0:
            print("weird")
        elif n in range(2, 5):
            print("not weird")
        elif n in range(6, 20):
            print("weird")
        else:
            print("not weird")


def mediansortedarray(self, num1, num2):
    merged = sorted(num1+num2)
    sorted = len(merged)
    if n%2 == 0:
        return (merged[n//2 - 1] + merged[n//2])/2
    else:
        return merged[n//2]

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = curr = ListNode()
        carry = 0
        while l1 or l2 or carry:
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            curr.next = ListNode(carry % 10)
            carry //= 10
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next




class Solution:

    def twoSum(self, nums: List[int], target: int) ->List[int]:
         for i in range(len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

nums = [2,7,11,15]
target = [9]
result =Solution().twoSum(nums,target)
print(result)