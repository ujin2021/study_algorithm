package scpc;
import java.util.Scanner;
public class Ex114 {
	static String Answer;
	public static String getTime (String start, String end) {
		String[] start_arr = start.split(":");
		String[] end_arr = end.split(":");
		int hours = Integer.parseInt(end_arr[0]) - Integer.parseInt(start_arr[0]);
		int minutes = Integer.parseInt(end_arr[1]) - Integer.parseInt(start_arr[1]);
		if(minutes < 0) {
			hours -= 1;
			minutes += 60;
		}
		Answer = String.format("%02d:%02d", hours, minutes);
		return Answer;
	}
	public static void main(String args[]) throws Exception	{
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int test_case = 0; test_case < T; test_case++) {
			String start = sc.next();
			String end = sc.next();
			Answer = getTime(start, end);
			System.out.println("Case #"+(test_case+1));
			System.out.println(Answer);
		}
	}
}
