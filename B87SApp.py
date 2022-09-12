import time


asciFile=open("input.txt","r")
originalData=asciFile.read()

print("original data:",originalData)

datalength=len(originalData)

output=""

lastPolarity="-"

flag=False
onesCounter=0

def checkEightZeroes(index):
      for j in range(1,8):
                    if(originalData[index+j]=='0'):
                         flag=True
                    else:
                         flag=False
                         break
      return flag               


i=0

while(i<datalength):


     #Case 1
     if(originalData[i]=='1'):
          if(lastPolarity=='-'):
              
               output+='+'
               lastPolarity='+'

          else:# if lastpolarity +ve
                 
                 output+='-'
                 lastPolarity='-'



   #Case 0
     else:
          if(datalength-i>=8):
               #finding 8 zeroes
               flag=checkEightZeroes(i)
              
          else:
               output+='0' 
               i+=1
               continue            ## should continue

          # if we found * zeroes flag will be equal true,then we will do the following
          if(flag==True):
               #000
               for j in range(0,3):
                  
                    output+='0'


               #V
               if(lastPolarity=='+'):
                   output+='+'
                   onesCounter+=1
                   lastPolarity='+'
                 
               else:
                  output+='-'
                  onesCounter+=1
                  lastPolarity='-'
                

               #B
               if(lastPolarity=='-'):
                   output+='+'
                   onesCounter+=1
                   lastPolarity='+'
                
               else:
                    output+='-'
                    onesCounter+=1
                    lastPolarity='-'
                   


               #0

               output+='0'

               #V
               if(lastPolarity=='+'):
                   output+='+'
                   onesCounter+=1
                   lastPolarity='+'
               else:
                  output+='-'
                  onesCounter+=1
                  lastPolarity='-'


               #B again
               if(lastPolarity=='-'):
                   output+='+'
                   onesCounter+=1
                   lastPolarity='+'
               else:
                    output+='-'
                    onesCounter+=1
                    lastPolarity='-'
          
               i+=7
          # case 8 places were found but no 8 zeroes(flag=flase)  
          else:
               output+='0'        


     i=i+1
     flag=False
    



print(output)


OutputFile=open("B87SEncoded.txt","a")
OutputFile.write(output)
OutputFile.close()

print("data encoded successfully in B87SEncoded.txt")
time.sleep(5)


