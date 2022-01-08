class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int nowL = 10;
        int nowR = 12;

        for(int number: numbers){
            if(number==1 || number==4 || number==7){
                answer+="L";
                nowL = number;
            }else if(number ==3 || number==6 || number==9){
                answer+="R";
                nowR = number;
            }else{
                int leftLen = getLen(nowL,number);
                int rightLen = getLen(nowR, number);

                if(leftLen > rightLen){
                    answer+="R";
                    nowR=number;
                }else if(leftLen < rightLen){
                    answer+="L";
                    nowL=number;
                }else{
                    if(hand.equals("right")){
                        answer+="R";
                        nowR=number;
                    }else{
                        answer+="L";
                        nowL=number;
                    }
                }
            }
        }
        return answer;
    }

    public static int getLen(int index, int number){
        index = (index==0) ? 11: index;
        number = (number ==0) ? 11: number;

        int x = (index-1)/3;
        int y = (index-1)%3;
        int numX= number/3;
        int numY= 1;

        return Math.abs(x-numX)+ Math.abs(y-numY);
    }
}