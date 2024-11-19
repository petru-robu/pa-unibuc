#include <bits/stdc++.h>
using namespace std;

//complexitate 0(logN)

string transform(int base, int x)
{
    string ans="";
    char m[16] = {'0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};

    while(x)
    {
        ans.insert(ans.begin(), m[x%base]);
        x /= base;
    }
    if(base == 16)
        return "0x" + ans;
    
    return ans;
}


int main()
{
    int x, cx, lgmax = -1;
    cin>>x;
    cx = x;

    while(x)
    {
        int lg = 0;
        while(x > 0 && (x & 1) == 1)
        {
            lg++;
            x = (x>>1);
        }

        lgmax = max(lgmax, lg);
        x = (x>>1);
    }

    cout<< transform(2, cx) << " are secv de lung. maxim " <<lgmax<<'\n';

    return 0;
}