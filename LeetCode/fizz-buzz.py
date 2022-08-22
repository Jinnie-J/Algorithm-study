
# Time Limit Code

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:   
        answer=[str(i) for i in range(n+1)]
    
        i=15
        while i<=n:
            answer[i]= "FizzBuzz"
            i+=15
        
        i=3
        while i<=n:
            if answer[i] != "FizzBuzz":
                answer[i]="Fizz"
                i+=3
        
        i=5
        while i<=n:
            if answer[i] != "FizzBuzz":
                answer[i]="Buzz"
                i+=5
                
        answer.pop(0)
        return answer


# Accepted Code

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        answer=[str(i) for i in range(1,n+1)]
        for i in range(1,n+1):
            if i%15==0:
                answer[i-1]= "FizzBuzz"
            
            elif i%3==0:
                answer[i-1] = "Fizz"
                
            elif i%5==0:
                answer[i-1] = "Buzz"
                
        return answer        

            