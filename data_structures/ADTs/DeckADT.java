public interface DeckADT {

    //  create a full set of cards (with 52 cards; no Jokers)
    void initialize();

    //  draw a card, and return the card as string. for example "2S" (2 of Spades)
    //  using single-letter representations for suits:
    //  S (spades), C (clubs), H (hearts) and D (diamonds)
    String drawRandomCard();

    String drawTopCardFromDeck();

    void pushCardOnBottomOfDeck(String str);
}
