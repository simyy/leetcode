#include <iostream>
#include <string>
#include <list>
using namespace std;

#ifndef _H_VISITOR
#define _H_VISITOR

class Employee;

class Visitor
{
public:
    virtual void visit(Employee* e) = 0; 
};

class Employee 
{
public:
    virtual void accept(Visitor* v) = 0;
};

class ConcreteEmployee : public Employee
{
public:
    ConcreteEmployee(string str):str(str) {}
    void accept(Visitor* v)
    {
        v->visit(this);
    }
    string getstr(){ return str; }
private:
    string str;
};

class ConcreteVistorA : public Visitor
{
public:
    void visit(Employee* e)
    {
        ConcreteEmployee* ce = dynamic_cast<ConcreteEmployee*>(e);
        cout<<"visitor A Elployee "<<ce->getstr()<<endl;
    }
};

class ConcreteVistorB : public Visitor
{
public:
    void visit(Employee* e)
    {
        ConcreteEmployee* ce = dynamic_cast<ConcreteEmployee*>(e);
        cout<<"visitor B Elployee "<<ce->getstr()<<endl;
    }
};

class ObjectStructure
{
public:
    void attach(Employee* e)
    {
        employees.push_back(e);
    }

    void detach(Employee* e)
    {
        employees.remove(e);
    }

    void accept(Visitor* v)
    {
        list<Employee*>::iterator it;
        for (it = employees.begin(); it != employees.end(); ++it) {
            (*it)->accept(v);
        }
    }

private:
    list<Employee*> employees;
};

#endif
