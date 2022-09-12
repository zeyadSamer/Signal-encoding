import time

# note , i assumed that i have even number of ones at the beggining

asciFile=open("input.txt","r")
originalData=asciFile.read()

print("Original Data:"+originalData)

datalength=len(originalData)


output="" 


zeroCounter=0
onesCounter=0
i=0
while(i<datalength):

    
 
     #zero case
    if(originalData[i]=='0'):
        ## checking how much is left from the string , if less than 4 chars is left then 4 zeroes case willnot happen
        #if(datalength - i >=4):
             

        #checking no 4 zeros occurs first 

          if (datalength-i>=4 and originalData[i+1]=='0' and originalData[i+2]=='0' and originalData[i+3]=='0' ):


            # checking the number of previos ones
               if(onesCounter%2==0):
            #applying bipolar
                #checking perceding pulse bit

                   #debug 
                    
                     if(output[i-1]=='-'):
                       
                       output=output+'+'+'0'+'0'+'+'
                       i+=3
                       onesCounter+=2
                       
                     elif(output[i-1]=='+'):
                    
                        output=output+'-'+'0'+'0'+'-'
                        i+=3
                        onesCounter+=2

            # not even  number of ones
               else:
                      if(output[i-1]=='-'):
                           
                           output=output+'0'+'0'+'0'+'-'
                           
                           i+=3
                           onesCounter+=1


                
                    
                      elif(output[i-1]=='+'):
                           output=output+'0'+'0'+'0'+'+'
                           i+=3
                           onesCounter+=1



                   

          else:
                 output+='0'            
                




   ## 1 case
    else:
         

         if(onesCounter%2==0):
              output+='+'
         else:
              output+='-'    

              
         onesCounter+=1
  
  
    i+=1
   


   
print("encoded data:"+output)
    
outputFile=open("hdb3Output.txt",'a')
outputFile.write(output)
outputFile.close()


print("data encoded successfully in hdb3Output.txt")
time.sleep(5)    



    

