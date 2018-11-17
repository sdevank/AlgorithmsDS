import traceback
import math

def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    left = [0]*(n1)
    right = [0]*(n2)
    for i in range(0,n1):
        left[i] = A[p+i]
    for j in range(0,n2):
        right[j] = A[q+1+j]
    i=0
    j=0
    k=p
    for k in range(p,r+1):
        if i<n1 and j<n2:
            if len(left[i].sender) >= len(right[j].sender):
                A[k] = left[i]
                i=i+1
            else:
                A[k] = right[j]
                j=j+1
        else:
            break

    while(i<n1):
        A[k] = left[i]
        i = i+1
        k = k+1
    while(j<n2):
        A[k] = right[j]
        j = j+1
        k = k+1

def merge_sort(A,p,r):
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)



def partition(A,p,r):
    x = A[r].sender
    i = p-1
    for j in range(p,r):
        if len(A[j].sender) > len(x):
             i = i+1
             temp1 = A[i]
             A[i] = A[j]
             A[j] = temp1
    temp2 = A[i+1]
    A[i+1] = A[r]
    A[r] = temp2
    return i+1


def quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

#DO NOT CHANGE ANYTHING BELOW THIS LINE

#Takes in list of Emails A, and begins the recursive merge_sort
#process by calling merge_sort on the entire list
#Returns nothing
def merge_sort_wrapper(A):
    merge_sort(A,0,len(A)-1)


#Takes in list of Emails A, and begins the recursive quicksort
#process by calling quicksort on the entire list
#Returns nothing
def quicksort_wrapper(A):
    quicksort(A,0,len(A)-1)

#Email class
#Each email has two instance variables:
#   self.sender is a string representing the name of the person
#     or organization that sent the email
#   self.subject is a stirng representing the subject line of
#     the Email
class Email:
    def __init__(self,sender,subject):
        self.sender = sender
        self.subject = subject
    def __repr__(self):
        return "\n"+self.sender + ": " + self.subject


#Setup test cases
e1 = Email("Inigo Montoya","You killed my father. Prepare to die.")
e2 = Email("IRS", "THIS IS YOUR FINAL WARNING")
e3 = Email("Your Grandson", "Need Money for College")
e4 = Email("Prince of Nigeria", "Help transferring funds")
e5 = Email("Jackpot Lottery", "YOU'RE WINNER!")
e6 = Email("Super Antivirus Pro", "Virus Detected! Download Now!")
e7 = Email("Anonymous", "Forward this to 20 friends and you will get $$$")
e8 = Email("The Bank", "Please confirm your password")

e9 = Email("Ted", "HAHAHAHAHAHAHAHAHAHA")
e10 = Email("Tedd","mine!")
e11 = Email("Teddd","be")
e12 = Email("Tedddd","will")
e13 = Email("Teddddd","Vengeance")
e14 = Email("Tedddddd","day.")
e15 = Email("Teddddddd","this")
e16 = Email("Tedddddddd","for")
e17 = Email("Teddddddddd","waited")
e18 = Email("Tedddddddddd","I")
e19 = Email("Teddddddddddd","have")
e20 = Email("Tedddddddddddd","Long")



inbox1 = []
inbox2 = [e13]
inbox3 = [e2,e6]
inbox4 = [e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20]
inbox5 = [e20,e19,e18,e17,e16,e15,e14,e13,e12,e11,e10,e9]
inbox6 = [e1,e2,e3,e4,e5,e6,e7,e8]

#Quicksort's 6th test is slightly different: QSort isn't stable,
#so we don't bother checking for the case where you have two messages
#of equal length.
inbox1q = []
inbox2q = [e13]
inbox3q = [e2,e6]
inbox4q = [e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20]
inbox5q = [e20,e19,e18,e17,e16,e15,e14,e13,e12,e11,e10,e9]
inbox6q = [e1,e2,e4,e5,e6,e7,e8]


tests = [inbox1,inbox2,inbox3,inbox4,inbox5,inbox6]
testsq = [inbox1q,inbox2q,inbox3q,inbox4q,inbox5q,inbox6q]
correct = [[],
           [e13],
           [e6,e2],
           [e20,e19,e18,e17,e16,e15,e14,e13,e12,e11,e10,e9],
           [e20,e19,e18,e17,e16,e15,e14,e13,e12,e11,e10,e9],
           [e6,e4,e5,e1,e3,e7,e8,e2]]

correctq = [[],
           [e13],
           [e6,e2],
           [e20,e19,e18,e17,e16,e15,e14,e13,e12,e11,e10,e9],
           [e20,e19,e18,e17,e16,e15,e14,e13,e12,e11,e10,e9],
            [e6,e4,e5,e1,e7,e8,e2]]

#Run test cases, check whether sorted list correct
count = 0

for i in range(len(tests)):
    print("TEST #"+str(i+1))
    try:
        print("Running: merge_sort_wrapper(",tests[i],")\n")
        merge_sort_wrapper(tests[i])
        print("Expected:",correct[i],"\n\nGot:",tests[i])
        if (correct[i] == tests[i]):
            count=count+1
        else:
            print("\nFAIL: Incorrect output")
    except Exception:
        print("\nFAIL: Error ", traceback.format_exc())
    print()
    try:
        print("Running: quicksort_wrapper(",testsq[i],")\n")
        quicksort_wrapper(testsq[i])
        print("Expected:",correctq[i],"\n\nGot:",testsq[i])
        if (correctq[i] == testsq[i]):
            count=count+1
        else:
            print("\nFAIL: Incorrect output")
    except Exception:
        print("\nFAIL: Error ", traceback.format_exc())
    print()
    print()


print(count,"out of",len(tests+testsq),"tests passed.")
