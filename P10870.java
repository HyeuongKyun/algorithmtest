//1. Ǯ�̹�� 

//2. �ð����⵵ Big O O()

//3. �ڷᱸ��
package recursive;

import java.util.Scanner;

public class P10870 {

	public static int Fibonaci(int N) {
		if (N==0) return 0;
		else if (N==1) return 1;
		else return Fibonaci(N-1)+Fibonaci(N-2);
	}
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		System.out.println(Fibonaci(N));
		sc.close();
	}
	
}
