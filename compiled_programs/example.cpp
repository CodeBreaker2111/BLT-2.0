#include <iostream>
#include <thread>
#include <chrono>
#include <string>

using namespace std;

int main() {
    int v0 = 2;
    int v1 = 1;
    string v2 = " Hello World!";
    cout << " Hello cute Chelsie!" << endl;
    this_thread::sleep_for(chrono::seconds(v0));
    cout << " Hello cute Rizo!" << endl;
    this_thread::sleep_for(chrono::seconds(v1));
    cout << v2 << endl;
    v2 = " Hello Big City!";
    cout << v2 << endl;
    cout << " Please type something" << endl;
    string v2 = "";
    cin << v2;
    cout << v3 << endl;
}