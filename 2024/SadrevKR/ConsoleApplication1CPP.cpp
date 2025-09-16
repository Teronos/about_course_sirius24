#include <iostream>
#include <string>
#include "ArrayTask.cpp"
#include <vector>


std::vector<std::unique_ptr<AbstractTask>> tasks;

void InitializeTask()
{
    tasks.push_back(std::make_unique<Task1>());
    tasks.push_back(std::make_unique<Task2>());
    tasks.push_back(std::make_unique<Task2EXTRA>());
    tasks.push_back(std::make_unique<Task3>());
    tasks.push_back(std::make_unique<Task3Extra>());
    tasks.push_back(std::make_unique<Task4>());
    tasks.push_back(std::make_unique<Task4Extra>());
    tasks.push_back(std::make_unique<Task5>());
    tasks.push_back(std::make_unique<Task5_1>());
    tasks.push_back(std::make_unique<Task5EXTRA>());
    tasks.push_back(std::make_unique<Task6>());
    tasks.push_back(std::make_unique<Task6Extra>());
    tasks.push_back(std::make_unique<Task7>());
    tasks.push_back(std::make_unique<Task7Extra>());
    tasks.push_back(std::make_unique<Task8>());
    tasks.push_back(std::make_unique<Task8Extra>());
    tasks.push_back(std::make_unique<Task9>());
    tasks.push_back(std::make_unique<Task9Extra>());
    tasks.push_back(std::make_unique<Task10>());
    tasks.push_back(std::make_unique<Task10Extra>());
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
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

        if (tasks.size() <= writeNum || writeNum < 0)
            continue;

        Clear();
        AbstractTask& task = *tasks[writeNum];

        task.Input();
        task.Calculate();
        std::cout << task.OutputResult();

        std::cout << "\n" << "Press Enter to Continue";

        std::cin.get(); // теперь достаточно одного get
    }
}



