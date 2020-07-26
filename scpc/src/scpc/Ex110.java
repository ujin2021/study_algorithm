package scpc;
/*
 태양이는 햄버거 장사를 하고있다. 햄버거 한 개를 만들기 위해서, 빵 2개와 고기 패티 1장, 그리고 양상추 3장이 필요하다. 
 빵, 고기 패티, 양상추의 개수가 각각 주어졌을 때, 최대 몇 개의 햄버거를 만들 수 있는지 구하여라.
 
입력 파일에는 여러 테스트 케이스가 포함될 수 있다.
파일의 첫째 줄에 테스트 케이스의 개수를 나타내는 자연수 T 가 주어지고,
이후 차례로  T 개의 테스트 케이스가 주어진다. (1 ≤ T ≤ 30)
각 테스트 케이스의 첫 줄에 음이 아닌 정수 3개가 주어진다. 이는 1000보다 작거나 같으며, 각각의 수는 빵, 고기 패티, 양상추의 개수를 나타낸다.
*/
/*
입력
3
1 2 3
2 1 3
10 10 10
출력
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