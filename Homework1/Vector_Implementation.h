#include <iostream>
#include <vector>
#include <exception>

#ifndef CUSTOM_VECTOR
#define CUSTOM_VECTOR
class Evec
{
public:
    std::vector<float> container;
    int row; //0 if column vector, 1 if row vector
    Evec(){row = 0;}
    Evec(int, int);
    friend float inner_product(const Evec& a,const Evec& b);
    friend Evec operator^(const Evec&b, char a);
    float l2_norm() const;
    void operator=(Evec& a);
    void Print();
};

Evec::Evec(int a, int b)
{
    
    if(a == 1)
    {
        container.resize(b);
        container.clear();
        row = 1;
    }
    else if((a * b) == 0 )
    {
        container.resize(1);
    }
    else
    {
        container.resize(a);
        container.clear();
        row = 0;
    }
}

float Evec::l2_norm() const
{
    float sum = 0;
    for(int i = 0; i < (int)container.size(); i++)
    {
        sum += (container[i]) * (container[i]);
    }
    float inner_Prod = sqrt(sum);
    return inner_Prod;
}

void Evec::operator=(Evec& a)
{
    container = a.container;
    row = a.row;
}

Evec operator^(const Evec&b, char a)
{
    Evec B;
    if(a == 'T')
    {
        B.container = b.container;
        if(b.row)
        {
            B.row = 0;
        }
        else
        {
            B.row = 1;
        }
    }
    return B;
}

void Evec::Print()
{
    if(row)
    {
        std::cout << "[ ";
        for(int i = 0; i < (int)container.size(); i++)
        {
            std::cout << container[i];
            if(i != (int)(container.size() - 1))
            {
                std::cout << ", ";
            }
        }
        std::cout << " ]" << std::endl;
    }
    else
    {
        for(int i = 0; i < (int)container.size(); i++)
        {
            if(i == 0)
            {
                std::cout << "|‾" << container[i] << "‾|" << std::endl;
            }
            else if(i == ((int)container.size()-1))
            {
                std::cout << "|_" << container[i] << "_|" << std::endl;
            }
            else
            {
                std::cout << "| " << container[i] << " |" << std::endl;
            }
        }
    }
}

float inner_product(const Evec& a, const Evec& b)
{
    float inner_prod = 0;
    int trans = a.row * b.row;
    if(a.container.size() != b.container.size())
    {
        throw std::logic_error("Dimention Mismatch");
    }
    switch(trans)
    {
        case 0:
            for(int i = 0; (i < (int)a.container.size()); i++)
            {
                inner_prod += a.container[i] * b.container[i];
            }
            break;
        
        case 1:
            Evec b_T = b^'T'; 
            inner_product(a, b_T);
            break;
    }
    return inner_prod;
}
#endif