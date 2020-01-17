import java.util.Random;
import java.util.ArrayList;

public class MyDeckOfCards implements DeckADT {
    private ArrayList<String> deck = new ArrayList<>();

    public void initialize() {
        for (int a = 1; a <= 13; a++) {
            deck.add("S" + a);
        }

        for (int b = 1; b <= 13; b++) {
            deck.add("C" + b);
        }

        for (int c = 1; c <= 13; c++) {
            deck.add("H" + c);
        }

        for (int d = 1; d <= 13; d++) {
            deck.add("D" + d);
        }
    }

    public String drawRandomCard() {
        Random rand = new Random();

        if (deck.size() == 0) {
            System.out.println("No cards in deck");
        }

        String card = this.deck.get(rand.nextInt(deck.size()));
        deck.remove(card);

        return card;
    }

    public String drawTopCardFromDeck() {
        if (deck.size() == 0) {
            System.out.println("No cards in deck");
        }

        String card = deck.get(0);
        deck.remove(card);

        return card;
    }

    public void pushCardOnBottomOfDeck(String str) {
        if (deck.contains(str.toUpperCase())) {
            System.out.println("Card already exists in the deck!");
        }
        else {
            deck.add(str);
        }
    }

    public String deckToString() {
        String str = "";

        for(int i = 0; i < this.deck.size(); i++) {
            str = str + this.deck.get(i) + "\n";
        }

        return str;
    }

    public static void main(String[] args) {
        System.out.println("Deck1 test");
        MyDeckOfCards myDeck = new MyDeckOfCards();
        myDeck.initialize();

        myDeck.deck.remove("S9");
        System.out.println(myDeck.deckToString());

        System.out.println(myDeck.drawRandomCard());
        System.out.println(myDeck.drawTopCardFromDeck());

        myDeck.pushCardOnBottomOfDeck("d2");
        myDeck.pushCardOnBottomOfDeck("S9");

        System.out.println(myDeck.deckToString());

        System.out.println("Deck2 test");
        MyDeckOfCards myDeck2 = new MyDeckOfCards();
        myDeck2.initialize();
        System.out.println(myDeck2.deckToString());

        System.out.println(myDeck2.drawRandomCard());
        System.out.println(myDeck2.drawTopCardFromDeck());
        myDeck2.pushCardOnBottomOfDeck("d2");
        myDeck2.deck.remove("H9");
        myDeck2.pushCardOnBottomOfDeck("H9");

        System.out.println(myDeck2.deckToString());
    }
}
