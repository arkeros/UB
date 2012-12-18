
package edu.ub.juanadearco;

import java.awt.Graphics2D;

/**
 * Tots els objectes que es puguin dibuixar (fer el render) per pantalla han
 * d'implementar aquesta interfície.
 * 
 * @author danieldelrio@ub.edu
 */
public interface Renderable {
    
    public void render(Graphics2D g);
        
}
