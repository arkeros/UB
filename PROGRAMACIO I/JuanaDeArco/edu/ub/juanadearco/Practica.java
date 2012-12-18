package edu.ub.juanadearco;

import edu.ub.juanadearco.actors.Heroina;
import edu.ub.juanadearco.actors.Menjar;
import edu.ub.juanadearco.actors.Bryan;
import edu.ub.juanadearco.actors.Escut;

/**
 *  
 * @author Rafa Arquero Gimeno
 */
public class Practica{
    private Joc joc;
    private Castell castell;
    private Heroina heroina;
    
    private static final int MAX_MENJAR_PER_HABITACIO = 7;
    
    private Practica() {
	int i, j;
        Habitacio h;

        castell = new Castell(3, 3);
        
        for(i = 0;i < castell.getNumPlantes();i++)
	    for(j = 0;j < castell.getNumHabitacions(i);j++)
		castell.addHabitacio(i, j, crearHabitacio(i, j));                        
        
        heroina = new Heroina();
        h = castell.getHabitacio(0, 0);
        int[] p = h.getPosicioCela(10, 10);
        heroina.setPosicioInicial(p[0], p[1]);
        
        joc = new Joc(castell, heroina);                            
        distribuirMenjar();
        colocarBryan();
        
        Escut escut = new Escut();    
        h = this.castell.getHabitacio(2, 2);  
        int[] cela = obtenirCelaLliure(h); 
        int[] posicio = h.getPosicioCela(8, 12);
        escut.setPosicioInicial(posicio[0], posicio[1]);        
        h.addActor(escut);   
        
        new JuanaDeArco(joc);      
    }
    
