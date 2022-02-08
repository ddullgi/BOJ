import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		int N = Integer.parseInt(br.readLine());
		
		if(N==1) {
			System.out.print("666");
		} else {
			func(N);
		}
		
		
	}
	public static void func(int N) {
		int count = 1;
		int prev_num =0;
		int after_num=0;
				
			while(true) {
				//prev_num의 1000의 자릿수부터 666으로 시작할 때
				if((prev_num %10000)/10 == 666 && prev_num%10 !=6) {
					for(int i =0; i<1000; i++) {
						if(count == N) {
							System.out.print(prev_num*1000+after_num);
							return;
						}
						count++;
						after_num++;
					}
					prev_num++;
				}
				//prev_num의 100의 자릿수부터 666으로 시작할 떄,
				else if(prev_num %1000 ==666) {
					after_num = 0;
					for(int i=0; i<1000; i++) {
						if(count == N) {
							System.out.print(prev_num*1000 +after_num);
							return;
						}
						count++;
						after_num++;
					}
					prev_num++;
				}
				
				//prev_num의 10의 자릿수부터 66으로 시작할 때, after_num의 100의 자릿수 = 6
				else if(prev_num %100 ==66) {
					after_num = 600;
					for(int i =0; i<100; i++) {
						if(count == N) {
							System.out.print(prev_num * 1000 + after_num);
							return;
						}
						count++;
						after_num++;
						
					}
					prev_num++;
				}
				//prev_num의 1의 자릿수가 6으로 시작할때, after_num의 100, 10의 자릿수 =6
				else if(prev_num %10 ==6) {
					after_num = 660;
					for(int i =0; i<10; i++) {
						if(count ==N) {
							System.out.print(prev_num*1000 + after_num);
							return;
						}
						after_num++;
						count++;
						
					}
					prev_num++;
				}
				//뒷자릿수가 666이고, prev_num의 1의 자리까지 6이 아닌 경우
				else {
					after_num = 666;
					if(count == N) {
						System.out.print(prev_num *1000 + after_num);
						return;
					}
					count++;
					prev_num++;
				}
			}
	}
	
}