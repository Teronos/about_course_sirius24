#include "AbstractTask.cpp"
#include "NumberVect.cpp"
#include <sstream>
#include <bitset>
#include <list>
#include <vector>

using namespace std;

class Task1 : public AbstractTask
{
    int numberResult;
public:
    void Input() override
    {
        std::cout << "Write down the numbers whose numbers will multiply \n";
        std::cin >> inputText;
    }
    void Calculate() override
    {
        int numeric = 1;
        for (int i = 0; i < inputText.length(); i++)
        {
            auto y = static_cast <int>(inputText[i] - '0');
            numeric *= y;
        }
        numberResult = numeric;
    }
    std::string OutputResult() override
    {
        return "Result: " + std::to_string(numberResult);
    }
    std::string GetName() override
    {
        return "Task 1 Multiply Number";
    }
};

class Task2 : public AbstractTask
{
    std::string numberResult;
public:
    void Input() override
    {
        std::cout << "Write number to revert \n";
        std::cin >> inputText;
    }
    void Calculate() override
    {
        std::string newNumber;
        for (int i = inputText.length(); i >= 0 ; i--)
        {
            newNumber += inputText[i];
        }
        numberResult = newNumber;
    }
    std::string OutputResult() override
    {
        return "Result: " + numberResult;
    }
    std::string GetName() override
    {
        return "Task 2 Revert number";
    }
};

class Task2EXTRA : public AbstractTask
{
    std::string numberResult;
public:
    void Input() override
    {
        std::cout << "Write number to Sum of even and odd \n";
        std::cin >> inputText;
    }
    void Calculate() override
    {
        int newNumber1 = 0;
        int newNumber2 = 0;
        for (int i = 0; i < inputText.length(); i++)
        {
            if(i % 2 == 0)
                newNumber1 += (inputText[i] - '0');
            else
                newNumber2 += (inputText[i] - '0');
        }
        numberResult = std::to_string(newNumber1) + std::to_string(newNumber2);
    }
    std::string OutputResult() override
    {
        return "Result: " + numberResult;
    }
    std::string GetName() override
    {
        return "Task2Extra even and odd";
    }
};
class Task3 : public AbstractTask
{
    int numberResult;
    int iterator;
    std::vector<int> numbers;
public:
    void Input() override
    {
        std::cout << "Write N iteration \n";
        std::cin >> iterator;
        std::cout << "Write" << std::to_string(iterator) << " numbers\n";
        for (int i = 0; i < iterator; i++)
        {
            int number = 0;
            std::cin >> number;
            numbers.push_back(number);
        }
    }
    void Calculate() override
    {
        numberResult = 0;
        for(int i = 0; i < numbers.size(); i++)
        {
            if (numbers[i] == 0)
            {
                numberResult++;
            }
        }
    }
    std::string OutputResult() override
    {
        return "Result: " + std::to_string(numberResult);
    }
    std::string GetName() override
    {
        return "Task3 count zero";
    }
};
class Task3Extra : public AbstractTask
{
    double numberResult;
    int iterator;
    std::vector<int> numbers;
public:
    void Input() override
    {
        std::cout << "Write N iteration \n";
        std::cin >> iterator;
        std::cout << "Write " << std::to_string(iterator) << " numbers\n";
        for (int i = 0; i < iterator; i++)
        {
            int number = 0;
            std::cin >> number;
            numbers.push_back(number);
        }
    }
    void Calculate() override
    {
        int sumNumber = 0;
        int countMultiplyOfThree = 0;
        for (int i = 0; i < numbers.size(); i++)
        {
            if (numbers[i] % 3 == 0)
            {
                sumNumber += numbers[i];
                countMultiplyOfThree += 1;
            }
        }
        if (countMultiplyOfThree == 1)
        {
            numberResult = -1;
            return;
        }
        numberResult = (double)sumNumber / (double)iterator;
    }
    std::string OutputResult() override
    {
        return "Result: " + std::to_string(numberResult);
    }
    std::string GetName() override
    {
        return "Task3Extra Middle of Multiple of 3";
    }
};

