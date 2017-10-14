def reverse_game():
    tc = input()
    list_final = []
    while tc > 0:
        num, ques = map(int, raw_input().strip().split(' '))
        if num % 2 == 0:
            list_final = [x for x in range(1,num,2)] + [x for x in range(num-2,-1,-2)]
        else:
            list_final = [x for x in range(1,num-1,2)] + [x for x in range(num-1,-1,-2)]
        print list_final[ques]
        tc -= 1

def main():
    reverse_game()

if __name__ == "__main__":
    main()