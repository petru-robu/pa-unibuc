#include <bits/stdc++.h>
using namespace std;

//Complexitate O(n)

int main()
{
    vector<int> v = {7, 8, 1, 2, 2, 4, 7, 8, 8, 8, 1, 4, 3};
    int ans = 0;
    for(int i=0; i<v.size();i++)
        ans = (ans^v[i]);

    cout<<ans<<'\n';

    return 0;
}
