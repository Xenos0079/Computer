public class test {
    public static void main(String[] args){
        int i = 1;
        System.out.println("before change, i = "+i);
        change(i);
        System.out.println("after change, i = "+i);
    }
    public static void change (int i){
        i = 5;
    }
}
