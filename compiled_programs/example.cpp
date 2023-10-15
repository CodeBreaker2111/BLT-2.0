#include <iostream>
#include <thread>
#include <chrono>
#include <string>

using namespace std;

int main() {
    int v0 = 2;
    int v1 = 1;
    string v2 = " Hello World!";
    cout << " Hello cute Chelsea!" << endl;
    this_thread::sleep_for(chrono::seconds(v0));
    cout << " Hello cute Rizo!" << endl;
    this_thread::sleep_for(chrono::seconds(v1));
    cout << v2 << endl;
    v2 = " Hello Big City!";
    cout << v2 << endl;
    cout << " Please type something:" << endl;
    string v3 = "";
    cin >> v3;
    cout << v3 << endl;
    int v4 = 0;
    v4 = 50 + 50;
    cout << to_string(v4) << endl;
    v4 = 678 - 159;
    cout << to_string(v4) << endl;
    v4 = 50 * 50;
    cout << to_string(v4) << endl;
    v4 = 50 / 50;
    cout << to_string(v4) << endl;
    cout << " Please type something:" << endl;
    string v5 = "";
    cin >> v5;
    cout << " Please type something:" << endl;
    string v6 = "";
    cin >> v6;
    if ( v5 == v6 ) {
    cout << " You typed the same thing twice!" << endl;
    this_thread::sleep_for(chrono::seconds(1));
    cout << " I hope ;)" << endl;
    }
    if ( v5 != v6 ) {
    cout << " You did not typed the same thing twice!" << endl;
    this_thread::sleep_for(chrono::seconds(1));
    cout << " I hope ;)" << endl;
    }
    return 0;
}