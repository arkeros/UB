
package edu.ub.juanadearco.actors;

import edu.ub.juanadearco.Actor;
import edu.ub.juanadearco.Constants;
import edu.ub.juanadearco.Context;
import edu.ub.juanadearco.Habitacio;
import edu.ub.juanadearco.Porta;

import java.awt.Canvas;
import java.awt.Rectangle;

/**
 * Classe base per tota la resta d'actors. Subclasses poden extendre aquesta
 * classe i beneficiar-se d'aquesta implementació bàsica.
 * 
 * @author danieldelrio@ub.edu
 */
public abstract class AbstractActor implements Actor {

    protected int x0;
    protected int y0;
    
    protected float vida = 100.0f;
    protected int x;
    protected int y;
    protected int estat;
    protected Canvas observer = new Canvas();
    
    public void inicialitzar() {
        this.x = x0;
        this.y = y0;
        this.vida = 100;
        this.estat = Constants.ESTAT_ACTIU;
    }
    
    public void setPosicioInicial(int x, int y) {
        this.x0 = x;
        this.y0 = y;
    }
    
    public int[] getPosicioInicial() {
        return new int[] { x0, y0 };
    }
    
    public void setVida(float vida) {
        this.vida = Math.max(0, Math.min(100, vida));
    }
    
    public float getVida() {
        return vida;
    }
    
    public boolean isMort() {
        return vida <= 0;
    }
    
    public int getEstat() {
        return estat;
    }
    
    public void setEstat(int estat) {
        this.estat = estat;
    }
        
    public void setPosicio(int x, int y) {
        this.x = x;
        this.y = y;        
    }
    
    public int[] getPosicio() {
        return new int[] { x, y };
    }
    
    public int getX() {
        return x;
    }
    
    public int getY() {
        return y;
    }
    
    /**
     * Retorna si l'actor en la posició propocionada col·lisionaria amb un mur
     * de l'habitació actual.
     * 
     * @param ctx
     * @param x la posició x de l'actor
     * @param y la posició y de l'actor
     * @return true si en la posició l'actor col·lisiona amb el mur.
     */
    public boolean testMur(Context ctx, int x, int y) {
        return testMur(ctx, x, y, getLimits());
    }
    
    /**
     * Retorna si el rectangle proporcionat intersecta amb un mur
     * de l'habitació actual.
     * 
     * @param ctx
     * @param x la posició x de l'actor
     * @param y la posició y de l'actor
     * @param limits el rectangle
     * @return true si el rectangle intersecta amb un mur.
     */
    public boolean testMur(Context ctx, int x, int y, Rectangle limits) {
        Habitacio habitacio = ctx.getJoc().getCastell().getHabitacio();
        int w = (int)limits.getWidth();
        int h = (int)limits.getHeight();        

        Rectangle r = new Rectangle(x, y, w, h);        
        int[][] celes = habitacio.getCelesIntersectades(r);
        
        for (int i = 0; i < celes.length; i++) {
            char c = habitacio.getValor(celes[i][0], celes[i][1]);
            if (c == Constants.SIMBOL_MUR) {
                return true;
            }
        }
        return false;        
    }
    
    /**
     * Obté la porta que hi col·lisionaria amb l'actor en un punt determinat de
     * l'espai.
     * 
     * @param ctx
     * @param x la posició x 
     * @param y la posició y
     * @return la porta o null si no hi ha cap
     */
    public Porta testPorta(Context ctx, int x, int y) {
        Porta p = null;
        Habitacio habitacio = ctx.getJoc().getCastell().getHabitacio();
        Rectangle limits = getLimits();
        int w = (int)limits.getWidth();
        int h = (int)limits.getHeight();        

        Rectangle r = new Rectangle(x, y, w, h);        
        int[][] celes = habitacio.getCelesIntersectades(r);
        
        int i = 0;
        while (p == null && i < celes.length) {
            p = habitacio.getPorta(celes[i][0], celes[i][1]);
            i++;
        }                
        return p;        
    }
                
}
