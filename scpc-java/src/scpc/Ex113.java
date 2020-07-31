package scpc;
/*
포함되는 1의 개수를 Population count, 줄여서 popcount라고 부른다. 
자연수 N이 주어졌을 때, N의 popcount를 구하는 프로그램을 작성하시오. 
예를 들어, 13을 이진수로 나타내면 1101이 되며, 13의 popcount는 3
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
