package scpc;
/*
������ ���� 10���� �̻��� �Ǹ� �ǹ� ��ư��, 100���� �̻��� �Ǹ� ��� ��ư��, 1,000���� �̻��� �Ǹ� ���̾Ƹ�� ��ư�� ������ �ش�. 
� ����Ʃ���� ������ ���� �־����� ��, ���������� ���� �÷��̹�ư�� ���� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.

�Է� ���Ͽ��� ���� �׽�Ʈ ���̽��� ���Ե� �� �ִ�.
������ ù° �ٿ� �׽�Ʈ ���̽��� ������ ��Ÿ���� �ڿ��� T �� �־�����,
���� ���ʷ�  T ���� �׽�Ʈ ���̽��� �־�����. (1 �� T �� 50)
�� �׽�Ʈ ���̽��� �Է��� ������ ���� �����̴�.
ù ��° �ٿ� ����Ʃ���� ������ ���� ��Ÿ���� �ڿ����� �־�����. �־����� ������ ���� 1����� ���� �ʴ´�.
*/
/*
�Է�
4
1432
192314
3635904
10000009
���
Case #1
NONE
Case #2
SILVER
Case #3
GOLD
Case #4
DIAMOND
*/
import java.util.Scanner;

public class Ex112 {
	static int Answer;
	static String[] Arr = {"NONE", "SILVER", "GOLD", "DIAMOND"};
	public static int button(int sub) {
		int top = sub / 100000 ;
		if(top == 0)
			Answer = 0;
		else if(1 <= top && top < 10) 
			Answer = 1;
		else if(10 <= top && top < 100) 
			Answer = 2;
		else
			Answer = 3;
		return Answer;
	}
	public static void main(String args[]) throws Exception	{
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 0; test_case < T; test_case++) {
			int sub = sc.nextInt();
			Answer = button(sub);
			System.out.println("Case #"+(test_case+1));
			System.out.println(Arr[Answer]);
		}
	}
}
