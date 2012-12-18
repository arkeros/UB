package edu.ub.juanadearco.actors;

import edu.ub.juanadearco.*;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.Rectangle;

/**
 * Representa el nostre heroina. L'heroina manté una llista amb les gemmes trobades
 * 
 * @author danieldelrio@ub.edu
 */
public class Heroina extends AbstractActor {   
    private Image[] imatges;
    
    public static final int AMPLADA = 25;
    public static final int ALCADA = 50;
    
    private static final int FRAMES_CHANGE = 1;
                
    private boolean bPosChanged = false;
    private int nFramesToChange = FRAMES_CHANGE;
    int lastImage = 0;
    private int deltaX = 10;
    private int deltaY = 8;
    private int direccio = -1;
    
    private static final float DANY_PER_SEGON = 1.0f;
            
    private boolean BryanTrobat;
    private boolean EscutTrobat;
    
    /**
     * Constructor.
     */
    public Heroina() {
        init();
    }
    
    public void inicialitzar() {
        super.inicialitzar();
        init();
    }
    
    /**
     * Obté un rectangle ambs el límits de l'heroina.
     * 
     * @return els límits, x,y, amplada i alçada
     */
    public Rectangle getLimits() {
        return new Rectangle(x, y, AMPLADA, ALCADA);
    }
    
    public void actualitzar(Context ctx) {
        calcularNivellVida(ctx);
        int desX = 0; 
        int desY = 0;
        bPosChanged = false;
                
        if (ctx.isKeyPressed(Context.KEY_DOWN)) {
            desY = 1;
            direccio = Constants.DIRECCIO_SUD;
            bPosChanged = true;
        } else if (ctx.isKeyPressed(Context.KEY_UP)) { 
            desY = -1;
            direccio = Constants.DIRECCIO_NORD;
            bPosChanged = true;
        } else if (ctx.isKeyPressed(Context.KEY_LEFT)) {
            desX = -1;
            direccio = Constants.DIRECCIO_OEST;
            bPosChanged = true;
        } else if (ctx.isKeyPressed(Context.KEY_RIGHT)) {
            desX = 1;
            direccio = Constants.DIRECCIO_EST;
            bPosChanged = true;
        }
        
        int auxX = x + (int)(deltaX * desX);
        int auxY = y + (int)(deltaY * desY);        
                
        Porta porta = testPorta(ctx, auxX, auxY);
        if (porta != null && porta.getNumPlantaDesti() != -1 && 
                porta.getNumHabitacioDesti() != -1) {
            
            Castell castell = ctx.getJoc().getCastell();            
            castell.setPlanta(porta.getNumPlantaDesti());
            castell.setNumHabitacio(porta.getNumHabitacioDesti());
            int[] posicio = porta.getPosicioHabitacioDesti();
            if (posicio != null) {
                x = posicio[0];
                y = posicio[1];
            }
        } else if (!testMur(ctx, auxX, auxY)) {
            x = auxX;
            y = auxY;
        }
    }
    
    public void tractarColisio(Colisio colisio) {

    }
    
    public void EscutTrobat() {
        this.EscutTrobat = true;
    }
    
    public boolean haTrobatEscut() {
        return this.EscutTrobat;
    }
    
    public void BryanTrobat() {
        this.BryanTrobat = true;
    }
    
    public boolean haTrobatBryan() {
        return this.BryanTrobat;
    }

    public void render(Graphics2D g) {
        int nImg = 0;
        if (bPosChanged) {
        	nFramesToChange--;
        	if (nFramesToChange == 0) {
        		nFramesToChange = FRAMES_CHANGE;
        		lastImage = (lastImage == 1) ? 0 : 1;
        	}
        }
        
        if (direccio == Constants.DIRECCIO_NORD) {
        	nImg = 2 + lastImage;
        } else {
        	nImg = lastImage;
        }
        Image image = imatges[nImg];
        g.drawImage(image, x, y, observer);
    }

    // private methods *********************************************************
    
    private void init() {
        this.BryanTrobat = false;
        this.EscutTrobat = false;
        imatges = new Image[4];
        for (int i=0; i<imatges.length; i++)
        	imatges[i] = Util.carregarImatge("heroina.png", AMPLADA*i, 0, AMPLADA, ALCADA);
    }
    
    private void calcularNivellVida(Context ctx) {
        long t = ctx.getTempsFrame();
        float dany = DANY_PER_SEGON * t / 1000.f;
        setVida(Math.max(0, getVida() - dany));
    }
    
}
