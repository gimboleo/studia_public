#include "unop.hpp"
#include <math.h>
#include <stdexcept>

unop::unop(expr* e)
{
    this->e = e;
}

int unop::get_priority()
{
    return 0;
}

unop::~unop()
{
    delete this->e;
    delete this;
}

double sine::calc()
{
    return sin(this->e->calc());
}

std::string sine::to_string()
{
    return "sin(" + this->e->to_string() + ")";
}

double cosine::calc()
{
    return cos(this->e->calc());
}

std::string cosine::to_string()
{
    return "cos(" + this->e->to_string() + ")";
}

double exponential::calc()
{
    return exp(this->e->calc());
}

std::string exponential::to_string()
{
    return "exp(" + this->e->to_string() + ")";
}

double ln::calc()
{   
    double temp = this->e->calc();
    if (temp > 0) return log(this->e->calc());
    throw std::invalid_argument(this->to_string() + " is invalid, argument must be greater than zero");
}

std::string ln::to_string()
{
    return "ln(" + this->e->to_string() + ")";
}

double absolute::calc()
{
    return abs(this->e->calc());
}

std::string absolute::to_string()
{
    return "|" + this->e->to_string() + "|";
}

double opposite::calc()
{
    return -1 * this->e->calc();
}

std::string opposite::to_string()
{ 
    std::string t = this->e->to_string();
    if (t == "0") return "0";
    if (this->e->get_priority() > this->get_priority()) t = "(" + t + ")";
    return "-" + t;
}

double inverse::calc()
{
    double temp = this->e->calc();
    if (temp) return 1 / temp;
    throw std::invalid_argument("Inversing " + e->to_string() + " would cause division by zero");
}

std::string inverse::to_string()
{
    std::string t = this->e->to_string();
    if (this->e->get_priority() > this->get_priority()) t = "(" + t + ")";
    return t + "^-1";
}