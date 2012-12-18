
package edu.ub.juanadearco;

/**
 * Les dades d'una col·lisió.
 * 
 * @author danieldelrio@ub.edu
 */
public class Colisio {
    
    private  Actor actor;

    /**
     * Nova col·lisió.
     * 
     * @param actor l'actor amb qui és col·lisiona.
     */
    public Colisio(Actor actor) {
        this.actor = actor;
    }
    
    /**
     * L'actor amb qui és col·lisiona.
     * 
     * @return l'actor
     */
    public Actor getActor() {
        return actor;
    }

        
}
