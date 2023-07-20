# print multiples of 3 from -300 to 0. Skip -3 and -8.
"""
for x in range(-300, 0, 3):
    if x == -3:
        break
    if x == -8:
        break
    print(x)
"""

# print integers from 2000 to 5280, using a WHILE
"""
x = 2000

while x <= 5280:
    print(x)
    x = x + 1
"""

# print integers 1 to 100. If divisible by 5, print"Coding" instead. If by 10, also print"Dojo".

"""
for x in range(1, 101):
    if (x % 5 == 0):
        print("Coding")
    if (x % 10 == 0):
        print("Dojo")
"""

# given lowNum, highNum, mult, print multiples of mult from highNum down to lowNum,
# using a FOR. For (2,9,3), print 9 6 3 on (sucessive lines).

"""
function flexCount:(lowNum, highNum, mult) {
    for(var i = highNum; i >= lowNum; i--) {
        if(i % mult === 0){
            console.log(i);

flexCount(2, 9, 3); 
"""
