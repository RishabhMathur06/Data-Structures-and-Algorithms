'''
    Name: Rishabh Mathur
    Date: 14 Apr, 2024
'''

#include<bits/stdc++.h>
using namespace std;


class Solution{
    public:
    unsigned long long int countSub(int arr[], int n)
    {
        long long ans = 0;
        std::vector<long long> dp(n, 1);
        
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (arr[i] > arr[j]) {
                    dp[i] += dp[j];
                }
            }
            ans += dp[i];
        }
        
        return ans;

    }
};

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int a[n+1];
        for(unsigned long long int i=0;i<n;i++)
            cin>>a[i];
        Solution ob;
        cout<<ob.countSub(a,n)<<endl;
    }
}
