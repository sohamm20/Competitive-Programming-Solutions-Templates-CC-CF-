#include <bits/stdc++.h>
#include <stack>
#include <stdlib.h>
using namespace std;

vector<pair<int, int>> glob;

void combinationUtil(int arr[], int data[],
                    int start, int end,
                    int index, int r);
 

void printCombination(int arr[], int n, int r)
{
    int data[r];
    combinationUtil(arr, data, 0, n-1, 0, r);
}
void combinationUtil(int arr[], int data[],
                    int start, int end,
                    int index, int r)
{
    if (index == r)
    {
        glob.push_back(make_pair(data[0], data[1]));
        return;
    }
    for (int i = start; i <= end &&
        end - i + 1 >= r - index; i++)
    {
        data[index] = arr[i];
        combinationUtil(arr, data, i+1,
                        end, index+1, r);
    }
}

struct Point
{
	double x, y;
};

Point p0;


Point nextToTop(stack<Point> &S)
{
	Point p = S.top();
	S.pop();
	Point res = S.top();
	S.push(p);
	return res;
}

void swap(Point &p1, Point &p2)
{
	Point temp = p1;
	p1 = p2;
	p2 = temp;
}

double distSq(Point p1, Point p2)
{
	return (p1.x - p2.x)*(p1.x - p2.x) +
		(p1.y - p2.y)*(p1.y - p2.y);
}

int orientation(Point p, Point q, Point r)
{
	double val = (q.y - p.y) * (r.x - q.x) -
			(q.x - p.x) * (r.y - q.y);

	if (val == 0) return 0; // collinear
	return (val > 0)? 1: 2; // clock or counterclock wise
}

int compare(const void *vp1, const void *vp2)
{
Point *p1 = (Point *)vp1;
Point *p2 = (Point *)vp2;

int o = orientation(p0, *p1, *p2);
if (o == 0)
	return (distSq(p0, *p2) >= distSq(p0, *p1))? -1 : 1;

return (o == 2)? -1: 1;
}

void convexHull(auto points, int n)
{

double ymin = points[0].y, min = 0;
for (int i = 1; i < n; i++)
{
	double y = points[i].y;
	
	if ((y < ymin) || (ymin == y &&
		points[i].x < points[min].x))
		ymin = points[i].y, min = i;
}

swap(points[0], points[min]);
p0 = points[0];
qsort(&points[1], n-1, sizeof(Point), compare);

int m = 1; // Initialize size of modified array
for (int i=1; i<n; i++)
{
	
	while (i < n-1 && orientation(p0, points[i],
									points[i+1]) == 0)
		i++;


	points[m] = points[i];
	m++;
}

if (m < 3) return;

stack<Point> S;
S.push(points[0]);
S.push(points[1]);
S.push(points[2]);


for (int i = 3; i < m; i++)
{

	while (S.size()>1 && orientation(nextToTop(S), S.top(), points[i]) != 2)
		S.pop();
	S.push(points[i]);
}
cout << S.size() << '\n';
}

Point midp(Point a, Point b){
    Point tempt = {(double(a.x + b.x) / 2), double((a.y + b.y) / 2)};
    return tempt;
}

int main(){
	
	int t;
	cin >> t;
	for(int T = 0; T < t; T++){
	    
	    glob.clear();
	    
	    int N;
	    cin >> N;
    	
    	vector<Point> mid;
    	
    	for(int i = 0; i < N; i++){
    	    double soham, mirikar;
    	    cin >> soham >> mirikar;
    	    
    	    Point temp = {soham, mirikar};
    	    mid.push_back(temp);
    	    
    	}
    	
        int r = 2;
        int arr[N];
        
        for (int j = 0; j < N; j++){
            arr[j] = j;
        }
        
        printCombination(arr, N, r);
        
        vector<Point> res;
        for (auto p : glob){
            res.push_back(midp(mid[p.first], mid[p.second]));
            // cout << p.first << " " << p.second << endl;
        }
    	
    	convexHull(res, res.size());
    	
	}
	
	return 0;
}
