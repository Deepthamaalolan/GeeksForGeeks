#include <bits/stdc++.h> 
using namespace std; 
bool hasEvenNumberOfFactors(int n) 
{ 
    int root_n = sqrt(n);
    if ((root_n*root_n) == n) 
        return false; 
     return true; 
} 
  
void StatusOfDoors(int n) 
{ 
    for (int i=1; i<=n; i++) 
    { 
        if (hasEvenNumberOfFactors(i)) 
            cout << "closed" << " ";
        else
            cout << "open" << " "; 
    } 
} 
   
int main() 
{ 
    int n = 5; 
    StatusOfDoors(n); 
    return 0; 
} 
