#define _USE_MATH_DEFINES
#include "figures.hpp"
#include <iostream>
#include <cmath>
#include <stdexcept>
#include <algorithm>
#include <cstdlib>
using namespace std;

point::point()
{
    this->x = 0;
    this->y = 0;
}

point::point(double x, double y)
{
    this->x = x;
    this->y = y;
}

point::point(const point& p)
{
    this->x = p.x;
    this->y = p.y;
}

point& point::operator=(const point& p)
{
    if (&p != this)
    {
        this->x = p.x;
        this->y = p.y;
    }
    return *this;
}

double point::get_x() const
{
    return this->x;
}

double point::get_y() const
{
    return this->y;
}

void point::print() const
{
    cout << "(" << this->x << ", " << this->y << ")" << endl;
}

void point::move(double x, double y)
{
    this->x = this->x + x;
    this->y = this->y + y;
}

void point::rotate(const point& p, double angle)
{
    double new_x = (this->x - p.x) * cos(angle) - (this->y - p.y) * sin(angle) + p.x;
    double new_y = (this->x - p.x) * sin(angle) + (this->y - p.y) * cos(angle) + p.y;
    this->x = new_x;
    this->y = new_y;
}

double distance_between_points(const point& p1, const point& p2)
{
    double x1 = p1.get_x();
    double x2 = p2.get_x();
    double y1 = p1.get_y();
    double y2 = p2.get_y();
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}



segment::segment(const point& p1, const point& p2)
{
    if (p1.get_x() == p2.get_x() && p1.get_y() == p2.get_y()) throw invalid_argument("Segment must be longer than 0!");

    this->a = p1;
    this->b = p2;
}

segment::segment(const segment& s)
{
    this->a = s.a;
    this->b = s.b;
}

segment& segment::operator=(const segment& s)
{
    if (&s != this)
    {
        this->a = s.a;
        this->b = s.b;
    }
    return *this;
}

double segment::get_ax() const
{
    return this->a.get_x();
}

double segment::get_ay() const
{
    return this->a.get_y();
}

double segment::get_bx() const
{
    return this->b.get_x();
}

double segment::get_by() const
{
    return this->b.get_y();
}

void segment::print() const
{
    this->a.print();
    this->b.print();
}

void segment::move(double x, double y)
{
    this->a.move(x,y);
    this->b.move(x,y);
}

void segment::rotate(const point& p, double angle)
{
    this->a.rotate(p, angle);
    this->b.rotate(p, angle);
}

double segment::length() const
{
    return distance_between_points(this->a, this->b);
}

bool segment::is_point_on_segment(const point& p) const
{
    double xc = p.get_x();
    double yc = p.get_y();
    double xa = this->get_ax();
    double ya = this->get_ay();
    double xb = this->get_bx();
    double yb = this->get_by();

    if (!distance_between_points(this->a, p) || !distance_between_points(this->b, p)) return true;
    if (xb*yc + xa*yb + xc*ya - xa*yc - xb*ya - xc*yb != 0) return false;
    if (xc < min(xa, xb) || xc > max(xa, xb)) return false;
    if (yc < min(ya, yb) || yc > max(ya, yb)) return false;
    return true;
}

point segment::middle_point() const
{
    return point((this->get_ax() + this->get_bx()) / 2, (this->get_ay() + this->get_by()) / 2);
}

bool are_parallel(const segment& s1, const segment& s2)
{
    double xa = s1.get_ax();
    double ya = s1.get_ay();
    double xb = s1.get_bx();
    double yb = s1.get_by();
    double xc = s2.get_ax();
    double yc = s2.get_ay();
    double xd = s2.get_bx();
    double yd = s2.get_by();

    if (xa == xb && xc == xd) return true;

    double a1 = (ya - yb) / (xa - xb);
    double a2 = (yc - yd) / (xc - xd);

    return (a1 == a2);
}

bool are_perpendicular(const segment& s1, const segment& s2)
{
    double xa = s1.get_ax();
    double ya = s1.get_ay();
    double xb = s1.get_bx();
    double yb = s1.get_by();
    double xc = s2.get_ax();
    double yc = s2.get_ay();
    double xd = s2.get_bx();
    double yd = s2.get_by();

    if ((xa == xb && yc == yd) || (xc == xd && ya == yb)) return true;

    double a1 = (ya - yb) / (xa - xb);
    double a2 = (yc - yd) / (xc - xd);

    return (a1 * a2 == -1);
}

