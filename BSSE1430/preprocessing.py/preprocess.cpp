#include<bits/stdc++.h>
using namespace std;

string padding(string s)
{
    stringstream ss;
    for(int i=0; i<s.size(); i++)
    ss<<bitset<8>(s[i]);
    string padded = ss.str();
    int len = padded.size();
    int add;
    int mod = padded.length()%1024;

    if((1024-mod)>=128)
    add = 1024-mod;
    else if((1024-mod)<128)
    add = 2048 - mod;

    padded+="1";
    for(int i=0; i<add-129; i++)
    padded+="0";

    string L = std::bitset<128>(len).to_string();
    padded+=L;

    return padded;
}

void getHash(string message)
{
    string padded = padding(message);
    cout<<padded<<endl;
    cout<<"Lenth of padded: "<<padded.length();
}

int main()
{
    string message;
    getline(cin, message);
    cout<<"Length: "<<message.length()<<endl;
    cout<<"Binary Length: "<<message.length()*8<<endl;
    
    getHash(message);
    return 0;
}