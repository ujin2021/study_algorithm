package scpc;
/*
 �¾��̴� �ܹ��� ��縦 �ϰ��ִ�. �ܹ��� �� ���� ����� ���ؼ�, �� 2���� ��� ��Ƽ 1��, �׸��� ����� 3���� �ʿ��ϴ�. 
 ��, ��� ��Ƽ, ������� ������ ���� �־����� ��, �ִ� �� ���� �ܹ��Ÿ� ���� �� �ִ��� ���Ͽ���.
 
�Է� ���Ͽ��� ���� �׽�Ʈ ���̽��� ���Ե� �� �ִ�.
������ ù° �ٿ� �׽�Ʈ ���̽��� ������ ��Ÿ���� �ڿ��� T �� �־�����,
���� ���ʷ�  T ���� �׽�Ʈ ���̽��� �־�����. (1 �� T �� 30)
�� �׽�Ʈ ���̽��� ù �ٿ� ���� �ƴ� ���� 3���� �־�����. �̴� 1000���� �۰ų� ������, ������ ���� ��, ��� ��Ƽ, ������� ������ ��Ÿ����.
*/
/*
�Է�
3
1 2 3
2 1 3
10 10 10
���
Case #1
0
Case #2
1
Case #3
3
 */
import java.util.Scanner;
public class Ex110 {
	static int Answer;
	
	public static int hamburger(int bread, int meat, int let) {
		int bread_pair = bread / 2;
		int meat_pair = meat / 1;
		int let_pair = let / 3;
		if(bread_pair == 0 || meat_pair == 0 || let_pair == 0) {
			Answer = 0;
		}
		
		if (bread_pair > meat_pair) {
			if(meat_pair > let_pair)
				Answer = let_pair;
			else
				Answer = meat_pair;
		}
		else {
			if(bread_pair > let_pair)
				Answer = let_pair;
			else
				Answer = bread_pair;
		}
			
		return Answer;
	}
	public static void main(String args[]) throws Exception	{
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); // test case
		for(int test_case = 0; test_case < T; test_case++) {
			int bread = sc.nextInt();
			int meat = sc.nextInt();
			int lettuce = sc.nextInt();
			Answer = hamburger(bread, meat, lettuce);
			System.out.println("Case #"+(test_case+1));
			System.out.println(Answer);
		}
	}
}