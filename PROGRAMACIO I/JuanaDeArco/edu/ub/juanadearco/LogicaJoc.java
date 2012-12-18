
package edu.ub.juanadearco;

/**
 * Gestiona la lògica del joc definint uns estats i les regles per passar
 * d'un estat a un altre.
 * 
 * @author danieldelrio@ub.edu
 */
public class LogicaJoc {

    public static enum EstatJoc {        MENU,    
        INICIANT,   // el joc s'està iniciant
        JUGANT,     
        PAUSAT,     
        GAMEOVER,   
        EXIT        // sortida del programa
    }
   
    private Joc joc;
    private EstatJoc estat;
    
    
    public LogicaJoc(Joc joc) {
        this.joc = joc;
        estat = EstatJoc.MENU;
    }
        
    public void setEstat(EstatJoc estat) {
        this.estat = estat;
    }
    
    public EstatJoc getEstat() {
        return estat;
    }

    public void iniciar() {
        if (this.estat == EstatJoc.MENU) {
            this.estat = EstatJoc.INICIANT;
            joc.iniciar();
            this.estat = EstatJoc.JUGANT;
        }
    }
    
    public void continuar() {
        this.estat = EstatJoc.JUGANT;
    }
     
    public void pausar() {
        if (estat == EstatJoc.JUGANT)
            estat = EstatJoc.PAUSAT;
        else if (estat == EstatJoc.PAUSAT)
            estat = EstatJoc.JUGANT;
    }
    
    public void exit() {
        if (estat == EstatJoc.MENU)
            this.estat = EstatJoc.EXIT;
        else
            estat = EstatJoc.MENU;            
    }
}
