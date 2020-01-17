/*
C343 Summer 2019
Hw 06
Evan Truong
etruong
 */

package edu.indiana.cs.c343;
import java.util.ArrayList;
import java.util.LinkedList;

// ---------------------------------------------------------------------------
// C343 / Summer 2019
// ---------------------------------------------------------------------------
import java.util.List;

// ---------------------------------------------------------------------------
// GameLogic implements the "Flood Fill" logic behind each move in the game
// ---------------------------------------------------------------------------
public class GameLogic {

    private FloodFillGame theGame;

    // floodList is declared as a LinkedList here,
    // alas declared as public (bad practice!),
    // because it is used in the FloodFillGame class...
    // ... you may make it private
    //     and provide methods for accessing it instead:
    // (not compulsory, but would make the code "neater")

    // C343 Homework 06 TODO:
    //    you may have to work with the floodList in your floodFill() method:
    public List<Coordinates> floodList = new LinkedList<Coordinates>();

    // ---------------------------------------------------------------------------
    // constructor for the game logic
    // ---------------------------------------------------------------------------
    public GameLogic(FloodFillGame pGame) {
        theGame = pGame;

        // when the game begins,
        //   the tile at the left/top corner
        //   is the only one considered "filled"
        floodList.add(
                new Coordinates(0, 0)
        );
    } // end of GameLogic()



    // ---------------------------------------------------------------------------
    // C343 Homework 06 TODO:
    //    implement the floodFill() function!
    //
    // ---------------------------------------------------------------------------
    public void floodFill(int colorToFlood) {
        for (int c = 0; c < floodList.size(); c++) {
            if (onBoard(this.above(floodList.get(c)))
                    && (this.colorAtCoordinates(this.above(floodList.get(c))) == colorToFlood)
                    && !floodList.contains(this.above(floodList.get(c)))) {
                floodList.add(this.above(floodList.get(c)));
            }
            if (onBoard(this.below(floodList.get(c)))
                    && (this.colorAtCoordinates(this.below(floodList.get(c))) == colorToFlood
                    && !floodList.contains(this.below(floodList.get(c))))) {
                floodList.add(this.below(floodList.get(c)));
            }
            if (onBoard(this.toTheLeft(floodList.get(c)))
                    && (this.colorAtCoordinates(this.toTheLeft(floodList.get(c))) == colorToFlood)
                    && !floodList.contains(this.toTheLeft(floodList.get(c)))) {
                floodList.add(this.toTheLeft(floodList.get(c)));
            }
            if (onBoard(this.toTheRight(floodList.get(c)))
                    && (this.colorAtCoordinates(this.toTheRight(floodList.get(c))) == colorToFlood)
                    && !floodList.contains(this.toTheRight(floodList.get(c)))) {
                floodList.add(this.toTheRight(floodList.get(c)));
            }
        }
    }
    // ---------------------------------------------------------------------------

    // ---------------------------------------------------------------------------
    // onBoard() returns true, if coords specify a tile *on* the game board
    // ---------------------------------------------------------------------------
    public boolean onBoard(final Coordinates coords) {
        final int x = coords.x;
        final int y = coords.y;
        final int size = this.theGame.size;
        return x > -1 && x < size && y > -1 && y < size;
    } // end of onBoard()

    // ---------------------------------------------------------------------------
    // return Coordinates of the tile above the tile at coords
    // ---------------------------------------------------------------------------
    public Coordinates above(final Coordinates coords) {
        return new Coordinates(coords.x, coords.y-1);
    }

    // ---------------------------------------------------------------------------
    // return Coordinates of the tile below the tile at coords
    // ---------------------------------------------------------------------------
    public Coordinates below(final Coordinates coords) {
        // instantiate new Coordinates object:
        return new Coordinates(coords.x, coords.y+1);
    }

    // ---------------------------------------------------------------------------
    // return Coordinates of the tile to the left of the tile at coords
    // ---------------------------------------------------------------------------
    public Coordinates toTheLeft(final Coordinates coords) {
        // instantiate new Coordinates object:
        return new Coordinates(coords.x-1, coords.y);
    }

    // ---------------------------------------------------------------------------
    // return Coordinates of the tile to the toTheRight of the tile at coords
    // ---------------------------------------------------------------------------
    public Coordinates toTheRight(final Coordinates coords) {
        // instantiate new Coordinates object:
        return new Coordinates(coords.x + 1, coords.y);
    }

    // ---------------------------------------------------------------------------
    // get the color of the tile at coords
    // ---------------------------------------------------------------------------
    public int colorAtCoordinates(final Coordinates coords) {
        // ask theGame object, which color at coords:
        return this.theGame.getColor(coords);
    }

    public int autoLogic() {
        ArrayList<Integer> perimeter = new ArrayList<>();

        for(int i = 0; i < floodList.size(); i++) {
            if (onBoard(above(floodList.get(i)))
                    && (colorAtCoordinates(above(floodList.get(i))) != colorAtCoordinates(floodList.get(i)))
                    && !floodList.contains(above(floodList.get(i)))) {
                perimeter.add(colorAtCoordinates(above(floodList.get(i))));
            }
            if (onBoard(below(floodList.get(i)))
                    && (colorAtCoordinates(below(floodList.get(i))) != colorAtCoordinates(floodList.get(i)))
                    && !floodList.contains(below(floodList.get(i)))) {
                perimeter.add(colorAtCoordinates(below(floodList.get(i))));
            }
            if (onBoard(toTheRight(floodList.get(i)))
                    && (colorAtCoordinates(toTheRight(floodList.get(i))) != colorAtCoordinates(floodList.get(i)))
                    && !floodList.contains(toTheRight(floodList.get(i)))) {
                perimeter.add(colorAtCoordinates(toTheRight(floodList.get(i))));
            }
            if (onBoard(toTheLeft(floodList.get(i)))
                    && (colorAtCoordinates(toTheLeft(floodList.get(i))) != colorAtCoordinates(floodList.get(i)))
                    && !floodList.contains(toTheLeft(floodList.get(i)))) {
                perimeter.add(colorAtCoordinates(toTheLeft(floodList.get(i))));
            }
        }
        return this.getMostFreq(perimeter);
    }

    public int getMostFreq(ArrayList<Integer> arr) {
        int mostFreq = arr.get(0);
        int temp;
        int count = 1;
        int tempCount;

        for(int i = 0; i < arr.size() - 1; i++) {
            temp = arr.get(i);
            tempCount = 0;

            for(int j = 1; j < arr.size(); j++) {
                if(temp == arr.get(j)) {
                    tempCount++;
                }
            }

            if(tempCount > count) {
                mostFreq = temp;
                count = tempCount;
            }
        }
        return mostFreq;
    }
} // end of class GameLogic
// ---------------------------------------------------------------------------
