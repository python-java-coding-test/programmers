import java.util.Arrays;

public class csStudy02 {
    public static void main(String[] args){
        int[] answers = {1,3,2,4,2};
        int maxNum=0, ansCount=0;
        int[][] pattern = {{1,2,3,4,5},{2,1,2,3,2,4,2,5},{3,3,1,1,2,2,4,4,5,5}};
        int[] count = {0,0,0};
        int[] idx = {0,0,0};

        for(int i=0;i<answers.length;i++){
            for(int j=0;j<3;j++) {
                if (answers[i] == pattern[j][idx[j]]) count[j] += 1;
                idx[j]+=1;
                if(idx[j]>=pattern[j].length)idx[j]=0;
            }
        }
        for(int i=0;i<3;i++){
            if(maxNum<count[i])maxNum=count[i];
        }
        for(int i=0;i<3;i++){
            if(count[i]==maxNum)ansCount+=1;
        }
        int[] answer = new int[ansCount];
        ansCount=0;
        for(int i=0;i<3;i++){
            if(count[i]==maxNum){
                answer[ansCount]=i+1;
                ansCount+=1;
            }
        }
        System.out.println(Arrays.toString(answer));
    }
}
