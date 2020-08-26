package scpc;
import java.util.Scanner;
import java.util.Arrays;
import java.util.stream.Stream; 
/*
입력
2 TC

2 2 메뉴 몇일
1 2 a
4 2 b

3 2
6 3 1
1 4 3
출력
Case #1
5
Case #2
4
*/
public class Round1_1 {
	static int Answer;
	public static int diet (int menu, int day, String a, String b) {
		int[] listA = Stream.of(a.split(" ")).mapToInt(Integer::parseInt).toArray();
		int[] listB = Stream.of(b.split(" ")).mapToInt(Integer::parseInt).toArray();
		// System.out.println(Arrays.toString(listA));
		Arrays.sort(listA);
		Arrays.sort(listB);
		System.out.println(Arrays.toString(listB));
		
		return 0;
	}

	public static void main(String args[]) throws Exception	{
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 0; test_case < T; test_case++) {
			int menu = sc.nextInt();
			int day = sc.nextInt();
			sc.nextLine();
			String storeA = sc.nextLine();
			String storeB = sc.nextLine();
			Answer = diet(menu, day, storeA, storeB);
			System.out.println("Case #"+(test_case+1));
			System.out.println(Answer);
		}
	}
}
