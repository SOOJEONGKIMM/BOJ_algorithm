#include <iostream>
#include <vector>
using namespace std;

void DFS(vector<int> *graph, bool *visited, int node){
	visited[node]=true;
	for(int i=0;i<graph[node].size();i++){
		int next = graph[node][i];
		cout<<"node"<<node<<"next"<<next;
		if(visited[next]==false){		
			DFS(graph,visited,next);
		}
	}
}

int main(){
	int node, edge;
	cin>>node>>edge;
	vector<int> graph[node+1];
	
	for(int i=0;i<edge;i++){
		int n1, n2;
		cin>>n1>>n2;
		graph[n1].push_back(n2);
		graph[n2].push_back(n1);
	}
	
	bool visited[node+1]={false};
	int comp = 0;
	for(int i=1;i<=node;i++){
		if(visited[i]==false){
			DFS(graph,visited,i);
			comp += 1;	
		}
	}
	
	cout<<comp;
}
