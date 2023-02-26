#ifndef figures_hpp
#define figures_hpp

class point 
{
    private:
        double x;
        double y;

    public:
        point();
        point(double x, double y);
        point(const point& p);
        point& operator=(const point& p);

        double get_x() const;
        double get_y() const;

        void print() const;
        void move(double x, double y);
        void rotate(const point& p, double angle);
};

double distance_between_points(const point& p1, const point& p2);



class segment
{
    private:
        point a;
        point b;

    public:
        segment(const point& p1, const point& p2);
        segment(const segment& s);
        segment& operator=(const segment& s);

        double get_ax() const;
        double get_ay() const;
        double get_bx() const;
        double get_by() const;

        void print() const;
        void move(double a, double b);
        void rotate(const point& p, double angle);
        double length() const;
        bool is_point_on_segment(const point& p) const;
        point middle_point() const;
};

bool are_parallel(const segment& s1, const segment& s2);
bool are_perpendicular(const segment& s1, const segment& s2);
point intersection(const segment& s1, const segment& s2);



class triangle
{
    private:
        point a;
        point b;
        point c;

    public:
        triangle(const point& p1, const point& p2, const point& p3);
        triangle(const triangle& t);
        triangle& operator=(const triangle& t);

        double get_ax() const;
        double get_ay() const;
        double get_bx() const;
        double get_by() const;
        double get_cx() const;
        double get_cy() const;      

        void print() const;
        void move(double a, double b);
        void rotate(const point& p, double angle);

        double perimeter() const;
        double area() const;
        bool is_point_in_triangle(const point& p) const;
        point center_point() const;

        point get_a() const;
        point get_b() const;
        point get_c() const;
};

bool are_disjoint(const triangle& t1, const triangle& t2);
bool does_contain(const triangle& t1, const triangle& t2);

#endif