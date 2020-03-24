#include <bits/stdc++.h>
#include <math.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
const ll mod = 1000000007;
const int INF = 1001001001;
const ll LINF = 1001001001001001001;

int main(){
    ll h , w, k ; cin >> h >> w >> k;
    vector<string> chc(h);
    rep(i,h) cin >> chc.at(i);

    ll ans = INF;

    for(int i=0;i<(1<<(h-1));i++){
        bitset<12> s(i);
        ll a = s.count();
        vector<ll> x(a+1,0);
        vector<ll> xreset(a+1,0);

        ll hakoidx = 0;
        bool flag = 0;

        ll anskouho = a;
        bool bitflag = 0;

        for(int yk = 0 ;yk < w ;yk++){
            for(int tt = 0;tt<h;tt++){
                if(chc.at(tt).at(yk)=='1') x.at(hakoidx)++;

                if(x.at(hakoidx)>k){
                    flag = 1;
                    break;
                }

                if(s[tt]) hakoidx++;
            }

            hakoidx = 0;

            if(flag){
                anskouho++;
                x = xreset;

                for(int tt = 0;tt<h;tt++){
                    if(chc.at(tt).at(yk)=='1')x.at(hakoidx)++;

                    if(x.at(hakoidx)>k){
                        bitflag = 1;
                        break;
                    }

                    if(s[tt]) hakoidx++;
                }

            }

            //cout << yk << " " << anskouho << endl;

            flag = 0;
            if(bitflag) break;
            hakoidx = 0;

        }
        if(bitflag) continue;
        ans = min(ans,anskouho);
        //cout << ans << endl;

    }
    cout << ans << endl;
}
