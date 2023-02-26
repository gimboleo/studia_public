#include "figures.cpp"

int main()
{
    point p(1,2);
    p.print();
    point p2(p);
    p2.print();
    point p3 = p2;
    p3.print();
    cout << endl;

    point p0(0, 0);
    p.move(1, 10);                                          //(2,12)
    p2.rotate(p0, M_PI_2);                                  //(1,2) --> (-2,1)
    p3.move(-5, 2);                                         //(-4,4)
    p.print();
    p2.print();
    p3.print();
    cout << endl;

    cout << distance_between_points(p, p) << endl;          //0
    cout << distance_between_points(p3, p2) << endl;        //3.605551
    cout << endl << endl << endl;
    

    point p4(5, 5);
    point p5(8, 5);
    segment s(p4, p5);
    segment s2(s);
    segment s3 = s2;
    s.print(); cout << endl;
    s2.print(); cout << endl;
    s3.print(); cout << endl << endl;

    s.move(3, 1);                                           //(8,6) (11,6)
    s2.move(1, 1);                                          //(6,6) (9,6) 
    s3.rotate(p0, M_PI_2);                                  //(5,5) -> (-5,5) (8,5) -> (-5, 8)
    s.print(); cout << endl;
    s2.print(); cout << endl;
    s3.print(); cout << endl << endl;  

    point p6(5, 5);
    try
    {
    segment s4(p4, p6);
    }
    catch(invalid_argument exc)
    {
        clog << exc.what() << endl << endl;
    }

    cout << s.length() << endl;                             //3
    cout << s2.length() << endl;                            //3    
    cout << s3.length() << endl << endl;                    //3

    point p7(1, 2);
    point p8(5, 10);
    point p9(3, 6);
    segment s4(p7, p8);
    cout << s4.is_point_on_segment(p9) << endl;             //true
    cout << s4.is_point_on_segment(p6) << endl << endl;     //false

    s4.middle_point().print();                              //(3,6)
    s3.middle_point().print();                              //(-5, 6.5)
    s.middle_point().print(); cout << endl;                 //(9.5, 6)

    cout << are_parallel(s, s2) << endl;                    //true
    cout << are_parallel(s, s4) << endl << endl;            //false

    cout << are_perpendicular(s, s2) << endl;               //false
    point p10(3, 1);
    point p11(3, 4);
    segment s5(p10, p11);
    cout << are_perpendicular(s, s5) << endl << endl;       //true   

    point p12(4, 8);
    point p13(1, 1);
    segment s6(p12, p13);
    intersection(s4, s6).print();                           //(4,8)
    try
    {
    intersection (s5, s6);
    }
    catch(invalid_argument exc)
    {
        clog << exc.what() << endl << endl;
    }
    cout << endl << endl;



    try
    {
        triangle(point(1, 2), point(2, 4), point(3, 6));
    }
    catch(invalid_argument exc)
    {
        clog << exc.what() << endl << endl;
    }

    triangle t1(point(1, 2), point(2, 4), point(3, 8));
    triangle t2(t1);
    triangle t3 = t2;
    t1.print(); cout << endl;
    t2.print(); cout << endl;
    t3.print(); cout << endl << endl;

    t2.move(1, 1);
    t3.rotate(p0, M_PI_2);
    t1.print(); cout << endl;                               //(1,2) (2,4) (3,8)   
    t2.print(); cout << endl;                               //(2,3) (3,5) (4,9)
    t3.print(); cout << endl << endl;                       //(-2,1) (-4,2) (-8,3)

    cout << t1.perimeter() << endl;                         //12.684
    cout << t1.area() << endl << endl;                      //1

    triangle t4(point(0, 0), point(10, 0), point(5, 20));
    cout << t4.is_point_in_triangle(point(5, 10)) << endl;  //true
    cout << t4.is_point_in_triangle(point(5, 20)) << endl;  //true
    cout << t4.is_point_in_triangle(point(5, 21)) << endl;  //false
    cout << endl << endl;

    t1.center_point().print();                              //(2, 4.667) 
    t4.center_point().print();                              //(5, 6.667)
    cout << endl << endl;
    
    cout << are_disjoint(t1, t2) << endl;                   //true
    t2.move(-1, 0);                                         //(1,3) (2,5) (4,9)
    cout << are_disjoint(t1, t2) << endl;                   //false
    cout << endl << endl;

    cout << does_contain(t1, t2) << endl;                   //false
    cout << does_contain(t4, t1) << endl;                   //true

    return 0;
}