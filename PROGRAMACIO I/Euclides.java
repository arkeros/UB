import java.util.Scanner;

public class Euclides {
	public static int mcd(int a, int b) {
		int tmp;//var auxiliar per intercanviar els nombres

		while (b != 0) {
			tmp = b;
			b = a % b;
			a = tmp;
		}
		
		return a;
	}

	public static int mcm(int a, int b) {
		//L'unio dels dos es la suma menys un cop l'interseccio (per que la contem dos cops)

		return a * b / mcd(a, b);
	}

	public static void main(String[] args) {
		int a, b, mcd, mcm;
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Introdueix un nombre: ");
		a = sc.nextInt();
		System.out.print("Introdueix un altre nombre: ");
                b = sc.nextInt();

		if(a > 0 && b > 0) {
			mcd = mcd(a, b);
			mcm = mcm(a, b);

			System.out.println("El mcd de " + a + " y " + b + " es " + mcd + ".");
			System.out.println("El mcm de " + a + " y " + b + " es " + mcm + ".");
		} else {
			System.out.println("Aquest programa nomes accepta numeros enters positius.");
		}
	}
}
