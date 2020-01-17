/*
C343 Summer 2019
HW04
Evan Truong
etruong
 */

import java.util.Observer;
import java.util.Observable;

public class HW04Controller implements Observer {
    private HW04Model model;
    private HW04View view;
    private int counter;

    public HW04Controller(HW04Model m, HW04View v) {
        this.model = m;
        this.view = v;
        this.counter = 0;
        model.addObserver(this);
    }

    public void update(Observable o, Object arg) {
        String aString = model.aString();
        String bString = model.bString();
        String vowels = "aeiou";

        if(counter == 0) {
            for(int i = 1; i <= aString.length(); i++) {
                char letter = aString.toLowerCase().charAt(i-1);
                if(letter == ' ') {
                    view.drawPoint(i,0,0,0,0);
                }
                else if(vowels.indexOf(letter) < 0) {
                    view.drawPoint(i,0,255,255,51);
                }
                else {
                    view.drawPoint(i,0,255, 128,0);
                }
            }

            for(int j = 1; j <= bString.length(); j++) {
                char letter = bString.toLowerCase().charAt(j-1);
                if(letter == ' ') {
                    view.drawPoint(0,j,0,0,0);
                }
                else if(vowels.indexOf(letter) < 0) {
                    view.drawPoint(0,j,255,255,51);
                }
                else {
                    view.drawPoint(0,j,255, 128,0);
                }
            }
        }

        char[] erow = model.eLine(counter);
        for(int b = 0; b < erow.length; b++) {
            if(erow[b] == ' ') {
                view.drawPoint(counter+1,b+1, 0,255,0);
            }
            else if(erow[b] == 'S') {
                view.drawPoint(counter+1,b+1,255,0,255);
            }
            else if(erow[b] == 'D') {
                view.drawPoint(counter+1, b+1, 255,0,0);
            }
            else {
                view.drawPoint(counter+1,b+1,0,0,255);
            }
        }

        int[] drow = model.dLine(counter);
        int index = 1;
        int min = drow[1];
        for(int a = 1; a < drow.length; a++) {
            if(drow[a] < min) {
                min = drow[a];
                index = a;
            }
        }
        view.drawPoint(index+1, counter+1, 255,255,255);
        counter++;
    }

    public static void main(String[] args) {
        HW04Model model = new HW04Model();
        HW04View view = new HW04View(1280,1024);
        HW04Controller controller = new HW04Controller(model,view);
        model.dist(model.aString(), model.bString());
        view.clear();
    }
}
