#include <cstdio>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;
int n, c, x;
map<int, int> mp;
map<int, int> m;
vector<pair<int, int> > p;
bool cmp(pair<int, int> a, pair<int, int> b) {
    if (a.first == b.first) {
        return m[a.second] < m[b.second];
    }
    return a.first > b.first;
}
int main() {
    scanf("%d%d", &n, &c);
    for (int i = 0; i < n; i++) {
        scanf("%d", &x);
        mp[x]++;
        if (!m[x])
            m[x] = i + 1;
    }
    for (auto i : mp) 
        p.emplace_back(i.second, i.first);
    sort(p.begin(), p.end(), cmp);
    for (auto i : p) {
        for (int j = 0; j < i.first; j++)
            printf("%d ", i.second);
    }
    return 0;
}


