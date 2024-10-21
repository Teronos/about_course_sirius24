#include<iostream>
#include<string>

class AbstractTask
{
public:
    std::string inputText;
    virtual void Input()
    {
        std::cout << "Write Text \n";
    }
    virtual void Calculate()
    {

    }
    virtual std::string OutputResult()
    {
        return "empty";
    }
    virtual std::string GetName()
    {
        return "Task";
    }
};