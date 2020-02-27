#include <iostream>
#include <cmath>
#include "Matrix_Implementation.h"

int main()
{
    char T = 'T'; 
    Evec a(1,3);
    Evec b(3,1);
    Matrix M(4, 4);
    Matrix A(1, 1, true);
    a.container.push_back(1);
    a.container.push_back(1);
    a.container.push_back(0);
    b.container.push_back(-1);
    b.container.push_back(2);
    b.container.push_back(5);
    int K = 1;
    for(int i = 0; i < M.Rows; i++)
    {
        for(int j = 0; j < M.Columns; j++)
        {
            M.Array[i][j] = K;
            K++;
        }
    }
    M.Print();
    a.Print();
    b.Print();
    std::cout << "aT b inner prod:  " << inner_product(a^T, b) << std::endl;
    std::cout << "Norm of a: " << a.l2_norm() <<std::endl;
    std::cout << "(aT b)MaT: " <<std::endl;
    // M = A;
    M = matrix_prod(M, M);
    M.Print();
    return 0;
}