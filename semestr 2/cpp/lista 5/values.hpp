#ifndef values_hpp
#define values_hpp
#include "expr.hpp"
#include <vector>

class number: public expr
{
    private:
        double value;

    public:
        number(double val);

        int get_priority();
        double calc();
        std::string to_string();
};



class constant: public expr
{
    public:
        int get_priority();

        virtual ~constant() = default;
};

class pi: public constant
{
    public:
        pi() = default;

        double calc();
        std::string to_string();
};

class e: public constant
{
    public:
        e() = default;

        double calc();
        std::string to_string();
};

class phi: public constant
{
    public:
        phi() = default;

        double calc();
        std::string to_string();
};



class variable: public expr
{
    private:
        static std::vector<std::pair <std::string, double>> vars;
        std::string symbol;

    public:
        static bool is_declared(std::string s);
        static void add_var(std::string s, double v);
        static void remove_var(std::string s);
        static void change_name(std::string s1, std::string s2);
        static void change_val(std::string s, double v);
        static double get_val(std::string s);

        variable(std::string s);

        int get_priority();
        double calc();
        std::string to_string();
};

#endif
