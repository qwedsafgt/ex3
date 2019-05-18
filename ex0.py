def judge_csv():
    csvfile=open("ex0_sample.csv",'r')
    a=csvfile.read()
    global arr
    arr=a.split()
    b=arr[0]
    c=b.split()
    n=["Name","Age","No"]
    if len(a and n) > 0:
        return True
    else:
        return Flase

def handle_csv():
    global arr
    if judge_csv():
        for a in arr:
            print(a)
    else :
        exit(o)

handle_csv()
