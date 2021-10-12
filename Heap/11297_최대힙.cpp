//11297_ÃÖ´ëÈü
#include<stdio.h>
#include<iostream>
#include<queue>
using namespace std;
int N;
priority_queue <int> pq;
int main(){
	cin.sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cin>>N;
	while(N--){
		int num;
		cin>>num;
		if(num==0){
			if(pq.empty())
				cout<<"0\n";
			else{
				cout<<pq.top()<<"\n";
				pq.pop();
			}
		}
		else
			pq.push(num);
	}
	return 0;
}
