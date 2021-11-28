import os
import auction_logo
def clear(): os.system('cls')

bidders_list={}
are_other_bidders=True
highest_bid=0
print(auction_logo.logo)
print("Welcom to Silent Bidding System:..........")
while are_other_bidders:
    name=input("Enter the name : ")
    bid=int(input("Enter your bid :"))
    bidders_list[name]=bid
    are_other=input("Are there any other to bid ? Yes or No : ")
    clear()
    if(are_other=='no'):
        are_other_bidders=False


for key in bidders_list:
    if bidders_list[key]>highest_bid:
        highest_bid=bidders_list[key]
        bidders_name=key
    

print(f"The bid is won by : {bidders_name} with the bid of Rs {highest_bid}")



# END OF CODE #

