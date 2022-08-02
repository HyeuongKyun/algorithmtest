//1. A1�� 3�� , A2�� 2*A1 +1 , A3 = 3*A2 +1 ...

package recursive;

import java.util.Scanner;

public class P11729 {

	
//	�̰� ī��Ʈ ���ִ� �Լ�
	public static int hino(int N) { // 2^n - 1�� �� ��Ÿ�� �� �ִ�. �������� �������� ���ĵаŶ� (��޼��� �ϵ峪?)
		if (N==1) return 1;
		else return 2*hino(N-1)+1;
	}
	
//	ī��Ʈ ���ִ� �Լ����� ������ �����ִ� �Լ�
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
