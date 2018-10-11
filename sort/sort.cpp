#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    int len = 10000;
    if (argc > 1)
    {
        len = atoi(argv[1]);
    }
    int *unsort_arr = new int[len];
    srand(time(NULL));
    for (int i = 0; i < len; i++)
    {
        unsort_arr[i] = rand();
    }

    int start = time(NULL);
    for (int i = 1; i < len; i++)
    {
        int key = unsort_arr[i];
        int j = i - 1;
        for (; j >= 0 && unsort_arr[j] > key; j--)
        {
            unsort_arr[j + 1] = unsort_arr[j];
        }
        unsort_arr[j + 1] = key;
    }
    int end = time(NULL);

    // for (int i = 0; i < len; i++)
    // {
    //     cout << unsort_arr[i] << " ";
    // }
    // cout << endl;

    cout << end - start << endl;

    return 0;
}