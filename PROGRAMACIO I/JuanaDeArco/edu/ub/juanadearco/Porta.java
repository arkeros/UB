
package edu.ub.juanadearco;

/**
 * Cada porta és situa en un punt dintre del mapa (fila i columna) i conté 
 * la informació de l'habitació amb la que és comunica, així com la posició x,y
 * a l'entrar.
 * 
 * @author danieldelrio@ub.edu
 */
public class Porta {

    private int fila;
    private int columna;
    private int numPlantaDesti = -1;
    private int numHabitacioDesti = -1;
    private int[] posicioHabitacioDesti;
    private boolean oberta = true;
    
    public static final short PORTA_TANCADA = 0;
    public static final short PORTA_OBERTA = 1;
    
    public Porta(int fila, int columna) {
        this.fila = fila;
        this.columna = columna;
    }

    public int getFila() {
        return fila;
    }
    
    public int getColumna() {
        return columna;
    }

    public int getNumHabitacioDesti() {
        return numHabitacioDesti;
    }

    public void setNumHabitacioDesti(int numHabitacioDesti) {
        this.numHabitacioDesti = numHabitacioDesti;
    }

    public int[] getPosicioHabitacioDesti() {
        return posicioHabitacioDesti;
    }

    public void setPosicioHabitacioDesti(int[] posicioHabitacioDesti) {
        this.posicioHabitacioDesti = posicioHabitacioDesti;
    }

    public boolean isOberta() {
        return oberta;
    }
    
    public void tancar() {
        this.oberta = false;
    }
    
    public void obrir() {
        this.oberta = true;
    }

    public int getNumPlantaDesti() {
        return numPlantaDesti;
    }

    public void setNumPlantaDesti(int numPlantaDesti) {
        this.numPlantaDesti = numPlantaDesti;
    }
        
}
