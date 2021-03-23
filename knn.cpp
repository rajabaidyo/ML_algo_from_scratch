// code for basic KNN with c++
//run command => g++ -std=c++11 knn.cpp -o t && ./t
#include<vector>
#include<math.h>
#include<iostream>
#include<queue>
#include<algorithm>
using namespace std;
vector<vector<float> > dataset{
    {1,3,0},
    {2,4,0},
    {4,4,0},
    {1.25,5.6,0},
    {4.5,8,1},
    {4.1,3.4,0},
    {9,7.4,1},
    {10,11.34,1},
    {5,5,1},
    {6,6,1},
    {4.4,4.2,1},
    {4.1,4.1,1},
    {5.0,4.3,1},
    {5.6,5.5,1},
    {7,7,1},
    {9,8,1},
    {1,1,0},
    {2,2,0},
    {2.2,3.4,0},
    {8,8,1}
};
float ed(float x, float y , vector<float> &tmp){
    return sqrt((tmp[0]-x)*(tmp[0]-x)+(tmp[1]-y)*(tmp[1]-y));
}
void knn(float x,float y,vector<vector<float> > &list){
    float dis;
    vector<float> temp;
    for(int i=0;i<dataset.size();i++){
        dis=ed(x,y,dataset[i]);
        temp.push_back(dataset[i][0]);
        temp.push_back(dataset[i][1]);
        temp.push_back(dataset[i][2]);
        temp.push_back(dis);
        list.push_back(temp);
        temp.clear();
    }
}
bool comp(vector<float> &a,vector<float> &b){
    return a[3]<b[3];
}
int grouping(vector<vector<float> > &list, int &k){
    sort(list.begin(),list.end(),comp);
    int count=0;
    for(int i=0;i<k;i++){
        if(0==int(list[i][2])) count++;
    }
    if(count>=3) return 0;
    return 1;
}
int main(){
    while(true){
        cout << "Put the input => ";
        int k=5;
        float x,y; cin >> x >> y;
        vector<vector<float> > list;
        knn(x,y,list);
        int result = grouping(list,k);
        vector<float> temp;
        temp.push_back(x); temp.push_back(y); temp.push_back(float(result));
        dataset.push_back(temp);
        temp.clear();
        cout << "The predicted class of the input is => " << result << endl;
        cout << "Do u want to continue testing with KNN?" << endl;
        cout << "Press 1 for YES 0 for NO" << endl;
        int stop; cin >> stop; if(stop==0) break;
    }
    return 0;
}
