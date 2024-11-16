#include <iostream> 

struct Vector2
{
    Vector2(int X, int Y)
    {
        x = X; y = Y;
    }
    Vector2()
    {
        x = y = 0;
    }
    int Y()
    {
        return y;
    }
    int X()
    {
        return x;
    }
    int MultyplyXY()
    {
        return x * y;
    }
    int GetDistance(Vector2 vect)
    {
        return sqrt((pow(vect.x - x, 2) + pow(vect.y - y, 2)));
    }
private:
    int x, y;
};