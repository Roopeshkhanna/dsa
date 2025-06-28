public class celebrity {
    public static void main(String[] args) {
        int mat[][]={{0,1,1,0},{0,0,0,0},{0,1,0,0},{1,1,0,0}};
        int top=0,down=mat.length-1;
        int s=0;
        while(top<down){
            if(mat[top][down]==1){
                top++;
            }
            else if(mat[down][top]==1){
                down--;
            }
        }
        if(top<down){
            System.out.println("no celebrity");

        }
        else{
            for(int i=0;i<mat.length;i++){
                if(top==i){
                    
                    continue;
                }
                if(mat[top][i]!=0 || mat[i][top]!=1){
                    s=1;
                    System.out.println("no celebrity");
                    break;

                }


            }
            if(s!=1){
                System.out.println(top);
            }
        }
    }
    
}
