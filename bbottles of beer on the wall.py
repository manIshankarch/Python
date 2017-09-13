# for loop

for quant in range(1,100,+1):
    if quant <100 :
        print(quant," bottle of beer on the wall","put one botttle of beer and make it",quant+1)
        if quant <99:
            suffix= str(quant)+ " bottles of beer on the wall"
        else:
            suffix = 'bottles of beer on the wall'

    elif quant ==100 :
        print("100 bottles of berr on the wall,100 bottle of the beer")
        suffix=" all bottles of beer on the wall"

    print(" take one bottle and put it on the wall ", suffix)
    print("----")



    # BREAK
    count=0
    while True:
        print(count)
        count+=1
        if (count > 10):
            break


    # continue


for x in range(20):
    if (x%2)==0:
        continue
        print(x)