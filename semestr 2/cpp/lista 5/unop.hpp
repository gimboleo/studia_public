#ifndef unop_hpp
#define unop_hpp
#include "expr.hpp"

class unop: public expr
{
    protected:
        expr* e;
        unop(expr* e);

    public:
        int get_priority();

        virtual ~unop();
};

class sine: public unop
{
    public:
        sine(expr* e): unop(e) {};

        double calc();
        std::string to_string();

};

class cosine: public unop
{
    public:
        cosine(expr* e): unop(e) {};

        double calc();
        std::string to_string();

};

class exponential: public unop
{
    public:
        exponential(expr* e): unop(e) {};

        double calc();
        std::string to_string();

};

class ln: public unop
{
    public:
        ln(expr* e): unop(e) {};

        double calc();
        std::string to_string();

};

class absolute: public unop
{
    public:
        absolute(expr* e): unop(e) {};

        double calc();
        std::string to_string();

};

class opposite: public unop
{
    public:
        opposite(expr* e): unop(e) {};

        double calc();
        std::string to_string();

};

class inverse: public unop
{
    public:
        inverse(expr* e): unop(e) {};

        double calc();
        std::string to_string();

};

#endif