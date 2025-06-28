import java.util.*;

public class infixtopostfix {

    public static void main(String args[]){
        Scanner input = new Scanner(System.in);
        String exp = "(p+q)*(m-n)";
        Stack<Character> st = new Stack<>();
        String res = "";

        for(char ch : exp.toCharArray()){
            if(Character.isLetterOrDigit(ch)){
                res += ch;
            }
            else if(ch == '('){
                st.push(ch);
            }
            else if(ch == ')'){
                while(!st.isEmpty() && st.peek() != '('){
                    res += st.pop();
                }
                st.pop();
            }
            else {
                while(!st.isEmpty() && precedence(ch) <= precedence(st.peek())){
                    res += st.pop();
                }
                st.push(ch);
            }
        }

        while(!st.isEmpty()){
            res += st.pop();
        }

        System.out.println(res);
    }

    static int precedence(char ch){
        switch (ch) {
            case '*':
            case '/':
                return 2;
            case '+':
            case '-':
                return 1;
            case '^':
                return 3;
        }
        return -1;
    }
}
