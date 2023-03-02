//John Kutbay
//BlackJack Lab
//COSC102
//5/27/22
//In this lab, I will create a program that simulates blackjack for the user.

#include <iostream>
#include <string>
#include <iomanip>
#include <cstdlib>
#include <ctime>

using namespace std;

//This is the declaration of my functions and the constant size of a deck.

const int numCard = 52;

string DealCard(int cards[numCard], int player);

int GetRandom(int min, int max);

void InitializeCards(int cards[numCard]);

int ScoreHand(int cards[numCard], int player);

int main() {

//I started by initializing my my cards and initializing variables.
	int cards[numCard];
	InitializeCards(cards);
	srand(time(NULL));
	string hitStand = "";
	const string cardValue[13] = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};
	const string cardSuit[4] = {"C", "D", "H", "S"};
	string dealersCards = "";
	string usersCards = "";

//This section is where I dealt the initial cards and scored the results.
	cout << "Dealer has cards: ";
	cout << setw(20) << left;
	DealCard(cards,1);
	DealCard(cards,1);
	for (int i = 0;i < numCard;i++) {
		if (cards[i] == 1) {
			dealersCards += cardValue[i % 13] + cardSuit[i / 13] + " ";
		}
	}
	cout << dealersCards;
	cout << "(" << ScoreHand(cards, 1) << ")" << '\n';

	cout << "You have cards  : ";
	cout << setw(20) << left;
	DealCard(cards, 2);
	DealCard(cards, 2);
	for (int i = 0;i < numCard;i++) {
		if (cards[i] == 2) {
			usersCards += cardValue[i % 13] + cardSuit[i / 13] + " ";
		}
	}
	cout << usersCards;
	cout << "(" << ScoreHand(cards, 2) << ")" << '\n';

	cout << "Hit or stand    ? ";
	cin >> hitStand;
	cout << '\n';
	
//This section is where I ran a series of if statements and loops to get input
//if the user wants to hit or stand.
	while (true) {
		if (hitStand == "hit") {
			cout << "Dealer has cards: ";
			cout << setw(20) << left;
			cout << dealersCards;
			cout << "(" << ScoreHand(cards, 1) << ")";
			cout << '\n';

			cout << "You have cards  : ";
			cout << setw(20) << left;
			usersCards += DealCard(cards, 2) + " ";
			cout << usersCards;
			cout << "(" << ScoreHand(cards, 2) << ")";
			cout << '\n';

			if (ScoreHand(cards, 2) > 21) {
				cout << "Player busts, dealer wins!\n";
				return -1;
			} else if (ScoreHand(cards, 2) == 21) {
				cout << "Player wins!\n";
				return -1;
			} else {
				cout << "Hit or stand    ? ";
				cin >> hitStand;
				cout << '\n';
			}		
		}else if (hitStand == "stand") {

//In this section, I used the restriction of scores for the dealer
//to determine if the dealer should hit or stand.

			if (ScoreHand(cards, 1) < 18) {
				cout << "Dealer hits     : ";
				cout << setw(20) << left;
				dealersCards += DealCard(cards, 1) + " ";
				cout << dealersCards;
				cout << "(" << ScoreHand(cards, 1) << ")";
				cout << '\n';

			} else if (ScoreHand(cards, 1) == 21) {
				cout << "Dealer wins!\n";
				return -1;
			} else if (ScoreHand(cards, 1) > 21) {
				cout << "Dealer busts, player wins!\n";
				return -1;
			} else if (ScoreHand(cards, 1) >= 18 || ScoreHand(cards, 1) < 21) {
				cout << "Dealer Stands  : ";
				cout << setw(20) << left;
				cout << dealersCards;
				cout << "(" << ScoreHand(cards, 1) << ")";
				cout << '\n' << '\n';
				break;
			}
		}
	}

//This is where I scored the results if neither dealer or player hit 21 or busted.
	if (ScoreHand(cards, 1) > ScoreHand(cards, 2)) {
		cout << "Dealer wins!\n";
	} else if (ScoreHand(cards, 2) > ScoreHand(cards, 1)) {
		cout << "Player wins!\n";
	} else if (ScoreHand(cards, 1) == ScoreHand(cards, 2)) {
		cout << "Player and dealer draw.\n";
	}
}

//This function deals a card to whoever is called.

string DealCard(int cards[numCard], int player) {

	int randomNumber;
	string card = "";
	const string cardValue[13] = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};
	const string cardSuit[4] = {"C", "D", "H", "S"};
	randomNumber = GetRandom(0, 51);
	while (cards[randomNumber] != 0) {
		randomNumber = GetRandom(0, 51);
	}
	cards[randomNumber] = player;
	card = cardValue[randomNumber % 13] + cardSuit[randomNumber / 13];
	return card;
}	

//This function returns a random number between the stated values.

int GetRandom(int min, int max) {
	
	return min + rand() % (max - min + 1);
}

//This function initializes an array with zeros.

void InitializeCards(int cards[numCard]) {
	for (int i = 0;i < numCard;i++) {
		cards[i] = 0;
	}
}

//This function scores a player's scores.

int ScoreHand(int cards[numCard], int player) {
	
	int scoreValue = 0;

	for (int i = 0; i < numCard; i++) {
		if (cards[i] == player) {
			if ((i % 13) < 10) {
				scoreValue += ((i % 13) + 1);
			} else if ((i % 13) >= 10) {
				scoreValue += 10;
			}
		}
	}
	return scoreValue;
}