class Task4 : public AbstractTask
{
    double numberResult;
    int iterator;
    std::vector<int> numbers;
public:
    void Input() override
    {
        cout << "Write N iteration \n";
        cin >> iterator;
        cout << "Write " << to_string(iterator) << " numbers\n";
        for (int i = 0; i < iterator; i++)
        {
            int number = 0;
            cin >> number;
            numbers.push_back(number);
        }
    }
    void Calculate() override
    {
        int maxNumber = numeric_limits<int>::max();

        int minNumber = maxNumber;

        if (iterator == 0)
        {
            numberResult = - 1;
            return;
        }
        for (int i = 0; i < numbers.size(); i++)
        {
            if (numbers[i] < minNumber)
            {
                minNumber = numbers[i];
            }
        }
        if (minNumber == maxNumber)
        {
            numberResult = -1;
            return;
        }
        int countMin = 0;
        for (int i = 0; i < numbers.size(); i++)
        {
            if (numbers[i] == minNumber)
            {
                countMin++;
            }
        }
        if (countMin == 0)
        {
            numberResult = -1;
            return;
        }
        numberResult = countMin;
        numbers.clear();
    }
    string OutputResult() override
    {
        return "Result: " + std::to_string(numberResult);
    }
    string GetName() override
    {
        return "Task4 Min count";
    }
};

class Task4Extra : public AbstractTask
{
    int numberResult;
    int searchFibanachi;
public:
    void Input() override
    {
        error:
        cout << "Write NumberFibanachi N>1 \n";
        cin >> searchFibanachi;
        if (searchFibanachi <= 1)
            goto error;
    }
    void Calculate() override
    {
        int currentNum = 1;
        int previousNum = 1;
        int countIteration = 3;
        while (true)
        {
            countIteration++;
            int previousOut = previousNum;
            previousNum = currentNum;
            currentNum += previousOut;
            if (searchFibanachi == currentNum)
                break;
            if (searchFibanachi < currentNum)
            {
                numberResult = -1;
                return;
            }
        }
        numberResult = countIteration;
    }
    string OutputResult() override
    {
        return "Result: " + std::to_string(numberResult);
    }
    string GetName() override
    {
        return "Task4Extra Find Num Fibanachi";
    }
};
class Task5 : public AbstractTask
{
    int numberResult;
    int A;
    int B;
public:
    void Input() override
    {
    
        cout << "Write number A \n";
        cin >> A;
    error:
        cout << "Write number B (A<=B) \n";
        cin >> B;
        if (A > B)
            goto error;
    }
    void Calculate() override
    {
        for (int i = B; i >= A; i--)
        {
            if (i % 7 == 0)
            {
                numberResult = i;
                return;
            }
        }
    }
    string OutputResult() override
    {
        return "Result: " + std::to_string(numberResult);
    }
    string GetName() override
    {
        return "Task5 Max % 7 number";
    }
};
class Task5_1 : public AbstractTask
{
    string result;
    string DNK;
public:
    void Input() override
    {
        cout << "Write DNK (A, T, C, G) \n";
        cin >> DNK;
    }
    void Calculate() override
    {
        for (int i = 0; i < DNK.size(); i++)
        {
            result = result + Complimentary(DNK[i]);
        }
    }
    char Complimentary(char DNK)
    {
        switch (DNK)
        {
        case 'A':
            return 'T';
        case 'G':
            return 'C';
        case 'C':
            return 'G';
        default: 
            return 'A';
            break;
        }
    }
    string OutputResult() override
    {
        return "Result: " + result;
    }
    string GetName() override
    {
        return "Task5_1 DNK Complimentary";
    }
};
class Task5EXTRA : public AbstractTask
{
    string result;
    int numberUP;
public:
    void Input() override
    {
        cout << "Write number for 2^N\n";
        cin >> numberUP;
    }
    void Calculate() override
    {
        result = "1";
        int numeric = 2;
        int multiply = 1;
        while (numeric < numberUP)
        {
            int resultMultiply = pow(numeric, multiply);
            if (resultMultiply < numberUP)
            {
                result += " " + to_string(resultMultiply);
            }
            else
                break;
            multiply++;
        }
    }
    string OutputResult() override
    {
        return "Result: " + result;
    }
    string GetName() override
    {
        return "Task5EXTRA 2^N";
    }
};
class Task6 : public AbstractTask
{
    string result;
    int iterator;
    int numberUP;
    vector<int> numbers;
public:
    void Input() override
    {
        cout << "Write N iteration \n";
        cin >> iterator;
        cout << "Write " << to_string(iterator) << " numbers\n";
        for (int i = 0; i < iterator; i++)
        {
            int number = 0;
            cin >> number;
            numbers.push_back(number);
        }
    }
    void Calculate() override
    {
        int max = *max_element(numbers.begin(), numbers.end());
        result = to_string(max);
    }
    string OutputResult() override
    {
        return "Result: " + result;
    }
    string GetName() override
    {
        return "Task6 Max Element";
    }
};
class Task6Extra : public AbstractTask
{
    string result;
    int iterator;
    int numberUP;
    vector<int> numbers;
public:
    void Input() override
    {
        cout << "Write N iteration \n";
        cin >> iterator;
        cout << "Write " << to_string(iterator) << " numbers\n";
        for (int i = 0; i < iterator; i++)
        {
            int number = 0;
            cin >> number;
            numbers.push_back(number);
        }
    }
    void Calculate() override
    {
        int countPositiveNumber = 0;
        for (int num : numbers)
        {
            if (num > 0)
                countPositiveNumber++;
        }
        result = to_string(countPositiveNumber);
    }
    string OutputResult() override
    {
        return "Result: " + result;
    }
    string GetName() override
    {
        return "Task6Extra Positive value";
    }
};

