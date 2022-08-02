//1. A1은 3번 , A2는 2*A1 +1 , A3 = 3*A2 +1 ...

package recursive;

import java.util.Scanner;

public class P11729 {

	
//	이건 카운트 해주는 함수
	public static int hino(int N) { // 2^n - 1로 도 나타낼 수 있다. 등비수열과 등차수열 합쳐둔거라서 (멱급수라 하드나?)
		if (N==1) return 1;
		else return 2*hino(N-1)+1;
	}
	
//	카운트 해주는 함수말고 과정을 보여주는 함수
	public static void hinoProcess(int N,int start , int mid , int end) {
		
		if (N==1) {
			System.out.println(start + " " + end);
			return;
		}
		
		hinoProcess(N-1,start,end,mid);
		System.out.println(start + " " + end);
		hinoProcess(N-1,mid,start,end);
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		System.out.println(hino(N));
		hinoProcess(N,1,2,3);
		sc.close();
	}
}
