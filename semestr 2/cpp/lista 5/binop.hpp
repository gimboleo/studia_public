#ifndef binop_hpp
#define binop_hpp
#include "unop.hpp"

enum priorities
{
    Logarithm = 0,
    Power = 1,
    Mult = 2,
    Divide = 2,
    Modulo = 2,
    Add = 3,
    Sub = 3
};

class binop: public unop
{
    protected:
        expr* e2;
        binop(expr* e, expr* e2);

    public:
        virtual ~binop();
};

class add: public binop
{
    public:
        add(expr* e, expr* e2): binop(e, e2) {};

        int get_priority();
        double calc();
        std::string to_string();
};

class sub: public binop
{
    public:
        sub(expr* e, expr* e2): binop(e, e2) {};

        int get_priority();
        double calc();
        std::string to_string();
};

class mult: public binop
{
    public:
        mult(expr* e, expr* e2): binop(e, e2) {};

        int get_priority();
        double calc();
        std::string to_string();
};

class divide: public binop
{
    public:
        divide(expr* e, expr* e2): binop(e, e2) {};

        int get_priority();
        double calc();
        std::string to_string();
};

class logarithm: public binop
{
    public:
        logarithm(expr* e, expr* e2): binop(e, e2) {};

        int get_priority();
        double calc();
        std::string to_string();
};

class mod: public binop
{
    public:
        mod(expr* e, expr* e2): binop(e, e2) {};

        int get_priority();
        double calc();
        std::string to_string();
};

class power: public binop
{
    public:
        power(expr* e, expr* e2): binop(e, e2) {};

        int get_priority();
        double calc();
        std::string to_string();
};

#endif