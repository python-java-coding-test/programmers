import java.util.ArrayList;

public class csStudy05 {
    static int answer = -1;
    static ArrayList explored = new ArrayList();
    public static void main(String[] args){
        int k=80;
        int[][] dungeons = {{80,20},{50,40},{30,10}};
        for(int i=0;i< dungeons.length; i++){
            if(dungeons[i][0]<=k){
                explored.add(Integer.toString(i));
                explore(k-dungeons[i][1],dungeons);
                explored.remove(Integer.toString(i));
            }
        }
        System.out.println(answer);
    }

    private static void explore(int k, int[][] dungeons) {
        if(answer<explored.size())answer=explored.size();
        for(int i=0;i< dungeons.length; i++){
            if(!explored.contains(Integer.toString(i)) && k>=dungeons[i][0]){
                int now=k-dungeons[i][1];
                explored.add(Integer.toString(i));
                explore(now, dungeons);
                explored.remove(Integer.toString(i));
            }
        }
    }
}
