/*
C343 Summer 2019
HW03
Evan Truong
etruong
 */

import java.util.Observer;
import java.util.Observable;

public class HW03Controller implements Observer {
    private HW03Model model;
    private HW03View view;

    public HW03Controller(HW03Model m, HW03View v) {
        this.model = m;
        this.view = v;
        this.model.addObserver(this);
    }

    public void update(Observable o, Object arg) {
        System.out.println("updating");
        for(int i = 0; i < model.getHeight(); i++) {
            for(int j = 0; j < model.getWidth(); j++) {
                view.drawPoint(i, j, model.getArray().get(i,j));
            }
        }
    }

    public static void main(String[] args) {
        HW03Model model = new HW03Model(1700,1000);
        HW03View view = new HW03View(1700, 1000);
        HW03Controller controller = new HW03Controller(model,view);
        while(true) {
            model.randomize();
            model.sortArray1();
            model.randomize();
            model.sortArray2();
        }
//        model.randomize();
//        model.sortArray1();
//        model.randomize();
//        model.sortArray2();
//        view.clear();
    }
}
