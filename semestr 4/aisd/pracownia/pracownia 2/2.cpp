#include <stdio.h>
#include <unordered_map>
#include <unordered_set>





std::unordered_map<unsigned long long, std::unordered_set<unsigned long long>> edges;
std::unordered_map<unsigned long long, unsigned int> roads;



unsigned int dfs(unsigned long long node) {
    if (roads[node]) return roads[node];

    unsigned int res = 0;
    for (auto& adj: edges[node]) res = (res + dfs(adj)) % 999979;

    roads[node] = res;
    return res;
}



int main() {
    unsigned int t; 
    unsigned long long m, n, a1, a2, b1, b2;

    scanf("%llu %llu %u", &m, &n, &t);

    for (unsigned int i = 0; i < t; i++) {
        scanf("%llu %llu %llu %llu", &a1, &b1, &a2, &b2);
        edges[(a1 << 32) | b1].insert((a2 << 32) | b2);
    }
    roads[(m << 32) | n] = 1;

    printf("%u\n", dfs(0));
    return 0;
}