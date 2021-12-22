#include <bits/stdc++.h>
using namespace std;

long long findM(string &S, long long L, long long R){
    if(S[L + 1] == '?'){
        long long M = L + 2;
        return M;
    }
    else{
        long long count1 = 1;
        long long count2 = 0;
        
        long long p = L + 2;
        
        while(count1 != count2){
            if(S[p] == '('){
                count1++;
            }
            else if(S[p] == ')'){
                count2++;
            }
            p++;
        }
        long long M = p;
        return M;
    }
}

long long solve(string &S, long long L, long long R, long long tag, map<tuple<long long, long long, long long>, long long> &m){
    tuple<long long, long long, long long> tempt = make_tuple(L, R, tag);
    auto itr = m.find(tempt);
    if(itr != m.end()){
        return itr->second;
    }
    
    if(S[L] == '?'){
        if(tag == 1){
            return 1;
        }
        else{
            return 0;
        }
    }
    
    long long M = findM(S, L, R);
    
    long long temp1 = solve(S, L + 1, M - 1, 1, m);
    tuple<long long, long long, long long> t1 = make_tuple(L + 1, M - 1, 1);
    m[t1] = temp1;
    
    long long temp2 = solve(S, M + 1, R - 1, 1, m);
    tuple<long long, long long, long long> t2 = make_tuple(M + 1, R - 1, 1);
    m[t2] = temp2;
    
    long long temp3 = solve(S, L + 1, M - 1, 0 ,m);
    tuple<long long, long long, long long> t3 = make_tuple(L + 1, M - 1, 0);
    m[t3] = temp3;
    
    long long temp4 = solve(S, M + 1, R - 1, 0, m);
    tuple<long long, long long, long long> t4 = make_tuple(M + 1, R - 1, 0);
    m[t4] = temp4;
    
    if(S[M] == '+'){
        if(tag == 1){
            return m.find(t1)->second + m.find(t2)->second;
        }
        else{
            return m.find(t3)->second + m.find(t4)->second;
        }
    }
    else{
        if(tag == 1){
            return m.find(t1)->second - m.find(t4)->second;
        }
        else{
            return m.find(t3)->second - m.find(t2)->second;
        }
    }
    
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	// your code goes here
	long long t;
	cin >> t;
	while(t--){
	    
	    map<tuple<long long, long long, long long>, long long> m;
	    
	    string S;
	    cin >> S;
	    long long Q;
	    cin >> Q;
	    
	    tuple<int, int, int> xt = make_tuple(0, S.size() - 1, 1);
	    int xtt = solve(S, 0, S.size() - 1, 1, m);
	    
	    m[xt] = xtt;
	    
	    while(Q--){
	        long long L, R;
	        cin >> L >> R;
	        cout << m.find(make_tuple(L - 1, R - 1, 1))->second << " ";
	        
	    }
	    cout << "\n";
	}
	return 0;
}
