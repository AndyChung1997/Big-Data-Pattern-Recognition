#include <iostream>
#include <cstdlib>
#include <ctime>
#include <math.h>
#include <random>

using namespace std;

int main(){

  random_device rd;  //使用產生的亂數來做為亂數種子
  mt19937 generator( rd() );  //亂數產生器: 梅森旋轉演算法

  int a;  //出現正面的機率
  cout << "出現正面的機率: " ;
  cin >> a;
  double p = a*0.01;

  cout << "擲硬幣次數: ";
  int n ;  //擲硬幣次數
  while(cin >> n && n > 0)
  {
      double mean = n * p;  //平均值
      double std9 = sqrt((n*p)*(1-p));   //標準差

      /* 常態分布函數 */
  normal_distribution<double> norm(mean, std9); //(期望值,標準差) ， 位置參數(決定了分布的位置)與尺度參數(決定了分布的幅度)

   /* 常態分布亂數直方圖 */
    int r[n+1]={};
    srand( time(NULL) );  //固定亂數種子
    int m = 0 ,y = 1;

    //測試的次數n
    cout << "n: " ;
    int quiz;
    cin >> quiz;
    cout << endl;
    for (int i=0; i < quiz; ++i) {
    double x = norm(generator);
    if ((x >= 0.0) && (x <= n)) ++r[int(x)]; //計數

    int pr = x;  // 出現正面的次數
    //cout << "第" << i+1 << "次測試結果:" << endl;

        int test1 = 0, test2 = 0;
        while((test1+test2) != n){

            int num = rand() % (y - m + 1) + m;  /* 產生 [0 , 1] 的整數亂數 */
            if(num == 1 && test1 < pr)
            {
                //cout << "num = " << num << endl;
                test1 ++;

            }
            else if(num == 0 && test2 < n-pr)
            {
                //cout << "num = " << num << endl;
                test2 ++;

            }
        }
        //cout << "正面 : " << test1 << "次，機率 : " << test1 << "/" << n << endl;
        //cout << "反面 : " << test2 << "次，機率 : " << test2 << "/" << n << endl;
     }

    cout << "出現正面的次數: " << endl;

    FILE *fp = NULL;
    fp = fopen("D:\\test4.xls","w");

    for (int i=0; i<=n; ++i) {
    cout << i << "次: ";
    cout << string(r[i], '*') << "        " << "機率: " << r[i] << "/" << quiz << endl;

    fprintf(fp,"%d\t%d\n",i,r[i]);
    }
    fclose(fp);
    cout << "擲硬幣次數: ";
  }


  return 0;

}