class Task7 : public AbstractTask
{
    string result;
    int iterator;
    int numberUP;
    vector<int> numbers;
public:
    void Input() override
    {
        cout << "Write N iteration \n";
        cin >> iterator;
        cout << "Write " << to_string(iterator) << " numbers\n";
        string s_numbers;
        cin >> ws;
        getline(cin , s_numbers);
        std::stringstream stream;
        stream << s_numbers;
        string numberLoc;
        while (iterator > 0 && stream >> numberLoc)
        {
            numbers.push_back(stoi(numberLoc));
            iterator--;
        }
    }
    void Calculate() override
    {
        int countPositiveNumber = 0;
        for (int num : numbers)
        {
            if(num < 100 && num % 8 == 0)
                countPositiveNumber += num;
        }
        result = to_string(countPositiveNumber);
    }
    string OutputResult() override
    {
        return "Result: " + result;
    }
    string GetName() override
    {
        return "Task7 Sum number ** % 8";
    }
};
class Task7Extra : public AbstractTask
{
    int numberResult;
    int iterator;
    std::vector<int> numbers;
public:
    void Input() override
    {
        cout << "Write N iteration \n";
        cin >> iterator;
        cout << "Write " << to_string(iterator) << " numbers\n";
        for (int i = 0; i < iterator; i++)
        {
            int number = 0;
            cin >> number;
            numbers.push_back(number);
        }
    }
    void Calculate() override
    {
        int minNumber = numeric_limits<int>::min();

        int maxNumber = minNumber;

        if (iterator == 0)
        {
            numberResult = -1;
            return;
        }
        for (int i = 0; i < numbers.size(); i++)
        {
            if (numbers[i] > minNumber)
            {
                minNumber = numbers[i];
            }
        }
        if (minNumber == maxNumber)
        {
            numberResult = -1;
            return;
        }
        int countMin = 0;
        for (int i = 0; i < numbers.size(); i++)
        {
            if (numbers[i] == minNumber)
            {
                countMin++;
            }
        }
        if (countMin == 0)
        {
            numberResult = -1;
            return;
        }
        numberResult = countMin;
        numbers.clear();
    }
    string OutputResult() override
    {
        return "Result: " + std::to_string(numberResult);
    }
    string GetName() override
    {
        return "Task3Extra Max count";
    }
};

