#include "binop.hpp"
#include <math.h>
#include <stdexcept>

binop::binop(expr* e, expr* e2): unop(e)
{
    this->e2 = e2;
}

binop::~binop()
{
    delete this->e;
    delete this->e2;
    delete this;
}

int add::get_priority()
{
    return Add;
}

double add::calc()
{
    return this->e->calc() + this->e2->calc();
}

std::string add::to_string()
{
    std::string l = this->e->to_string();
    std::string r = this->e2->to_string();
    if (this->e->get_priority() > this->get_priority()) l = "(" + l + ")";
    if (this->e2->get_priority() > this->get_priority()) r = "(" + r + ")";
    return l + " + " + r;
}

int sub::get_priority()
{
    return Sub;
}

double sub::calc()
{
    return this->e->calc() - this->e2->calc();
}

std::string sub::to_string()
{
    std::string l = this->e->to_string();
    std::string r = this->e2->to_string();
    if (this->e->get_priority() > this->get_priority()) l = "(" + l + ")";
    if (this->e2->get_priority() >= this->get_priority()) r = "(" + r + ")";
    return l + " - " + r;
}

int mult::get_priority()
{
    return Mult;
}

double mult::calc()
{
    return this->e->calc() * this->e2->calc();
}

std::string mult::to_string()
{
    std::string l = this->e->to_string();
    std::string r = this->e2->to_string();
    if (this->e->get_priority() > this->get_priority()) l = "(" + l + ")";
    if (this->e2->get_priority() > this->get_priority()) r = "(" + r + ")";
    return l + " * " + r;
}

int divide::get_priority()
{
    return Divide;
}

double divide::calc()
{
    double temp = this->e2->calc();
    if (temp) return this->e->calc() / temp;
    throw std::invalid_argument(this->to_string() + " is invalid, would cause division by zero"); 
}

std::string divide::to_string()
{
    std::string l = this->e->to_string();
    std::string r = this->e2->to_string();
    if (this->e->get_priority() > this->get_priority()) l = "(" + l + ")";
    if (this->e2->get_priority() >= this->get_priority()) r = "(" + r + ")";
    return l + " / " + r;
}

int logarithm::get_priority()
{
    return Logarithm;
}

double logarithm::calc()
{
    double temp = this->e->calc();
    double temp2 = this->e2->calc();

    if (temp <= 0) throw std::invalid_argument(this->to_string() + " is invalid, base must be greater than zero");
    if (temp == 1) throw std::invalid_argument(this->to_string() + " is invalid, base can't be equal to 1");
    if (temp2 <= 0) throw std::invalid_argument(this->to_string() + " is invalid, argument must be greater than zero");

    return log(temp) / log(temp2);
}

std::string logarithm::to_string()
{
    return "log[" + this->e->to_string() + ", " + this->e2->to_string() + "]";
}

int mod::get_priority()
{
    return Modulo;
}

double mod::calc()
{
    double temp = this->e2->calc();
    if (temp) return fmod(this->e->calc(), temp);
    throw std::invalid_argument(this->to_string() + " is invalid, would cause division by zero");
}

std::string mod::to_string()
{
    std::string l = this->e->to_string();
    std::string r = this->e2->to_string();
    if (this->e->get_priority() > this->get_priority()) l = "(" + l + ")";
    if (this->e2->get_priority() >= this->get_priority()) r = "(" + r + ")";
    return l + " % " + r;
}

int power::get_priority()
{
    return Power;
}

double power::calc()
{
    double temp = this->e->calc();
    double temp2 = this->e2->calc();
    if (!temp && temp2 < 0) throw std::invalid_argument(this->to_string() + " is invalid, would cause division by zero");

    return pow(temp, temp2);
}

std::string power::to_string()
{
    std::string l = this->e->to_string();
    std::string r = this->e2->to_string();
    if (this->e->get_priority() > this->get_priority()) l = "(" + l + ")";
    if (this->e2->get_priority() >= this->get_priority()) r = "(" + r + ")";
    return l + "^" + r;
}