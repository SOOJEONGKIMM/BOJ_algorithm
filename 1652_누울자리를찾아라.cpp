#include <iostream>
using namespace std;

int main(){
	int n;
	cin>>n;
	char room[n][n];

	int w=0,h=0;
	for(int i=0;i<n;i++){
			cin >> room[i];

	}

	for(int i=0;i<n;i++){
		int cnt_h = 0;	
		int first_h = 0;
		int cnt_w = 0;	
		int first_w = 0;
		for(int j=0;j<n;j++){
			if(room[j][i]=='.')
				cnt_h ++;
			if(cnt_h==2){
				if(!first_h)
					h++;
				first_h = 1;
				cnt_h = 0;
			}			
			else if(room[j][i]=='X'){
				cnt_h = 0;
				first_h = 0;
			}



			if(room[i][j]=='.')
				cnt_w ++;
			if(cnt_w==2){
				if(!first_w)
					w++;
				first_w = 1;
				cnt_w = 0;	
			}
			else if(room[i][j]=='X'){
				cnt_w = 0;
				first_w = 0;
			}
		
	
		}
	}
	
	cout<<w<<' '<<h<<'\n';

	
}
