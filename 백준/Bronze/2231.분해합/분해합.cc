#include<bits/stdc++.h>
using namespace std;
int n,a,b,c,x=1;
int main()
{
	cin>>n;
	for(int i=max(0,n-54);i<n;i++)
	{
		c=i;
		a=0;
		for(int l=0;l<6;l++)
		{
			a+=c%10;
			c=c/10;
			
		}
		if(a+i==n)
		{
			cout<<i;
			x=0;
			break;
		}
	}
	if(x)
		cout<<0;
}