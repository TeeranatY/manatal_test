import random

def generate_lottery() :
    out = list()
    # random.seed(11,version=2)
    for i in range(10) :
        out.append(random.randint(1,50))
   
    out.sort()
    print(out)
    # print(random.choices(out,weights=int,k=10))
    return out

def test_lottery(lottery) :
    for i in range(len(lottery)) :
        if i+1 >= len(lottery) : 
            break
        if lottery[i] > lottery[i+1] :
            return False 
    return True

lotto = generate_lottery()
print(test_lottery(lotto))