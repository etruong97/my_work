import java.awt.*;
import javax.swing.JComponent;
import javax.swing.JFrame;

public class Lab12View extends JComponent {
    private JFrame frame;
    private int height;
    private int width;

    public Lab12View(int h, int w) {
        this.frame = new JFrame();
        this.height = h;
        this.width = w;
        frame.add(this);
        frame.setSize(w, h);
        frame.setBackground(Color.green);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }

    public void drawLine(int x, int value) {
        Color col = Color.BLACK;
        Graphics g = this.getGraphics();
        g.setColor(col);
        g.fillRect(x,0, 2, value);
    }

    public void clear() {
        Graphics g = this.getGraphics();
        Color col = Color.green;
        g.setColor(col);
        g.fillRect(0,0, this.width, this.height);
    }
}
