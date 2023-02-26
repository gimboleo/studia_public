#ifndef queue_hpp
#define queue_hpp
#include <string>
using namespace std;

class queue
{
    private:
        string* elements;
        int max_capacity;
        int begin;
        int element_count;

    public:
        queue(int capacity);
        queue();
        queue(initializer_list<string> string_list);
        queue(const queue& q);
        queue& operator=(const queue& q);
        queue(queue&& q);
        queue& operator=(queue&& q);
        ~queue();

        void insert(string s);
        string take_out();
        string beginning() const;
        int number_of_elements() const;
        int get_capacity() const;
        void print() const;
};

#endif