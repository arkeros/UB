
package edu.ub.juanadearco.actors;

import edu.ub.juanadearco.Actor;
import edu.ub.juanadearco.Colisio;
import edu.ub.juanadearco.Constants;
import edu.ub.juanadearco.Context;
import edu.ub.juanadearco.Util;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.Rectangle;
import java.util.HashSet;
import java.util.Set;

/**
 * Aquest es l'antagonista del joc.
 * 
 * 
 * @author rafa.arquero@gmail.com
 */
public class Bryan extends AbstractActor {  
    public static final String NOM  = "Bryan";  
    public static final int AMPLADA = 25;
    public static final int ALCADA  = 50;    
    
    private Image image;  
    
    /**
     * Si Juana es topa amb ell, poden ocorrer 2 coses: la mort de Juana o be la mort de Bryan si Juana te l'escut i el fi del joc.
     * 
     */
    public Bryan() {
        this.image = Util.carregarImatge("bryan.png", 0, 0, AMPLADA, ALCADA);
        setEstat(Constants.ESTAT_ACTIU);
    }

    public void actualitzar(Context context) {
        // no fem res, es estàtic
    }

    public Rectangle getLimits() {
        return new Rectangle(getX(), getY(), AMPLADA, ALCADA);
    }

    public void tractarColisio(Colisio colisio) {
        Actor actor = colisio.getActor();
        if (actor instanceof Heroina) {
            Heroina heroina = (Heroina)actor;    
            
            heroina.BryanTrobat();   
            if(!heroina.haTrobatEscut())
                heroina.setVida(0);
        }
    }

    public void render(Graphics2D g) {
        g.drawImage(image, getX(), getY(), observer);
        g.setColor(Color.CYAN);
        Font f = new Font("Dialog", Font.BOLD, 10);
        g.setFont(f);
        g.drawString(NOM, getX(), getY() - 3);
    }           
}