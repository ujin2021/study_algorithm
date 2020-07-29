package scpc;
import java.util.Arrays;
/*
�������� 21���� ������ �¸��Ѵ�. 
������ ������ �־����� ��, ������ ����������, Ȥ�� ������ ������ AliceȤ�� Bob�� �¸��Ͽ����� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.

�Է�
3
ABAAABBAAA
ABBAAAAAAAABAAAAAAAABAABAA
BBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAAAAAB
���
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
