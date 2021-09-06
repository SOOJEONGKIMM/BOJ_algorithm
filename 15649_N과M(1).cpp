#include<iostream>
using namespace std;
#define MAX 8

int N, M;
int arr[MAX+1];
bool visited[MAX+1]={false};
void permutation(int cnt){
	
	if(cnt==M){	
		for(int i=0;i<M;i++){
			cout<<arr[i]<<" ";
		}
		cout<<"\n";
		return;
	}
	for(int i=1;i<=N;i++){
		if(!visited[i]){
			visited[i]=true;
			arr[cnt]=i;
			permutation(cnt+1);
			visited[i]=false;
		}
	}
	
}
int main(){
	const int cnt=0;
	cin>>N>>M;
	
	permutation(cnt);
	return 0;
}
