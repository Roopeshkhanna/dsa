import java.util.*;
class matrixmul{
    public static void main(String args[]){
        int mat1[][]={{1,1,1},{1,1,1},{1,1,1}};

        int mat2[][]={{1,1,1},{1,1,1},{1,1,1}};
        Scanner input =new Scanner(System.in);
        int c[][]=new int[3][3];
            for(int i=0;i<=2;i++){
            for(int j=0;j<=2;j++){
                c[i][j]=0;
                for(int k=0;k<3;k++){
                    c[i][j]+=mat1[i][k]*mat2[k][j];


                }


            }
        }
        for(int i=0;i<=2;i++){
            for(int j=0;j<=2;j++){
                System.out.print(c[i][j]+" ");

        }
        System.out.println();
        


    }
}
}