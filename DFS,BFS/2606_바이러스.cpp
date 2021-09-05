#include<iostream>
#include<vector>
using namespace std;
int cnt=0;
void DFS(vector<int> *graph, bool *visited, int node){
	visited[node]=true;
	for(int i=0;i<graph[node].size();i++){
		int next = graph[node][i];
		
		if(visited[next]==false){
			DFS(graph, visited, next);
			cnt+=1;
		}	
	}
}
int main(){
	int node, C;
	cin>>node>>C;
	vector<int> graph[node+1];
	
	for(int i=0;i<C;i++){
		int n1, n2;
		cin>>n1>>n2;
		graph[n1].push_back(n2);
		graph[n2].push_back(n1);
	}
	
	bool visited[node+1]={false};
	DFS(graph,visited,1);
	
	cout<<cnt;
	
}
