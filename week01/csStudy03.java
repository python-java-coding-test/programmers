import java.util.ArrayList;

public class csStudy03 {
    static int count = 0;
    static ArrayList history = new ArrayList();
    public static void main(String[] args){
        String numbers="011";
        int length = numbers.length();
        for(int i=1;i<=length;i++){
            String one = numbers.substring(i-1,i);
            f(one,1, length, numbers.replaceFirst(one, ""));
        }
        System.out.println(count);
    }
    private static void f(String now, int dep, int l, String full) {
        if(dep>l) return;
        //System.out.println("now: "+now+" full: "+full+" dep: "+dep);
        int num=Integer.parseInt(now);
        if(isPrime(num) && !history.contains(num)){
            history.add(num);
            count+=1;
        }
        for(int i=1;i<=full.length();i++){
            String tmp = full.substring(i-1,i);
            now += tmp;
            String newFull = full.replaceFirst(tmp, "");
            f(now, dep+1, l, newFull);
            now = now.substring(0,now.length()-1);
        }
    }

    private static boolean isPrime(int n) {
        boolean res = true;
        if(n<=1)return false;
        for(int i=2;i<=Math.sqrt(n);i++){
            if(n%i==0){
                res = false;
                break;
            }
        }
        return res;
    }
}
