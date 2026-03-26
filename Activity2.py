Amount = int(input("Please Enter Amount for Withdraw :"))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print( "The number of 100 dollar notes", note_1)
print( "The number of 50 dollar notes", note_2)
print( "The number of 10 dollar notes", note_3)