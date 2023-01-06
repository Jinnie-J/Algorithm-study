def solution(today, terms, privacies):
    answer = []
    
    def validate(date1, date2, term):
        date2_arr = list(map(int,date2.split(".")))
        date1_arr = list(map(int,date1.split(".")))
        
        date2_arr[1] += term
        if date2_arr[1]> 12:
            date2_arr[0] += date2_arr[1]//12
            date2_arr[1] -= (12 * (date2_arr[1]//12))
            if date2_arr[1]==0:
                date2_arr[0] -=1
                date2_arr[1]=12    
            
        date2_arr[2] -= 1
        if date2_arr[2] == 0:
            date2_arr[2] = 28
            date2_arr[1] -= 1     
            if date2_arr[1]==0:
                date2_arr[0] -=1
                date2_arr[1]=12
            
        if date1_arr[0] > date2_arr[0]:
            return True
        if date1_arr[0] == date2_arr[0] and date1_arr[1] > date2_arr[1]:
            return True
        if date1_arr[0] == date2_arr[0] and date1_arr[1] == date2_arr[1] and date1_arr[2] > date2_arr[2]:
            return True
        
        return False
    
    terms_dic={}
    for term in terms:
        a,b= term.split(" ")
        terms_dic[a]=b
        
    for i in range(len(privacies)):
        date, term = privacies[i].split(" ")
        if validate(today, date, int(terms_dic[term])):
            answer.append(i+1)
    
    return answer