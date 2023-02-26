#include "values.cpp"
#include "unop.cpp"
#include "binop.cpp"
#include <iostream>
using namespace std;

int main()
{   
    expr *e1 = new divide(
        new mult (
            new sub(new variable("x"), new number(1)),
            new variable("x")),
        new number(2));

    cout << e1->to_string() << "\n";

    expr *e2 = new divide(
        new add(new number(3), new number(5)),
        new add(new number(2), new mult(
            new variable("x"), new number(7))));

    cout << e2->to_string() << "\n";

    expr *e3 = new sub(
        new add(new number(2), new mult(
            new variable("x"), new number(7))),
        new add(new mult(
                new variable("y"), new number(3)),
            new number(5)));

    cout << e3->to_string() << "\n";

    expr *e4 = new divide(
        new cosine(new mult(
            new add(
                new variable("x"), new number(1)),
            new variable("x"))),
        new power(new e(), new power(new variable("x"), new number(2))));
    
    cout << e4->to_string() << "\n";

    expr *e42 = new divide(
        new cosine(new mult(
            new add(
                new variable("x"), new number(1)),
            new variable("x"))),
        new exponential(new power(new variable("x"), new number(2))));
    
    cout << e42->to_string() << "\n";

    expr *e43 = new absolute(e42);

    cout << e43->to_string() << "\n";

    expr *e5 = new sub(
        new pi(),
        new add(
            new number(2),
            new mult(
                new variable("x"),
                new number(7))));

    cout << e5->to_string() << "\n";

    expr *e6 = new mod(new variable("x"), new number(5));

    cout << e6->to_string() << "\n";

    expr *e7 = new inverse(new opposite(new add(new variable("x"), new number(1))));

    cout << e7->to_string() << "\n";

    expr *e8 = new ln(new add(new variable("x"), new number(1)));

    cout << e8->to_string() << "\n\n\n";

    variable::add_var("x", 0);
    variable::add_var("y", 1);  

    for (int i = 0; i < 11; i ++)
    {
        variable::change_val("x", i);
        cout << "x = " << i << ":" << "\n";
        cout << e1->calc() << "\n";
        cout << e2->calc() << "\n";
        cout << e3->calc() << "\n";
        cout << e4->calc() << "\n";
        cout << e42->calc() << "\n";
        cout << e43->calc() << "\n";
        cout << e5->calc() << "\n";
        cout << e6->calc() << "\n";
        cout << e7->calc() << "\n";
        cout << e8->calc() << "\n\n";
    }
}