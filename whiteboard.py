

numbers = [4,11,20,3,15,20]
more_nums = [4,10,3,5,7]

doubleminus = list(map(lambda x,y: ((x*2)-1,y*2)-1), numbers,more_nums)
print(doubleminus)