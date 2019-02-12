#include <stdlib.h>
#include <string>
#include <iostream>
#include <bitset>
#include <bits/basic_string.h>

using namespace std;

void conversion(string number, string modo);
void bitToDec(string s);
void bitToHex(string s);
void decToBit(string s);
void decToHex(string s);
void hexToDec(string s);
void hexToBit(string s);

int main() {
    int casos; 
    cin >> casos;
    for(int i = 0; i < casos; i++) {
        string number, modo;
        cin >> number;
        cin >> modo;
        cout << "Case: " << i << endl;
        conversion(number, modo);
        cout << endl;
    }
}

void conversion(string number, string modo) {
    if(modo.compare("bin") == 0) {
        bitToDec(number);
        bitToHex(number);
    }
    else if(modo.compare("dec") == 0) {
        //decToHex(number);
        decToBit(number);
    }else if(modo.compare("hex") == 0) {
        //hexToDec(number);
        hexToBit(number);
    }else cout << "erro" << endl;
}

void bitToDec(string s) {
    cout << bitset<12>(s).to_ulong() << " dec" << endl;
}

void bitToHex(string s) {
    if(s.compare("000") == 0) {
        cout << "0";
    }
    else if(s.compare("001") == 0) {
        cout << "1";
    }
    else if(s.compare("010") == 0) {
        cout << "2";
    }
    else if(s.compare("011") == 0) {
        cout << "3";
    }
    else if(s.compare("100") == 0) {
        cout << "4";
    }
    else if(s.compare("101") == 0) {
        cout << "5";
    }
    else if(s.compare("110") == 0) {
        cout << "6";
    }
    else if(s.compare("111") == 0) {
        cout << "7";
    }else cout << "8";
    cout << " hex" << endl;
}

void decToBit(string s) {
    cout << bitset<12>(stoi(s)).to_string() << " bin" << endl;
}

void hexToBit(string s) {
    for(int i = 0; i < s.length(); i++) {
        switch(s.at(i)) {
            case '0':
                cout << "0000";
                break;
            case '1':
                cout << "0001";
                break;
            case '2':
                cout << "0010";
                break;
            case '3':
                cout << "0011";
                break;
            case '4':
                cout << "0100";
                break;
            case '5':
                cout << "0101";
                break;
            case '6':
                cout << "0110";
                break;
            case '7':
                cout << "0111";
                break;
            case '8':
                cout << "1000";
                break;
            case '9':
                cout << "1001";
                break;
            case 'a':
                cout << "1010";
                break;
            case 'b':
                cout << "1011";
                break;
            case 'c':
                cout << "1100";
                break;
            case 'd':
                cout << "1101";
                break;
            case 'e':
                cout << "1110";
                break;
            case 'f':
                cout << "1111";
                break;
        }
    }
    cout << " bin" << endl;
}