import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static boolean[] prime;
	public static void main(String[] args) throws IOException {
		
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		int M = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		
		prime = new boolean[N+1];
		get_prime();
		
		StringBuilder sb =new StringBuilder();
		//false 값이 소수이므로 !prime을 반복시켜서 출력한다.
		for(int i = M; i<=N; i++) {
			if(!prime[i]) sb.append(i).append('\n');
		}
		System.out.println(sb);
	}
	
	
	public static void get_prime() {
		
		prime[0] = prime[1] = true; //true = 소수x
		
		for(int i =2; i<=Math.sqrt(prime.length); i++) {
			if(prime[i]) continue; //prime[i]가 true면 continue
			
			for(int j=i*i; j<prime.length; j += i) {
				prime[j] = true; 
			}//j의 초기값은 Math.sqrt 이하의 소수를 제외한 해당 소수들의 배수이다.
			 //즉 2의 배수를 지우려면, j=2*2부터 시작해서 j+= 2 로 2의 배수를 true로 만든다.
		}
	}
	
}