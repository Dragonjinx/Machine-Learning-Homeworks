#include <iostream>
#include <vector>
#include <exception>
#include <algorithm>
#include "Vector_Implementation.h"

// Have Problems when copying a vector from a vector array into anhother vector

class Matrix
{
public:
    std::vector<std::vector<float>> Array;
    int Rows; // Number of vectors in Array
    int Columns; // Number of elements in vector

    Matrix();
    Matrix(int rows, int columns, bool input = false); // Constructor is fine
    friend Matrix matrix_prod(const Matrix a,const  Matrix b); // Problems when copyting
    friend Matrix matrix_prod(const Matrix a,const  Evec b); // Problems when copying
    friend Matrix operator^(const Matrix a, char b);
    friend Matrix operator*(float a, Matrix b);
    friend Matrix operator*(Matrix b, float a);
    void operator=(const Matrix a); // ASsignment is fine
    void Print();
};


Matrix::Matrix()
{
    Rows = 0;
    Columns = 0;
    Array.resize(1);
}

Matrix::Matrix(int rows, int columns, bool input)
{
    Rows = rows;
    Columns = columns;
    Array.resize(Rows);
    Array.clear();
    for(int i = 0; i < Rows; i++)
    {
        Array[i].resize(Columns);
        Array[i].clear();
    }
    if (input == true)
    {
        std::cout << "You have a " << Rows << " x " << Columns << " matrix" << std::endl;
        for (int i = 0; i < Rows; i++)
        {
            std::cout << "Enter values for row: " << i + 1 << std::endl;
            float value;
            for (int j = 0; j < Columns; j++)
            {
                scanf("%f", &value);
                getchar();
                Array[i][j] = value;
            }
        }
        std::cout << "Entry Successful" << std::endl;
    }
}

Matrix matrix_prod(const Matrix a,const  Matrix b)
{
    if(a.Columns != b.Rows)
    {
        throw std::logic_error("Dimention Mismatch");
    }
    Matrix Output(a.Rows, b.Columns, false);
    Evec rowA;
    rowA.row = 1;
    Evec colB;
    for(int i = 0; i < a.Rows; i++)
    {
        rowA.container = a.Array[i];
        
        for(int j = 0; j < b.Columns; j++)
        {
            for(int K = 0; K < b.Rows; K++)
            {
                colB.container[K] = b.Array[K][j];
            }
            Output.Array[i][j] = inner_product(rowA, colB);
        }
    }
    return Output;
}

Matrix matrix_prod(const Matrix a,const  Evec b)
{
    if(b.row == 1)
    {
        Matrix Row(1, b.container.size());
        Row.Array[1] = b.container;
        return matrix_prod(a, Row);
    }
    else
    {
        Matrix Col(b.container.size(), 1, false);
        for (int i = 0; i < Col.Rows; i++)
        {
            Col.Array[i][1] = b.container[i];
        }
        return matrix_prod(a, Col);
    }
}

Matrix operator*(float a, Matrix b)
{
    Matrix Ret;
    Ret = b;
    for(int i = 0; i < Ret.Rows; i++)
    {
        for(int j  = 0; j < Ret.Columns; j++)
        {
            Ret.Array[i][j] = a;
        }
    }
    return Ret;
}

Matrix operator*(Matrix b, float a)
{
    return a * b;
}


void Matrix::operator=(const Matrix a)
{
    Array = a.Array;
    Rows = a.Rows;
    Columns = a.Columns;
}

Matrix operator^(const Matrix a, char b)
{
    Matrix A;
    A.Rows = a.Columns;
    A.Columns = a.Rows;
    A.Array.resize(A.Rows);
    if(b == 'T')
    {
        for(int i = 0; i < a.Rows ; i++)
        {
            for(int j = 0; j < a.Columns; j++)
            {
                A.Array[j].resize(A.Columns);
                A.Array[j][i] = a.Array[i][j];
            }
        }
    }
    return A;
}

void Matrix::Print()
{
    for(int i = 0; i < Rows; i++)
    {
        if(i == 0)
        {
            std::cout << "|‾";
            for(int j = 0; j < Columns; j++)
            {
                std::cout << Array[i][j];
                if(j < Columns-1)
                {
                    std::cout << " ";
                }
            } 
            std::cout << "‾|" << std::endl;
        }
        else if(i == (Rows-1))
        {
            std::cout << "|_";
            for(int j = 0; j < Columns; j++)
            {
                std::cout << Array[i][j];
                if(j < Columns-1)
                {
                    std::cout << " ";
                }
            } 
            std::cout << "_|" << std::endl;
        }
        else
        {
            std::cout << "| "; 
            for(int j = 0; j < Columns; j++)
            {
                std::cout << Array[i][j];
                if(j < Columns-1)
                {
                    std::cout << " ";
                }
            }
            std::cout<<" |" << std::endl;  
        }
    }
}