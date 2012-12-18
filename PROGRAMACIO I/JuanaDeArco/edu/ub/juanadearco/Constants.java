
package edu.ub.juanadearco;

import java.awt.event.KeyEvent;

/**
 * Constants del programa utilitzades freqüentment.
 * 
 * @author danieldelrio@ub.edu
 */
public interface Constants {

    /**
     * Número de frames per segon (50).
     */
    public int FRAMES_PER_SEGON = 50;
    
    public int AMPLADA_FINESTRA = 800;
    public int ALCADA_FINESTRA = 576;
    
    public char SIMBOL_PORTA = 'p';
    public char SIMBOL_MUR = 'x';
    public char SIMBOL_TERRA = '0';
 
    public short DIRECCIO_NORD = 1;
    public short DIRECCIO_SUD = 2;
    public short DIRECCIO_EST = 3;
    public short DIRECCIO_OEST = 4;
    
    public int KEY_UP = KeyEvent.VK_UP;
    public int KEY_DOWN = KeyEvent.VK_DOWN;
    public int KEY_LEFT = KeyEvent.VK_LEFT;
    public int KEY_RIGHT = KeyEvent.VK_RIGHT;
    
    public int NUM_CELES_HORIZONTALS = 25;
    public int NUM_CELES_VERTICALS = 17;
    public int AMPLADA_CELA = 32;
    public int ALCADA_CELA = 32;
    
    public int ESTAT_INACTIU = 0;
    public int ESTAT_ACTIU = 1;
           
}
