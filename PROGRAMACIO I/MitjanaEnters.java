// @author Rafa
import java.util.Scanner;

public class MitjanaEnters {
    
    //L'argument freqs es un array amb les frequencies que apareixen el nombres:
    // de la forma nombre => vegades (key => value) 
    public static double average(int[] freqs) {
        int n, sum = 0, times = 0;//sum guarda la suma, times per sabes per quant hem de dividir despres
        
        for(n = 0;n < freqs.length;n++) {
            sum += n * freqs[n];
            times += freqs[n];
        }
        
        return 1.0 * sum / times;//*1.0 per pasar-ho a double, si no dividiria sense decimals...
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, count;
        int[] notes = new int[11];//hi han nomes 11 notes posibles: 0, 1, ..., 10
        double average;
        
        System.out.println("Introdueix notes enteres entre 0 i 10. Per acabar -1");
        
        do {  
            do {            
                System.out.print("Introdueix una nota: ");
                n = sc.nextInt();
                
                if(n < -1 || n > 10)
                    System.out.println("[!] Entrada invalida, siusplau, introdueix nombres enters entre 0 i 10. Per acabar -1");
            } while(n < -1 || n > 10);//per evitar que introdueixi nombres imposibles 
            
            if(n != -1)//en aquest punt del programa, per a n l'unic valor invalid posible es -1
                notes[n]++;     
        } while(n != -1);
        
        average = average(notes); 
        count = 0; //guarda el nombre d'elements per sota de average (mitjana)
        n = 0;
        while(n < average && n <= 10) 
            count += notes[n++];//++ s'executa despres de donar el valor
        
        System.out.println("Hi han " + count + " notes per sota de la mitjana (" + average + ").");
    }
}
