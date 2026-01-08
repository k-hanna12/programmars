def solution(nums):
    ani = {}
    for i in nums:
        ani[i] = ani.get(i)
    if (len(ani)<=(len(nums)/2)):
        return len(ani)
    return (len(nums)/2)
