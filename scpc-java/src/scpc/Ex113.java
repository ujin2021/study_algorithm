package scpc;
/*
���ԵǴ� 1�� ������ Population count, �ٿ��� popcount��� �θ���. 
�ڿ��� N�� �־����� ��, N�� popcount�� ���ϴ� ���α׷��� �ۼ��Ͻÿ�. 
���� ���, 13�� �������� ��Ÿ���� 1101�� �Ǹ�, 13�� popcount�� 3
*/
import java.util.Scanner;
import java.lang.Integer;
public class Ex113 {
	static int Answer;
	public static int popcount(int num) {
		Answer = 0;
		String toBin = Integer.toBinaryString(num);
		String[] arr = toBin.split("");
		for(int i = 0; i < arr.length; i++) {
			if(arr[i].equals("1"))
				Answer++;
		}
		return Answer;
	}
	public static void main(String args[]) throws Exception	{
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 0; test_case < T; test_case++) {
			System.out.println("Case #"+(test_case+1));
			int num = sc.nextInt();
			Answer = popcount(num);
			System.out.println(Answer);
		}
	}
}
