#include<iostream>
#include<vector>
#include<cmath>
#define MAX 20
using namespace std;
int N;
int output=100*100;
bool visited[MAX+1]={false};
int arr[MAX+1][MAX+1]={0};
void startlink(int idx, int cnt){
	vector<int> cases_start;
	vector<int> cases_link;
	int start=0;
	int link=0;
	
	if(cnt==(N/2)){
		for(int i=0;i<N;i++){
			if(visited[i]==true)
				cases_start.push_back(i);
			else
				cases_link.push_back(i);
		}				
		for(int i=0;i<(N/2);i++){
			for(int j=0;j<(N/2);j++){
				start+=arr[cases_start[i]][cases_start[j]];
				link+=arr[cases_link[i]][cases_link[j]];
			}
		}
		if(abs(start-link)<output)
			output=abs(start-link);
		return;
	}
			
	for(int i=idx;i<N;i++){
		if(visited[i]){
			continue;
		}
		else{
			visited[i]=true;		
			startlink(i,cnt+1);
			visited[i]=false;
		}
		
	}
}
int main(){

	cin>>N;
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++)
			cin>>arr[i][j];
	}
	startlink(0,0);	
	cout<<output;	
}
