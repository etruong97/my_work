/*
C343 Summer 2019
HW04
Evan Truong
etruong
*/

import javax.swing.JComponent;
import javax.swing.JFrame;
import java.awt.Color;
import java.awt.Graphics;

public class HW04View extends JComponent {
    private int height;
    private int width;
    private JFrame frame;

    public HW04View(int h, int w) {
        this.height = h;
        this.width = w;
        this.frame = new JFrame();
        frame.setSize(h,w);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(this);
        frame.setVisible(true);
    }

    public void drawPoint(int x, int y, int r, int g, int b) {
        if(r > 250) {r = 250;}
        if(g > 250) {g = 250;}
        if(b > 250) {b = 250;}
        if(r < 0) {r = 0;}
        if(g < 0) {g = 0;}
        if(b < 0) {b = 0;}

        Graphics graph = this.getGraphics();
        Color col = new Color(r,g,b);
        graph.setColor(col);
        graph.drawOval(x,y,1, 1);
    }

    public void clear() {
        Graphics g = this.getGraphics();
        Color col = Color.white;
        g.setColor(col);
        g.fillRect(0,0, this.height, this.width);
    }
}