class Task8 : public AbstractTask
{
    string result;
    string numberUP;
    string numberDown;

public:
    void Input() override
    {
        int iterator = 2;
        cout << "Write " << to_string(iterator) << " numbers\n";
        string s_numbers;
        cin >> ws;
        getline(cin, s_numbers);
        std::stringstream stream;
        stream << s_numbers;
        stream >> numberUP;
        stream >> numberDown;

    }
    void Calculate() override
    {
        result = "";
        vector<char> repetitive;
        for (char x : numberUP)
        {
            for (char y : numberDown)
            {
                bool isCount0 = find(repetitive.begin(), repetitive.end(), x) == repetitive.end();
                if (y == x && isCount0) repetitive.push_back(x);
            }
        }
        for (char t : repetitive)
        {
            result += " " + to_string((t - '0'));
        }
    }
    string OutputResult() override
    {
        return "Result: " + result;
    }
    string GetName() override
    {
        return "Task8 Repetitive numbers";
    }
};
class Task8Extra : public AbstractTask
{
    string result;
    vector<vector<int>> s_numbers;
    int iterator = 0;

public:
    void Input() override
    {
        cout << "Write range duble Array\n";
        cin >> iterator;
        
        for (int i = 0; i < iterator; i++)
        {
            string locS;
            cout << "Write " << to_string(iterator) << " numbers Separated by a space Array\n";
            cin >> ws;
            getline(cin, locS);
            std::stringstream stream;
            stream << locS;
            string number;
            int index = 0;
            locS = "";
            vector<int> localVect;
            while (stream >> number && index < iterator)
            {
                localVect.push_back(stoi(number));
                index++;
            }
            if (index < iterator)
            {
                cout << "Error: Incorrect number of numbers in the array";
                cout << "Try again";
                localVect.clear();
                i = -1;
                continue;
            }
            s_numbers.push_back(localVect);
        }
    }
    void Calculate() override
    {
        result = "";
        Vector2 vect(iterator, iterator);
        InfoCurve curve(vect);
        for (int i = 0; i < vect.MultyplyXY(); i++)
        {
            Vector2 vect;
            vect = curve.GetValue(i);
            result += " " + to_string(s_numbers[vect.X()][vect.Y()]);
        }
    }
    struct InfoCurve
    {
        Vector2 max;
        int left;
        int right;
        int top;
        int buttom;
        vector<Vector2> positionsCurve;
        void CalculatePositions()
        {
            while (positionsCurve.size() < max.MultyplyXY())
            {
                for (int y = left; y < right; y++)
                {
                    Vector2 vect(top, y);
                    positionsCurve.push_back(vect);
                }
                for (int x = top; x < buttom; x++)
                {
                    Vector2 vect(x, right);
                    positionsCurve.push_back(vect);
                }
                for (int y= right; y >= left; y--)
                {
                    Vector2 vect(buttom,y);
                    positionsCurve.push_back(vect);
                }
                for (int x = buttom - 1; x > top; x--)
                {
                    Vector2 vect(x, left);
                    positionsCurve.push_back(vect);
                }
                top++;
                buttom--;
                left++;
                right--;
            }
        }
        public:
            InfoCurve(Vector2 _vector2)
            {
                max = _vector2;
                left = 0;
                right = _vector2.X() - 1;
                top = 0;
                buttom = _vector2.Y() - 1;
                CalculatePositions();
            }
            Vector2 GetValue(int t)
            {
                if (positionsCurve.size() <= t)
                {
                    Vector2 vect;
                    return vect;
                }
                return positionsCurve[t];
            }

    };
    string OutputResult() override
    {
        return "Result: " + result;
    }
    string GetName() override
    {
        return "Task8Extra Curve Array numbers";
    }
};

