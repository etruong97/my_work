/*
C343 / Summer 2019
HW 02
Evan Truong
etruong
 */

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Shape;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.Timer;
import java.util.Random;

public class HW02starterCode extends JComponent implements ActionListener {

    static final int H_SIZE = 1000;
    static final int V_SIZE = 1200;

    // TODO: draw the content of this 2D array of integers,
    //       where each integer value in the array should be represented thus:
    //       from MIN_VALUE to 0 (included) - black color
    //       from 1 to 254 - gray color at given intensity
    //       from 255 to MAX_VALUE - white color
    Int2DArray pixels = new Int2DArray(V_SIZE, H_SIZE);

    javax.swing.Timer timer;

    // we have to implement actionPerformed() since we implement the ActionListener interface:
    public void actionPerformed(ActionEvent e) {
        System.out.println("here be actionPerformed() for HW02starterCode");

        // ...do whatever you need to do at repeated intervals...
        Random rand = new Random();

        for(int i = 0; i < V_SIZE; i++) {
            for(int j = 0; j < H_SIZE; j++) {
                int n = rand.nextInt(255);
                this.pixels.set(i, j, n);
            }
        }

        this.repaint();
    }

    public void paintComponent(Graphics pGraphics) {
        System.out.println("here be paintComponent() for HW02starterCode");

        super.paintComponent(pGraphics);

        // clear background at every re-painting:
        pGraphics.setColor(Color.PINK);
        Shape lClipArea = pGraphics.getClip();
        int lWidth = lClipArea.getBounds().width;
        int lHeight = lClipArea.getBounds().height;
        pGraphics.fillRect(0,0,lWidth,lHeight);

        Color lForegroundColor = new Color(0,0,0);
        pGraphics.setColor(lForegroundColor);

        for(int i = 0; i < V_SIZE; i++) {
            for(int j = 0; j < H_SIZE; j++) {
                int pixelInt = this.pixels.get(i,j);
                Color pixelCol = new Color(pixelInt,pixelInt,pixelInt);
                pGraphics.setColor(pixelCol);
                pGraphics.drawOval(j,i,2,2);
            }
        }
    }


    // client code - main() method:
    public static void main(String[] args) {

        // instantiate the main JComponent, i.e. "this" Java class:
        HW02starterCode theMainJComponent = new HW02starterCode();

        // create JFrame where we (the main object in its JComponent identity) can paint:
        JFrame aJFrame = new JFrame();
        aJFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        aJFrame.add(theMainJComponent);
        aJFrame.setSize(H_SIZE, V_SIZE);
        aJFrame.setVisible(true);

        theMainJComponent.timer = new Timer(100, theMainJComponent);
        theMainJComponent.timer.start();
    }
}