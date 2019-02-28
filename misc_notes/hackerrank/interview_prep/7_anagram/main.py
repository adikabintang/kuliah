# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a_list = list(a)
    b_list = list(b)

    i = 0
    while i < len(a_list):   
        if a_list[i] in b_list:
            b_list.remove(a_list[i])
            del a_list[i]
        else:
            i = i+1
    
    return (len(a_list) + len(b_list))

def main():
    a = "abc"
    b = "cdf"
    print(makeAnagram(a, b))

if __name__ == "__main__":
    main()