import java.lang.reflect.Array;
import java.util.Arrays;

public class csStudy04 {
    public static void main(String[] args){
        int brown=24, yellow=24;
        int[] answer = {0,0};
        int tiles, row=0, col=0, tmp;
        tiles=brown+yellow;
        for(int i=1;i<=tiles;i++){
            if(tiles%i==0){
                row = i;
                col = tiles / row;
                if(col>row){
                    tmp = col;
                    col = row;
                    row = tmp;
                }
                if((row-2)*(col-2)==yellow)break;
            }
        }
        answer[0]=row;
        answer[1]=col;

        System.out.println(Arrays.toString(answer));
    }
}
