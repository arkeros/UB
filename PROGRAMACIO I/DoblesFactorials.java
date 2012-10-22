//By: Rafa Arquero Gimeno
import java.util.Scanner;

public class DoblesFactorials {
	public static long  factorial2(int n) {
		if (n <= 0) return 1;//casos especials

		return n * factorial2(n - 2);//casos generals
	}

        public static void main(String[] args) {
                int n, i;
                Scanner scan = new Scanner(System.in);

                System.out.print("Escriu un nombre enter: ");
                n = scan.nextInt();
		for(i = 0;i < n;i++)//segons l'exemple, es compren un < i no pas un <=
		{   
                	System.out.print(factorial2(i) + " ");
		}      

		//per que la sortida del programa sigui amb \n
		System.out.println();
        }
}

