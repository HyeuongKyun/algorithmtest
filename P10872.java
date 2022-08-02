//1. 풀이방법 

//2. 시간복잡도 Big O O()

//3. 자료구조
package recursive;

import java.util.Scanner;

public class P10872 {

	public static int pectorial(int N) {
		if (N>0) return N*pectorial(N-1);
		else return 1;
	}
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		System.out.println(pectorial(N));
		sc.close();
	}
	
}
