
package edu.ub.juanadearco;


/**
 * Manté les dades del joc. el castell i l'heroina.
 * 
 * @author danieldelrio@ub.edu
 */
public class Joc {

    private Castell castell;
    private Actor heroina;

    
    /**
     * Constructor.
     */    
    public Joc() {        
    }
    
    public Joc(Castell castell, Actor heroina) {
        this.castell = castell;
        this.heroina = heroina;
    }
    
    public void iniciar() {
        castell.setPlanta(0);
        castell.setNumHabitacio(0);
                
        // inicialitzar actors
        heroina.inicialitzar();
        for (int i = 0; i < castell.getNumPlantes(); i++) {
            Habitacio[] arr = castell.getHabitacions(i);
            if (arr != null) {
                for (Habitacio h : arr) {
                    if (h != null) {
                        for (Actor actor : h.getActors()) {
                            actor.inicialitzar();
                        }
                    }
                }
            }
        }        
    }
            
    /**
     * Estableix el castell.
     * 
     * @param castell el castell
     */
    public void setCastell(Castell castell) {
        this.castell = castell;
    }
    
    public Castell getCastell() {
        return castell;
    }
    
    /**
     * Estableix l'heroina.
     * 
     * @param heroina
     */
    public void setHeroina(Actor heroina) {
        this.heroina = heroina;
    }
    
    public Actor getHeroina() {
        return heroina;
    }
                    
    
}
