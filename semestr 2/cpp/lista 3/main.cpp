#include "queue.cpp"

void menu()
{
    cout << "0. Exit program" << endl;
    cout << "1. Add element" << endl;
    cout << "2. Remove element" << endl;
    cout << "3. Print element" << endl;
    cout << "4. Print number of elements" << endl;
    cout << "5. Print queue's capacity" << endl;
    cout << "6. Print the whole queue" << endl << endl;
}

int main()
{
    int initial;
    cout << "Enter queue capacity: ";
    cin >> initial;
    if (cin.fail()) throw invalid_argument("That is not a number!");
    queue q(initial);
    int choose;
    string element;

    while (true)
    {   
        menu();
        cin >> choose; cout << endl;

        if(cin.fail())
        {
            cin.clear();
            cin.ignore(10000, '\n');
            continue;
        }

        switch (choose)
        {
            case 0:
            {
                return 0;
            }

            case 1:
            {
                cout << "Type in a new element: ";
                cin >> element;
                
                try
                {
                    q.insert(element);
                }
                catch(out_of_range exc)
                {
                    clog << exc.what() << endl;
                }

                cout << endl;
                break;
            }

            case 2:
            {
                try
                {
                    cout << q.take_out() << endl;
                }
                catch(out_of_range exc)
                {
                    clog << exc.what() << endl;
                }

                cout << endl;
                break;
            }

            case 3:
            {
                try
                {
                    cout << q.beginning() << endl;
                }
                catch(out_of_range exc)
                {
                    clog << exc.what() << endl;
                }

                cout << endl;
                break;
            }

            case 4:
            {
                cout << q.number_of_elements() << endl << endl;
                break;
            }

            case 5:
            {
                cout << q.get_capacity() << endl << endl;
                break;
            }

            case 6:
            {
                q.print(); cout << endl;
            }
        }
    }
}