
# roman = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}

NUMERIC = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
ROMAN = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
def convert(numb) :
    out = ""
    i = 0
    while numb >0 :
        if numb<NUMERIC[i] : 
            i+=1
        else :
            out += ROMAN[i]
            numb -= NUMERIC[i]
    print(out)
    return out 
def test() :
    while True :
        inp = int(input("Enter : ").strip())
        convert(inp)
        
if __name__ == "__main__":
    test()