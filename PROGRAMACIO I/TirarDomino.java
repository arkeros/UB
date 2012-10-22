import java.util.Scanner;

public class TirarDomino {


  public static void main(String[] args)
  {
    Scanner scan = new Scanner(System.in);
    int table;
    int[] hand = new int[5];
    int i, piece, matches = 0;
    boolean valid;
    
    System.out.print("Quina fitxa hi ha a la taula? ");
    table = scan.nextInt;
    
    for(i = 0;i < 5;i++)
    {
      System.out.print("Escriu la " + (i + 1) + "a fitxa de la teva ma: ");
      hand[i] = scan.nextInt();     
    }
    
    for(i = 0;i < 5;i++)
    {
	piece = hand[i];
	valid = Math.round(piece / 10) ==  Math.round(table / 10) ||
	  Math.round(piece / 10) == table % 10 ||
	  piece % 10 == Math.round(table / 10) ||
	  piece % 10 == table % 10;
	  
	if(valid) matches++; 
    }
    
    System.out.println(matches);
    
  }

}
