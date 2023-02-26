#include "queue.cpp"

int main()
{
    queue q(11);
    q.insert("abc");
    cout << q.beginning() << endl;
    cout << q.number_of_elements() << endl;

    queue q2(q);
    queue q3 = q2;

    q2.insert("cde");
    q3.insert("dfe");

    cout << q2.number_of_elements() << " " << q3.number_of_elements() << endl;
    cout << q2.take_out() << " " << q2.take_out() << endl;
    cout << q3.take_out() << " " << q3.take_out() << endl;

    queue q4 = queue();
    cout << q4.number_of_elements() << " " << q4.get_capacity() << endl << endl;
    
    queue q5{"a", "b", "c", "d"};
    cout << q5.get_capacity() << endl;
    q5.print(); cout << endl;

    queue q6 = move(q5);
    q6.print(); cout << endl;
    q5.print();

    return 0;
}