point intersection(const segment& s1, const segment& s2)
{
    if (are_parallel(s1, s2)) throw invalid_argument("Segments are parallel!");

    double xa = s1.get_ax();
    double ya = s1.get_ay();
    double xb = s1.get_bx();
    double yb = s1.get_by();
    double xc = s2.get_ax();
    double yc = s2.get_ay();
    double xd = s2.get_bx();
    double yd = s2.get_by();

    double a1 = (ya - yb) / (xa - xb);
    double a2 = (yc - yd) / (xc - xd);
    double b1 = (ya - (ya - yb) / (xa - xb) * xa);
    double b2 = (yc - (yc - yd) / (xc - xd) * xc);

    double x;
    double y;

    if (xc == xd)
    {
        x = (a1 - b1) / xc;
        y = xc;
    }
    else if (xa == xb)
    {
        x = (a2 - b2) / xa;
        y = xa;
    }
    else
    {
        x = (b2 - b1) / (a1 - a2);
        y = a1 * x + b1;
    }
    point res(x, y);
    if (s1.is_point_on_segment(res) && s2.is_point_on_segment(res)) return res;
    else throw invalid_argument("Segments don't intersect!");
}



triangle::triangle(const point& p1, const point& p2, const point& p3)
{
    double x1 = p1.get_x();
    double x2 = p2.get_x();
    double x3 = p3.get_x();
    double y1 = p1.get_y();
    double y2 = p2.get_y();
    double y3 = p3.get_y();

    if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) == 0) throw invalid_argument("Given points are collinear!");

    this->a = p1;
    this->b = p2;
    this->c = p3;
}

triangle::triangle(const triangle& t)
{
    this->a = t.a;
    this->b = t.b;
    this->c = t.c;
}

triangle& triangle::operator=(const triangle& t)
{
    if (&t != this)
    {
        this->a = t.a;
        this->b = t.b;
        this->c = t.c;
    }
    return *this;
}

double triangle::get_ax() const
{
    return this->a.get_x();
}

double triangle::get_ay() const
{
    return this->a.get_y();
}

double triangle::get_bx() const
{
    return this->b.get_x();
}

double triangle::get_by() const
{
    return this->b.get_y();
}

double triangle::get_cx() const
{
    return this->c.get_x();
}

double triangle::get_cy() const
{
    return this->c.get_y();
}

void triangle::print() const
{
    this->a.print();
    this->b.print();
    this->c.print();
}

void triangle::move(double x, double y)
{
    this->a.move(x,y);
    this->b.move(x,y);
    this->c.move(x,y);
}

void triangle::rotate(const point& p, double angle)
{
    this->a.rotate(p, angle);
    this->b.rotate(p, angle);
    this->c.rotate(p, angle);
}

double triangle::perimeter() const
{
    segment temp1(this->a, this->b);
    segment temp2(this->b, this->c);
    segment temp3(this->c, this->a);

    return temp1.length() + temp2.length() + temp3.length();
}

double triangle::area() const
{
    double xa = this->get_ax();
    double xb = this->get_bx();
    double xc = this->get_cx();
    double ya = this->get_ay();
    double yb = this->get_by();
    double yc = this->get_cy();

    return 0.5 * abs((xb - xa) * (yc - ya) - (yb - ya) * (xc - xa));
}

bool triangle::is_point_in_triangle(const point& p) const
{
    double xa = this->get_ax();
    double xb = this->get_bx();
    double xc = this->get_cx();
    double ya = this->get_ay();
    double yb = this->get_by();
    double yc = this->get_cy();
    double xp = p.get_x();
    double yp = p.get_y();

    double c1 = (xb - xa) * (yp - ya) - (yb - ya) * (xp - xa);
    double c2 = (xc - xb) * (yp - yb) - (yc - yb) * (xp - xb);
    double c3 = (xa - xc) * (yp - yc) - (ya - yc) * (xp - xc);

    if ((c1 <= 0 && c2 <= 0 && c3 <= 0) || (c1 >= 0 && c2 >= 0 && c3 >= 0)) return true;
    return false;
}

point triangle::center_point() const
{
    double xa = this->get_ax();
    double xb = this->get_bx();
    double xc = this->get_cx();
    double ya = this->get_ay();
    double yb = this->get_by();
    double yc = this->get_cy();

    return point((xa + xb + xc) / 3, (ya + yb + yc) / 3);
}

point triangle::get_a() const
{
    return this->a;
}

point triangle::get_b() const
{
    return this->b;
}

point triangle::get_c() const
{
    return this->c;
}

bool are_disjoint(const triangle& t1, const triangle& t2)
{
    segment A(t1.get_a(), t1.get_b()); segment B(t1.get_b(), t1.get_c()); segment C(t1.get_c(), t1.get_a());
    segment D(t2.get_a(), t2.get_b()); segment E(t2.get_b(), t2.get_c()); segment F(t2.get_c(), t2.get_a());

    segment T[3] = {A, B, C};
    segment T2[3] = {D, E, F};
    int flag = 0;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            try
            {
                intersection(T[i], T2[j]);
            }
            catch(invalid_argument exc)
            {
                flag = flag + 1;
            }
        }
    }

    return (flag == 9);
}

bool does_contain(const triangle& t1, const triangle& t2)
{
    point a = t2.get_a();
    point b = t2.get_b();
    point c = t2.get_c();

    return (t1.is_point_in_triangle(a) && t1.is_point_in_triangle(b) && t1.is_point_in_triangle(c));
}