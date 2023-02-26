#ifndef rational_exception_hpp
#define rational_exception_hpp
#include <stdexcept>

namespace computations
{
    class rational_exception: std::logic_error 
    {
        public:
            explicit rational_exception(const char* exc): std::logic_error(exc) {};
            virtual const char* what() const noexcept {return std::logic_error::what();};
    };

    class division_by_zero: rational_exception 
    {
        public:
            explicit division_by_zero(const char* exc): rational_exception(exc) {}
            virtual const char* what() const noexcept {return rational_exception::what();};
    };

    class out_of_range: rational_exception 
    {
        public:
            explicit out_of_range(const char* exc): rational_exception(exc) {};
            virtual const char* what() const noexcept {return rational_exception::what();};
    };
}

#endif