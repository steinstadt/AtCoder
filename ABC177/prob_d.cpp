// Problem D - Friends
#include <bits/stdc++.h>
#include <vector>
#include <algorithm>
using namespace std;

class UnionFind {

public:
     vector<int> par;

  // constructor
  UnionFind(int N) {
    for (int i=0; i < N; i++) {
      par.push_back(-1);
    }
  }

public:
  // root search
  int root(int x) {
    if (this->par[x] < 0) {
      return x;
    } else {
      this->par[x] = this->root(this->par[x]);
      return this->par[x];
    }
  }

  // if x and y are in same group
  bool same(int x, int y) {
    return this->root(x) == this->root(y);
  }

  // union process
  void unite(int x, int y) {
    x = this->root(x);
    y = this->root(y);

    if (x == y) {
      return;
    }

    if (this->par[x] <= this->par[y]) {
      this->par[x] += this->par[y];
      this->par[y] = x;
    } else {
      this->par[y] += this->par[x];
      this->par[x] = y;
    }
  }

  // max group member
  int max_member() {
    int tmp = 0;
    for (auto member_num : this->par) {
      tmp = max(tmp, (-1) * member_num);
    }
    return tmp;
  }

  // print member
  void print_member() {
    for (auto member : this->par) {
      cout << member << " ";
    }
    cout << endl;
  }
};



int main() {
  // input
  int N, M;
  cin >> N >> M;

  // initialization
  UnionFind *uf = new UnionFind(N);
  for (int i=0; i < M; i++) {
    int a, b;
    cin >> a >> b;
    uf->unite(a-1, b-1);
  }
  int ans = 0;

  // max calc
  ans = uf->max_member();

  // output
  cout << ans << endl;
}
