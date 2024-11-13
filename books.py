from collections import OrderedDict
cash=OrderedDict({
  0.5:0,
  1:0,
  2:0,
  5:0,
  10:0,
  20:0,
  50:0
})
records=OrderedDict({
  "total":0,
  "customers":0,
  "eftpos":0,
  "extra cash":0
})
step=2
totalcash=0
setcash=0
def main():
  global cash
  global records
  global step
  global totalcash
  global setcash
  a50=0
  a20=0
  a10=0
  for x in cash:
    rerun = True
    while rerun:
      rerun = False
      try:
        cash[x]=round(float(input("till "+str(step)+" $"+str(x)+" cash value")),2)
      except ValueError:
        rerun = True
        print("Invalid input. Try again")
    totalcash+=cash[x]
    setcash+=cash[x]
  setcash-=250
  while setcash>=10 and (cash[50]>0 or cash[20]>0 or cash[10]>0):
    if setcash>=50 and cash[50]>0:
      setcash-=50
      cash[50]-=50
      a50+=1
    else:
      if setcash>=20 and cash[20]>0:
        setcash-=20
        cash[20]-=20
        a20+=1
      else:
        if setcash>=10 and cash[10]>0:
          setcash-=10
          cash[10]-=10
          a10+=1
  if setcash<0:
    print("$"+str(-setcash)+" missing")
  else:
    print("remove "+str(a50)+" * $50, "+str(a20)+" * $20, "+str(a10)+" * $10")
    if setcash>=10:
      print("remove $"+str(setcash)+" more")
  for x in records:
    rerun = True
    while rerun:
      rerun = False
      try:
        records[x]+=float(input("till "+str(step)+" "+str(x)))
      except ValueError:
        rerun = True
        print("Invalid input. Try again")
    records[x] = round(records[x],2)
  for x in cash:
    cash[x]=0
  setcash=0
  if step==2:
    step=1
    main()
  if step==1:
    step=2
    results()
def results():
  global records
  global totalcash
  cashrec=records["total"]-records["eftpos"]
  ave=round(records["total"]/records["customers"],2)
  totalcash-=cashrec+500
  totalcash = round(totalcash,2)
  print("total: $"+str(records["total"])+"\neftpos: $"+str(records["eftpos"])+"\ncash: $"+str(cashrec))
  print("customers: "+str(round(records["customers"]))+"\naverage: $"+str(ave))
  if totalcash>=10:
    print("$"+str(totalcash)+" over")
  if totalcash<=-10:
    print("$"+str(-totalcash)+" under")
  for x in records:
    records[x]=0
  totalcash=0
  cashrec=0
  ave=0
  input("continue")
  main()
main()