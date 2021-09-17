#include<iostream>
#include<algorithm>
using namespace std;
int tri[501][501]={0,};
int arr[501][501]={0,};
int main(){
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=i;j++){
			cin>>tri[i][j];
		}
	}
	
	int res=0;
	for (int i = 1; i <=n; i++) {
		for (int j =1; j <=n; j++) {
			arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j]) + tri[i][j];
			res = max(res, arr[i][j]);
		}
	}
	cout << res;




}
