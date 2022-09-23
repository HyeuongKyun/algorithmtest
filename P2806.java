package lecture.swea;

import java.util.Scanner;

public class P2806 {
	static int N;
	static boolean[][] v;
	static int[] arr;
	static int cnt;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		
		for(int tc=1;tc<=TC;tc++) {
			N = sc.nextInt();
			cnt=0;
			v = new boolean[N][N];
			dfs(0);
			System.out.printf("#%d %d\n",tc,cnt);
		}//for
		
		sc.close();
	}

	private static void dfs(int idx) {
		if(idx==N) {
			
//			for(int i=0;i<N;i++) {
//				if(!v[i]) return;
//			}
			cnt++;
			return;
		}//기저조건
		
		for(int i=0;i<N;i++) {
			
			if(check(i,idx)) {
				v[i] = true;
				dfs(idx+1);
				v[i] = false;
			}//if
		}//for
		
	}//dfs

	private static boolean check(int i,int idx) {
		if(v[i]) return false;
		for(int j=1;j<=idx;j++) {
			if(i-j>=0) 
				if(v[i-j]) return false;
			if(i+j<N) 
				if(v[i+j]) return false;
		}
		return true;
	}
	
	
}
