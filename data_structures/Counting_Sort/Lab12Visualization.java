import java.util.Observer;
import java.util.Observable;

public class Lab12Visualization implements Observer {
    Lab12Model model;
    Lab12View view;

    public Lab12Visualization(Lab12Model m, Lab12View v) {
        this.model = m;
        this.view = v;
        this.model.addObserver(this);
    }

    public void update(Observable o, Object arg) {
        System.out.println("updating");

        for(int i = 0; i < this.model.getArray().length; i++) {
            view.drawLine(i, model.getArray()[i]);
        }
        view.clear();
    }

    public static void main(String[] args) {
        Lab12Model model = new Lab12Model(1000);
        Lab12View view = new Lab12View(600,800);
        Lab12Visualization controller = new Lab12Visualization(model, view);
        model.sort();
    }
}
