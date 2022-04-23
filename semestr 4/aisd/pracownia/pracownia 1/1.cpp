#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <vector>





class disjoined_set {
    private:
        unsigned int count;
        unsigned int sets;
        std::vector<unsigned int> parent;
        //std::vector<unsigned int> rank;



    public:
        //disjoined_set(int n) {
        //    count = n;
        //    for (int i = 0; i < n; i++) {
        //        parent.push_back(i);
	    //        rank.push_back(1);
	    //    }
        //}

        disjoined_set() : count(0), sets(0) {};


        void add_node() {
            parent.push_back(count++);
            sets++;
            //rank.push_back(1);
        }


        unsigned int find(unsigned int x) {
            //int root = x;
            //while (root != parent[root]) root = parent[root];
            //return root;

            if (parent[x] == x) return x;

            unsigned int result = find(parent[x]);
            parent[x] = result;
            return result;
        }


        void union_sets(unsigned int x, unsigned int y) {
            int x_s = find(x);
            int y_s = find(y);

            if (x_s == y_s) return;

            sets--;
            parent[x_s] = y_s;

            //if (rank[x_s] < rank[y_s]) { 
		    //    parent[x_s] = y_s; 
		    //    rank[y_s] += rank[x_s]; 
	        //} else { 
		    //    parent[y_s] = x_s; 
		    //    rank[x_s] += rank[y_s]; 
	        //}
        }


        unsigned int count_sets() {return sets;}
};





bool horizontal(char a, char b) {
    return a >= 'D' && a <= 'F' && (b == 'B' || b == 'C' || b == 'F');
}

bool vertical(char a, char b) {
    return (a == 'B' || a == 'E' || a == 'F') && (b == 'C' || b == 'D' || b == 'F');
}



int main() {
    unsigned short n, m;
    unsigned int label = 0;
    char previous[2001], current[2001];
    unsigned int prev_label[2001], curr_label[2001];
    disjoined_set S;
    bool v, h;

    scanf("%hu %hu", &n, &m);
    while ((getchar()) != '\n');


    fgets(previous, m + 2, stdin);

    if (previous[0] > 'A') {
        prev_label[0] = label++;
        S.add_node();
    }

    for (unsigned short j = 1; j < m; j++) {
        if (previous[j] > 'A') {
            if (horizontal(previous[j - 1], previous[j])) prev_label[j] = prev_label[j - 1];
            else {
                prev_label[j] = label++;
                S.add_node();
            }
        }
    }


    for (unsigned short i = 1; i < n; i++) {
        fgets(current, m + 2, stdin);

        if (current[0] > 'A')
        {
            if (vertical(previous[0], current[0])) curr_label[0] = prev_label[0];
            else {
                curr_label[0] = label++;
                S.add_node();
            }
        }
        previous[0] = current[0];
        prev_label[0] = curr_label[0];

        for (unsigned short j = 1; j < m; j++) {
            if (current[j] > 'A') {
                v = vertical(previous[j], current[j]);
                h = horizontal(current[j - 1], current[j]);
                if (v && h && (prev_label[j] != curr_label[j - 1])) {
                    curr_label[j] = std::min(prev_label[j], curr_label[j - 1]);
                    S.union_sets(prev_label[j], curr_label[j - 1]);
                }
                else if (v) curr_label[j] = prev_label[j];
                else if (h) curr_label[j] = curr_label[j - 1];
                else {
                    curr_label[j] = label++;
                    S.add_node();
                }
            }
            previous[j] = current[j];
            prev_label[j] = curr_label[j];
        }
    }



    printf("%u\n", S.count_sets());
    return 0;
}