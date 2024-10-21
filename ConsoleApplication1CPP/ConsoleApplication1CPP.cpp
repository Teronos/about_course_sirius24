
#include <iostream>
#include <string>
#include "ArrayTask.cpp"
#include <vector>


std::vector<AbstractTask*> tasks;

void InitializeTask()
{
    tasks.push_back(new Task1());
    tasks.push_back(new Task2());
    tasks.push_back(new Task2EXTRA());
    tasks.push_back(new Task3());
    tasks.push_back(new Task3Extra());
    tasks.push_back(new Task4());
    tasks.push_back(new Task4Extra());
    tasks.push_back(new Task5());
    tasks.push_back(new Task5_1());
    tasks.push_back(new Task5EXTRA());
    tasks.push_back(new Task6());
    tasks.push_back(new Task6Extra());
    tasks.push_back(new Task7());
    tasks.push_back(new Task7Extra());
    tasks.push_back(new Task8());
    tasks.push_back(new Task8Extra());
    tasks.push_back(new Task9());
    tasks.push_back(new Task9_1());
    tasks.push_back(new Task9Extra());
    tasks.push_back(new Task10());
}
void Clear()
{
    std::system("cls");
}
int main()
{
    InitializeTask();
    while (true)
    {
        Clear();
        std::cout << "Write number Task \n";
        for (int i = 0; i < tasks.size(); i++)
        {
            std::cout << "index: " << std::to_string(i) << " " << "Name: " << tasks[i]->GetName() << "\n";
        }
        int writeNum;
        std::cin >> writeNum;
        if (tasks.size() <= writeNum || writeNum < 0)
            continue;
        Clear();
        AbstractTask* task = tasks[writeNum];
        task->Input();
        task->Calculate();
        std::cout << task->OutputResult();
        std::cout << "\n" << "Press Enter to Continue";

        std::cin.get();
        std::cin.get();
    }
}



