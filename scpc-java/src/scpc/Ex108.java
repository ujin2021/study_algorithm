package scpc;
import java.util.Arrays;
/*
배드민턴은 21점을 얻으면 승리한다. 
득점한 순서가 주어졌을 때, 게임이 진행중인지, 혹은 게임이 끝나서 Alice혹은 Bob가 승리하였는지 출력하는 프로그램을 작성하시오.

입력
3
ABAAABBAAA
ABBAAAAAAAABAAAAAAAABAABAA
BBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAAAAAB
출력
Case #1
Playing
Case #2
Alice
Case #3
Bob
*/
import java.util.Scanner;
import java.util.Arrays;
public class Ex108 {
	static String Answer;
	
	public static String win(String score) {
		int len = score.length();
		if(len < 21)
			return "Playing";
		String[] arr = score.split("");
		int a = 0;
		int b = 0;
		for(int i = 0; i < len; i++) {
			if(arr[i].equals("A")) {
				a++;
				if (a == 21) {
					return "Alice";
				}
			}
			else {
				b++;
				if (b == 21) {
					return "Bob";
				}
			}
		}
		return "Playing";
	}

	public static void main(String args[]) throws Exception	{
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 0; test_case < T; test_case++) {
			String score = sc.next();
			Answer = win(score);
			System.out.println("Case #"+(test_case+1));
			System.out.println(Answer);
		}
	}
}
