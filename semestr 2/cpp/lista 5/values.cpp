#define _USE_MATH_DEFINES
#include "values.hpp"
#include <math.h>
#include <stdexcept>

number::number(double val)
{
    this->value = val;
}

int number::get_priority()
{
    return 0;
}

double number::calc()
{
    return this->value;
}

std::string number::to_string()
{
    if(floor(this->value) == this->value) return std::to_string(int(this->value));
    return std::to_string(this->value);
}



int constant::get_priority()
{
    return 0;
}

double pi::calc()
{
    return M_PI;
}

std::string pi::to_string()
{
    return "pi";
}

double e::calc()
{
    return M_E;
}

std::string e::to_string()
{
    return "e";
}

double phi::calc()
{
    return 1.618033988749895;
}

std::string phi::to_string()
{
    return "phi";
}



std::vector<std::pair <std::string, double>> variable::vars;

bool variable::is_declared(std::string s)
{
    for (auto& i : vars) if (s == i.first) return true;
    return false;
}

void variable::add_var(std::string s, double v)
{
    if(is_declared(s))
    {
        for (auto& i : vars)
        {
            if (s == i.first)
            {
                i.second = v;
                break;
            }
        }
    }
    else vars.push_back({s, v});
}

void variable::remove_var(std::string s)
{
    int j = 0;

    for (auto& i : vars)
    {
        if (s == i.first) break;
        j++;
    }

    if (j < vars.size()) vars.erase(vars.begin() + j);
}

void variable::change_name(std::string s1, std::string s2)
{
    int j = 0;

    for (auto& i : vars)
    {
        if (s1 == i.first)
        {
            i.first = s2;
            break;
        }
        j++;
    }

    if (j >= vars.size()) throw std::invalid_argument("Variable " + s1 + " doesn't exist");
}

void variable::change_val(std::string s, double v)
{
    for (auto& i : vars)
    {
        if (s == i.first)
        {
            i.second = v;
            return;
        }
    }

    throw std::invalid_argument("Variable " + s + " doesn't exist");
}

double variable::get_val(std::string s)
{
    for (auto& i : vars)
    {
        if (s == i.first) return i.second;
    }

    throw std::invalid_argument("Variable " + s + " doesn't exist");
}

variable::variable(std::string s)
{
    this->symbol = s;
}

int variable::get_priority()
{
    return 0;
}

double variable::calc()
{
    return get_val(this->symbol);
}

std::string variable::to_string()
{
    return this->symbol;
}