public class csStudy01 {
    class Solution {
        public int solution(int[][] sizes) {
            int tmp = 0;
            int answer = 0;
            int max = 0, tmpMax=0;
            for(int i=0;i<sizes.length;i++){
                for(int j=0;j<sizes[i].length;j++){
                    if(max<sizes[i][j])max=sizes[i][j];
                }
            }
            //System.out.println(max);
            for(int i=0;i<sizes.length;i++){
                tmp = min(sizes[i][0],sizes[i][1]);
                if(tmp>tmpMax)tmpMax=tmp;
            }
            //System.out.println(tmpMax);
            answer = max * tmpMax;
            return answer;
        }
        int min(int a, int b){
            if(a>b)return b;
            else return a;
        }
    }
}
