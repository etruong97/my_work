/*
C343 Summer 2019
HW03
Evan Truong
etruong
 */

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Shape;
import javax.swing.JComponent;
import javax.swing.JFrame;
import java.util.Random;

public class HW03View extends JComponent{
    private int height;
    private int width;
    private JFrame frame;

    public HW03View(int h, int w) {
        this.height = h;
        this.width = w;
        this.frame = new JFrame();
        frame.setSize(h,w);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(this);
        frame.setVisible(true);
    }

    public void drawPoint(int x, int y, int value) {
        //System.out.println("Drawing point: (" + x + ", " + y + ")");
        Color col;
        if(value < 0) {
            col = new Color(value * -1, 0, 0);
        }
        else {
            col = new Color(0, value, 0);
        }

        Graphics g = this.getGraphics();
        g.setColor(col);
        g.drawOval(x,y,1, 1);
    }

    public void clear() {
        for(int i = 0; i < this.width; i++) {
            for(int j = 0; j < this.height ; j++) {
                Graphics g = this.getGraphics();
                Color blk = new Color(0, 0, 0);
                g.setColor(blk);
                g.drawOval(i,j,1,1);
            }
        }
    }
}
