#ifndef expr_hpp
#define expr_hpp
#include <string>

class expr
{
    protected:
        expr() = default;

    public:
        virtual int get_priority() = 0;
        virtual double calc() = 0;
        virtual std::string to_string() = 0;

        expr(const expr&) = delete;
        expr& operator=(const expr&) = delete;
        expr(expr&&) = delete;
        expr& operator=(expr &&) = delete;
        
        virtual ~expr() = default;
};

#endif