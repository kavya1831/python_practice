def prime(num):

    '''

    :param num: number to check if prime
    :return:nothing
    '''
    for i in range(2,num):
        if (num % i == 0):
            print "NOT PRIME"
            break
        else:
            print "IS PRIME"
            break

if __name__ == '__main__':

    n = int(input("enter a number"))
    prime(n)