class Task9 : public AbstractTask
{
    string result;
    Vector2 vect1;
    Vector2 vect2;

public:
    void Input() override
    {
        int iterator = 4;
        cout << "Write " << to_string(iterator) << " numbers to Create 2 Point\n";
        string s_numbers;
        cin >> ws;
        getline(cin, s_numbers);
        std::stringstream stream;
        stream << s_numbers;
        int X, Y;
        stream >> X;
        stream >> Y;
        Vector2 vect(X, Y);
        vect1 = vect;
        stream >> X;
        stream >> Y;
        Vector2 vectk(X, Y);
        vect2 = vectk;
    }
    void Calculate() override
    {
        result = "Distance: " + to_string(vect1.GetDistance(vect2));
    }
    string OutputResult() override
    {
        return "Result: " + result;
    }
    string GetName() override
    {
        return "Task9 Cpeater Point and distance";
    }
};
class Task9_1 : public AbstractTask
{
    class Person
    {
        string first_name;

        string last_name;

        int age;
    public:
        Person(string _first_name, string _last_name, int _age)
        {
            first_name = _first_name;
            last_name = _last_name;
            age = _age;
        }
        string GetFullName()
        {
            return "<" + first_name + "> <" + last_name + ">";
        }
        string IsAduit()
        {
            return age > 18 ? "True" : "False";
        }

    };
    string result;

public:
    void Input() override
    {
        Person kamil("Kamil", "Sadreev", 22);
        Person milana("Milana", "Sadreeva", 6);
        cout << "Full name KamilPerson: " << kamil.GetFullName() << endl;
        cout << "IsAduit: " << kamil.IsAduit() << endl;
        cout << "Full name MilanaPerson: " << milana.GetFullName() << endl;
        cout << "IsAduit: " << milana.IsAduit() << endl;
    }
    string GetName() override
    {
        return "Task9_1 Cpeater Person";
    }
};
class Task9Extra : public AbstractTask
{
    string result;
    class Laptop
    {
        string first_name;

        string last_name;

        int prise;
    public:
        Laptop(string _first_name, string _last_name, int _prise)
        {
            first_name = _first_name;
            last_name = _last_name;
            prise = _prise;
        }
        string GetFullName()
        {
            return first_name + " " + last_name;
        }
        int GetPrice()
        {
            return prise;
        }

    };

public:
    void Input() override
    {
        Laptop hp("hp", "15-bw0xx", 57000);
        cout << "Full name Laptop: " << hp.GetFullName() << endl;
        cout << "Price: " << to_string(hp.GetPrice()) << endl;
    }
    string GetName() override
    {
        return "Task9Extra Cpeater Laptop";
    }
};
class Task10 : public AbstractTask
{
    enum Role
    {
        Admin, Teacher, Student
    };
    struct Homework
    {
        string title;
        string discription;
        string content;
        string answer;
    };
    struct User
    {
        vector<Homework> homevorks;
        User(Role role, string last_name, string first_name,
            string login, string hashPassword)
        {
            this->role = role;
            this->last_name = last_name;
            this->first_name = first_name;
            this->hashPassword = hashPassword;
            this->login = login;
        }
        bool IsAdmin()
        {
            return role == Role::Admin;
        }
        bool IsTeacher()
        {
            return role == Role::Teacher;
        }
        string GetInfo()
        {
            string str;
            str += to_string(role) + "\n";
            str += last_name + "\n";
            str += first_name + "\n";
            str += hashPassword + "\n";
            str += login + "\n";
            return str;
        }
        static string GetHash(string password)
        {
            hash<string> mystdhash;
            return to_string(mystdhash(password));
        }
    private:
        Role role;
        string last_name;
        string first_name;
        string login;
        string hashPassword;
    };
    struct Group
    {
        string name;
        vector<User> users;
    };
    
public:
    void Input() override
    {
        User user(Role::Student, "lastName", "firstName", "LaLa@gmail.com", User::GetHash("qwerty"));
        cout << user.GetInfo();
    }
    string GetName() override
    {
        return "Task10";
    }
};