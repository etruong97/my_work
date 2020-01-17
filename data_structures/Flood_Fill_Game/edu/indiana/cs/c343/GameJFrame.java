package edu.indiana.cs.c343;

// ---------------------------------------------------------------------------
// C343 / Summer 2019
// ---------------------------------------------------------------------------

import java.awt.Color;
import java.awt.event.KeyEvent;
import java.awt.event.MouseEvent;
import java.awt.GridLayout;
import java.util.HashMap;
import java.util.Map;
import javax.swing.event.MouseInputAdapter;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;

// ---------------------------------------------------------------------------
// the class GameJFrame handles the main JFrame for this game
//   including "menu" items at top of the frame,
//   and a grid of button-tiles
// ---------------------------------------------------------------------------
public class GameJFrame extends JFrame {

    public final FloodFillGame theFloodFillGame;

    private JPanel theMainJPanel;
    private JMenu numberOfStepsMenuEntry = new JMenu();
    private Map<Coordinates, ButtonTile> mapFromCoordsToTile;

    // constructor for GameJFrame:
    public GameJFrame(final FloodFillGame pGame) {
        this.theFloodFillGame = pGame;
        this.theMainJPanel = new JPanel(
                // note: GridLayout is a Java AWT class,
                //   predating even Java Swing...
                new GridLayout(
                        this.theFloodFillGame.size, this.theFloodFillGame.size
                )
        );
        this.mapFromCoordsToTile = new HashMap<>();
        this.updateMenuEntryForNumberOfSteps();
        this.initMenuInsideFrame();
        this.initTiles();
        this.setContentPane(theMainJPanel);
        this.setSize(640, 640);
        this.setVisible(true);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public void updateMenuEntryForNumberOfSteps() {
        this.numberOfStepsMenuEntry.setText(
                Integer.toString (
                        this.theFloodFillGame.currentStep) +
                        "/" +
                        Integer.toString(this.theFloodFillGame.maxNumberOfSteps)
        );
    }

    public void setColor(final Coordinates pCoordinates, final int pColorIndex) {
        this.mapFromCoordsToTile.get(pCoordinates).setColor(pColorIndex);
    }

    private void initMenuInsideFrame() {
        JMenuBar lJavaMenuInAFrame;

        lJavaMenuInAFrame = new JMenuBar();

        final JMenu lGameMenu = new JMenu("(Click here for Game Menu)");
        lGameMenu.setMnemonic(KeyEvent.VK_G);
        lJavaMenuInAFrame.add(lGameMenu);

        final JMenuItem lRestartMenu = new JMenuItem("Restart");
        lRestartMenu.addActionListener(e -> this.theFloodFillGame.restart());
        lGameMenu.add(lRestartMenu);
        final JMenuItem lAutoplayMenu = new JMenuItem("Auto-Play");
        lAutoplayMenu.addActionListener(e -> this.theFloodFillGame.autoPlay());
        lGameMenu.add(lAutoplayMenu);
        final JMenuItem lQuitMenu = new JMenuItem("Quit Game");
        lRestartMenu.addActionListener(e -> this.dispose());
        lGameMenu.add(lQuitMenu);

        lJavaMenuInAFrame.add(numberOfStepsMenuEntry);

        this.setJMenuBar(lJavaMenuInAFrame);
    }

    private void initTiles() {
        final int[][] colorAtCoordinates = this.theFloodFillGame.colorAtCoordinates;
        for (int y=0; y<colorAtCoordinates.length; y+=1) {
            for (int x=0; x<colorAtCoordinates[y].length; x+=1) {
                final ButtonTile tile = new ButtonTile(colorAtCoordinates[y][x], this);
                this.theMainJPanel.add(tile);
                this.mapFromCoordsToTile.put(new Coordinates(x, y), tile);
            }
        }
    }
} // end of class GameJFrame
// ---------------------------------------------------------------------------



// ---------------------------------------------------------------------------
// the class ButtonTile is used to... draw tiles for the game!
//   however, tiles are actually implemented as Java "button" GUI elements
// ---------------------------------------------------------------------------
class ButtonTile extends JButton {
    public int theColorIndex;
    public GameJFrame theGameJFrame;

    public ButtonTile(final int pColorIndex,  final GameJFrame pGameJFrame) {
        this.theGameJFrame = pGameJFrame;
        this.setColor(pColorIndex);

        final TileMouseAdapter listener = new TileMouseAdapter(this);
        this.addMouseListener(listener);
        this.addMouseMotionListener(listener);

        // according to Java documentation for setOpaque():
        //   "If true the component paints every pixel within its bounds.
        //    Otherwise, the component may not paint some or all of its pixels,
        //    allowing the underlying pixels to show through."
        // huh?
        this.setOpaque(true);

    } // end of ButtonTile() constructor

    public void setColor(final int pColorIndex) {
        this.theColorIndex = pColorIndex;
        this.setBackground(ButtonTile.genColor(pColorIndex));
    }

    private static Color genColor(final int pColorIndex) {
        switch (pColorIndex) {
            case Constants.BLUE:
                return Color.BLUE;
            case Constants.RED:
                return Color.RED;
            case Constants.CYAN:
                return Color.CYAN;
            case Constants.PINK:
                return Color.PINK;
            case Constants.GREEN:
                return Color.GREEN;
            case Constants.YELLOW:
                return Color.YELLOW;
            default:
                return Color.YELLOW;
        }
    }
} // end of class ButtonTile
// ---------------------------------------------------------------------------




// ---------------------------------------------------------------------------
// the class TileMouseAdapter
//    implements Java Swing's abstract class MouseInputAdapter
// so that we can attach to *every tile object*
//    its own event handler for mouse clicks.
//
//  ... this is where the oneMove() function actually gets called,
//      when the user is playing the game.
// ---------------------------------------------------------------------------
class TileMouseAdapter extends MouseInputAdapter {
    private final ButtonTile tile;

    public TileMouseAdapter(final ButtonTile pTile) {
        // the constructor storing the tile to be monitored:
        this.tile = pTile;
    }

    // when the mouse is clicked on this tile,
    //   play the corresponding move in the game!
    public void mouseClicked(final MouseEvent e) {
        this.tile.theGameJFrame.theFloodFillGame.oneMove(this.tile.theColorIndex);
    }

} // end of class TileMouseAdapter
// ---------------------------------------------------------------------------
