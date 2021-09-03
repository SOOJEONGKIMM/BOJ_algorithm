#include<iostream>
#include<algorithm>
using namespace std;
const int MAX=1000+1;
int main(){
	int N, L;
	cin>>N>>L;
	int leak[1000]={0,};
	for(int i=0;i<N;i++)
		cin>>leak[i];
		
	sort(leak, leak+N);
	
	int start = leak[0];
	int end = leak[0]+L;
	int tape =1;
	
	for(int i=0;i<N;i++){
		if(start<=leak[i]&&leak[i]<end)
			continue;
		if(end>1000)
			continue;
		else{
			start = leak[i];
			end = leak[i]+L;
			tape++;
		}
	}
	
	cout<<tape;
		
}
