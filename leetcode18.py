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



class Solution:
    def mediansortedarray(self, num1, num2):
        merged = sorted(num1+num2)
        n = len(merged)
        if n%2 == 0:
            return (merged[n//2 - 1] + merged[n//2])/2
        else:
            return merged[n//2]
s = Solution()
print(s.mediansortedarray([1,2,3],[]))
print(s.mediansortedarray([1,2],[3,4]))
