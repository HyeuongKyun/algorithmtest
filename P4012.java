package lecture.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P4012 {
	static int[][] arr;
	static boolean[] v;//���° ��Ḧ �������� ������ �迭
	static int N;
	
	private static void select(int start) {
		if(start==N/2) {
			
		}//������Ʈ
		
		
	}
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine());
		
		for(int tc=1;tc<=TC;tc++) {//�׽�Ʈ ���̽�
			
			N = Integer.parseInt(br.readLine());
			arr = new int[N][N];
			for(int i=0;i<N;i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for(int j=0;j<N;j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}//for
			}//for
			
			//�Է°� �ޱ� ��

			v = new boolean[N];
			
			select(0);
			
			
		}//for �ؽ�Ʈ���̽�
		
		br.close();
	}//main



}//class
