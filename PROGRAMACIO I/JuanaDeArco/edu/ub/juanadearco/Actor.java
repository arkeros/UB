
package edu.ub.juanadearco;

import java.awt.Rectangle;

/**
 * Intefície que defineix els mètodes d'un Actor.
 * 
 * @author danieldelrio@ub.edu
 */
public interface Actor extends Renderable {

    /**
     * Inicialitza les dades de l'actor.
     */
    public void inicialitzar();
    
    /**
     * Estableix la posició inicial de l'actor.
     * 
     * @param x coordenada horizontal en pixels
     * @param y coordenada vertical en pixels
     */
    public void setPosicioInicial(int x, int y);

    /**
     * Obté la posicio inicial de l'actor.
     * 
     * @return un array de tamany 2 amb la posició x al primer element i la y
     * al segon
     */
    public int[] getPosicioInicial();
    
    /**
     * Estableix la posició de l'actor.
     * 
     * @param x coordenada horizontal en pixels
     * @param y coordenada vertical en pixels
     */
    public void setPosicio(int x, int y);

    /**
     * Obté la posicio actual de l'actor.
     * 
     * @return un array de tamany 2 amb la posició x al primer element i la y
     * al segon
     */
    public int[] getPosicio();
    
    /**
     * Actualitza les dades de l'actor segons l'estat actual del joc.
     * 
     * @param context el context del joc en el moment d'actualitzar
     */
    public void actualitzar(Context context);
    
    /**
     * Obté la posició i mida d'un actor en el moment actual
     * 
     * @return un rectangle amb la posició x,y i l'amplada i alçada
     */
    public Rectangle getLimits();

    /**
     * Gestiona la colició d'aquest actor amb un altre.
     * 
     * @param colisio les dades de la col·lisió.
     */
    public void tractarColisio(Colisio colisio);        
    
    /**
     * Obté el nivell de vida de l'actor.
     * 
     * @return un número entre 0 i 100, 0 eś mort.
     */
    public float getVida();
        
    /**
     * Estableix el nivell de vida.
     * 
     * @param nivell un número enter 0 i 100
     */
    public void setVida(float nivell);
    
    /**
     * Obté l'estat 
     * 
     * @return una de les constants <code>Constants.ACTIU</code>, 
     * <code>Constants.INACTIU</code>
     */
    public int getEstat();
    
    /**
     * Estableix l'estat.
     * 
     * @param estat
     */
    public void setEstat(int estat);
}
