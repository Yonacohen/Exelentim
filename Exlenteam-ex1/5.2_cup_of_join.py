import random
list = ["Club","Diamond","Heart","Spade"]
def print_card_arr(arr):
    for k in arr:
        if type(k) is card:
            k.print_card()


class card:
    def __init__(self,num, shape):             #const
        if (num>0 & num <14):                 #check if num invalid
            self.num = num
            if (shape in list):                #chech if shape invalid
                 self.shape = shape
    def print_card(self):
        print('num:' , self.num , 'shape:',  self.shape)



packet = []        #create a packet
for i in range(1,14):
    for j in list:
        packet.append(card(i,j))

random.shuffle(packet)      #shuffle packet

    #devide a packet
player1  = packet[0:12]
player2  = packet[13:26]
player3  = packet[27:39]
player4  = packet[40:52]

def sum_of_card (arr): #func of sum
    sum = 0
    for k in arr:
        if type(k) is card:
            sum = sum + k.num
    return sum
        #check who the biggest sum
sum_arr = [sum_of_card (player1) ,sum_of_card (player2) ,sum_of_card (player3) ,sum_of_card (player4) ]
print(sum_arr)
the_big_sum = max(sum_of_card (player1) ,sum_of_card (player2) ,sum_of_card (player3) ,sum_of_card (player4) )
print (the_big_sum)








