#include "queue.hpp"
#include <stdexcept>
#include <iostream>

queue::queue(int capacity)
{
    if (capacity < 0) throw invalid_argument("Queue capacity must be bigger than 0!");

    this->max_capacity = capacity;
    this->begin = -1;
    this->element_count = 0;

    this->elements = new string[this->max_capacity];
}

queue::queue() : queue(1) {}

queue::queue(initializer_list<string> string_list)
{
    this->max_capacity = string_list.size();
    this->begin = -1;
    this->element_count = 0;
    this->elements = new string[this->max_capacity];

    for (string s: string_list) this->insert(s);
}

queue::queue(const queue& q)
{
    this->max_capacity = q.max_capacity;
    this->begin = q.begin;
    this->element_count = q.element_count;

    this->elements = new string[this->max_capacity];
    for (int i = 0; i < this->element_count; i++) this->elements[i] = q.elements[i];
}

queue& queue::operator=(const queue& q)
{
    if (&q != this)
    {
        delete[] this->elements;

        this->max_capacity = q.max_capacity;
        this->begin = q.begin;
        this->element_count = q.element_count;

        this->elements = new string[this->max_capacity];
        for (int i = 0; i < this->element_count; i++) this->elements[i] = q.elements[i];
    }

    return *this;
}

queue::queue(queue&& q)
{
    this->max_capacity = q.max_capacity;
    this->begin = q.begin;
    this->element_count = q.element_count;
    this->elements = q.elements;

    q.max_capacity = 0;
    q.begin = -1;
    q.element_count = 0;
    q.elements = nullptr;
}

queue& queue::operator=(queue&& q)
{
    if (&q != this)
    {
        delete[] this->elements;

        this->max_capacity = q.max_capacity;
        this->begin = q.begin;
        this->element_count = q.element_count;
        this->elements = q.elements;

        q.max_capacity = 0;
        q.begin = -1;
        q.element_count = 0;
        q.elements = nullptr;
    }

    return *this;
}

queue::~queue()
{
    delete this->elements;
}

void queue::insert(string s)
{
    if (this->element_count >= this->max_capacity) throw out_of_range("Couldn't add a new element, queue max capacity was already reached.");
    else
    {
        if (this->begin == -1) this->begin = 0;
        int index = (this->begin + this->element_count) % this->max_capacity;
        this->elements[index] = s;
        this->element_count++;
    } 
}

string queue::take_out()
{
    if (!this->element_count) throw out_of_range("Couldn't take out an element, this queue is empty!");
    else
    {
        int res = this->begin;
        if (!this->element_count) this->begin == -1;
        else this->begin = (this->begin + 1) % this->max_capacity;
        this->element_count--;

        return this->elements[res];        
    }
}

string queue::beginning() const
{
    if(!this->element_count) throw out_of_range("Couldn't return an element, this queue is empty!");
    else return this->elements[begin];
}

int queue::number_of_elements() const
{
    return this->element_count;
}

int queue::get_capacity() const
{
    return this->max_capacity;
}

void queue::print() const
{
    int i = 1;
    for(int c = 0; c < this->element_count; c++)
    {
        cout << i << ". " << this->elements[(this->begin + c) % this->max_capacity] << endl;
        i++;
    }
}