    private Habitacio crearHabitacio(int planta, int habitacio) {
	Habitacio h = Util.carregarHabitacio("h" + planta + "_" + habitacio + ".txt");
	Porta porta;
	
	if(planta == 0) {
	    if(habitacio == 0) {        
		porta = h.getPorta(13, 17);
		porta.setNumPlantaDesti(0);
		porta.setNumHabitacioDesti(1);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(6, 1));

		porta = h.getPorta(0, 10);
		porta.setNumPlantaDesti(0);
		porta.setNumHabitacioDesti(2);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(14, 10));

		porta = h.getPorta(16, 10);
		porta.setNumPlantaDesti(1);
		porta.setNumHabitacioDesti(0);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(1, 10));	    
	    } else if(habitacio == 1) {
		porta = h.getPorta(6, 0);
		porta.setNumPlantaDesti(0);
		porta.setNumHabitacioDesti(0);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(13, 16));	    
	    } else if(habitacio == 2) {
                //AQUESTA ES LA HABITACIO MISTERIOSA JEJE
		porta = h.getPorta(16, 10);
		porta.setNumPlantaDesti(0);
		porta.setNumHabitacioDesti(0);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(1, 10));
                
		porta = h.getPorta(16, 14);
		porta.setNumPlantaDesti(2);
		porta.setNumHabitacioDesti(2);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(12, 12));
                
		porta = h.getPorta(8, 0);
		porta.setNumPlantaDesti(0);
		porta.setNumHabitacioDesti(2);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(8, 23));
                
		porta = h.getPorta(8, 24);
		porta.setNumPlantaDesti(0);
		porta.setNumHabitacioDesti(2);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(8, 1));    
                
		porta = h.getPorta(8, 12);
		porta.setNumPlantaDesti(0);
		porta.setNumHabitacioDesti(2);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(8, 11));    
                
		porta = h.getPorta(0, 10);
		porta.setNumPlantaDesti(0);
		porta.setNumHabitacioDesti(2);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(1, 14));  
                
		porta = h.getPorta(0, 14);
		porta.setNumPlantaDesti(0);
		porta.setNumHabitacioDesti(2);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(1, 10));           
	    }	
	} else if(planta == 1) {
	    if(habitacio == 0) {	
		porta = h.getPorta(0, 10);
		porta.setNumPlantaDesti(0);
		porta.setNumHabitacioDesti(0);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(14, 10));
                
		porta = h.getPorta(8, 20);
		porta.setNumPlantaDesti(2);
		porta.setNumHabitacioDesti(0);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(14, 4));
                
		porta = h.getPorta(16, 10);
		porta.setNumPlantaDesti(1);
		porta.setNumHabitacioDesti(1);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(2, 2));
                
	    } else if(habitacio == 1) {                
		porta = h.getPorta(0, 2);
		porta.setNumPlantaDesti(1);
		porta.setNumHabitacioDesti(0);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(14, 10));
                
		porta = h.getPorta(8, 10);
		porta.setNumPlantaDesti(1);
		porta.setNumHabitacioDesti(2);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(8, 1));                
	    } else if(habitacio == 2) {	                
		porta = h.getPorta(8, 0);
		porta.setNumPlantaDesti(1);
		porta.setNumHabitacioDesti(1);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(8, 9));   	    
	    }		
	} else if(planta == 2) {
	    if(habitacio == 0) {	
		porta = h.getPorta(0, 12);
		porta.setNumPlantaDesti(2);
		porta.setNumHabitacioDesti(1);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(14, 12));
                
		porta = h.getPorta(16, 4);
		porta.setNumPlantaDesti(1);
		porta.setNumHabitacioDesti(0);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(10, 20));	    
	    } else if(habitacio == 1) {
		porta = h.getPorta(0, 12);
		porta.setNumPlantaDesti(2);
		porta.setNumHabitacioDesti(2);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(14, 12));
                
		porta = h.getPorta(16, 12);
		porta.setNumPlantaDesti(2);
		porta.setNumHabitacioDesti(0);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(2, 12));                
	    } else if(habitacio == 2) {                
		porta = h.getPorta(16, 12);
		porta.setNumPlantaDesti(2);
		porta.setNumHabitacioDesti(1);
		porta.setPosicioHabitacioDesti(h.getPosicioCela(2, 12));                
	    }		
	}
	
	return h;    
    }
    
    private void distribuirMenjar() {
        String[] menjars = {"Formatge", "Pollastre", "Poma"};
        // { calories,x,y,width,height } de cada imatge
        int[][] dades = {
            { 25, 28, 48, 34, 26 },
            { 50, 439, 14, 27, 23 },
            { 50, 510, 10, 30, 30 }
        };
        
        for (int i = 0; i < castell.getNumPlantes(); i++) {            
            for (int j = 0; j < castell.getNumHabitacions(i); j++) {
                Habitacio h = castell.getHabitacio(i, j);
                int numMenjars = (int)(Math.random() * (MAX_MENJAR_PER_HABITACIO + 1));
                
                for (int k = 0; k < numMenjars; k++) {
                    int[] cela = obtenirCelaLliure(h);
                    int imenjar = (int)(Math.random() * menjars.length);
                    Menjar m = new Menjar(menjars[imenjar], 
                            dades[imenjar][0], dades[imenjar][1], dades[imenjar][2], 
                            dades[imenjar][3], dades[imenjar][4]);
                    
                    int[] posicio = h.getPosicioCela(cela[0], cela[1]);
                    m.setPosicioInicial(posicio[0], posicio[1]);
                    h.addActor(m);                     
                }
            }            
        }
    }
    
    private void colocarBryan() {
        int i, j;
        
        Bryan bryan = new Bryan();       
        
        i = (int)(Math.random() * this.castell.getNumPlantes());
        j = (int)(Math.random() * this.castell.getNumHabitacions(i));
        Habitacio h = this.castell.getHabitacio(i, j);        
        
        int[] cela = obtenirCelaLliure(h); 
        int[] posicio = h.getPosicioCela(cela[0], cela[1]);
        bryan.setPosicioInicial(posicio[0], posicio[1]);
        
        h.addActor(bryan);         
    }
   
    private int[] obtenirCelaLliure(Habitacio h) {
        int fila = 0;
        int col = 0;
        int cela[] = null;
        boolean trobada = false;
        boolean terra = false;
        
        while (!trobada) {            
            terra = false;
            while (!terra) {
                fila = (int)(Math.random() * Constants.NUM_CELES_VERTICALS);
                col = (int)(Math.random() * Constants.NUM_CELES_HORIZONTALS);
                terra = h.getValor(fila, col) == Constants.SIMBOL_TERRA;
            }
            
            // comprovar que cap actor està dins la cela
            Actor[] actors = h.getActorsAsArray();
            int i = 0;
            boolean lliure = true;
            while (i < actors.length && lliure) {
                cela = h.getCela(actors[i].getPosicioInicial()[0], 
                        actors[i].getPosicioInicial()[1]);
                lliure = fila != cela[0] || col != cela[1];            
                i++;
            }         
            trobada = lliure;
        }
        return new int[] { fila, col };
    }
    

    /**
     * Principal.
     * 
     * @param args
     */
    public static void main(String[] args) {
        new Practica();
    }
    
}
