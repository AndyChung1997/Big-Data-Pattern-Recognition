#include <iostream>
#include <cstdlib>
#include <ctime>
#include <math.h>
#include <random>

using namespace std;

int main(){

  random_device rd;  //�ϥβ��ͪ��üƨӰ����üƺؤl
  mt19937 generator( rd() );  //�üƲ��;�: ���˱���t��k

  int a;  //�X�{���������v
  cout << "�X�{���������v: " ;
  cin >> a;
  double p = a*0.01;

  cout << "�Y�w������: ";
  int n ;  //�Y�w������
  while(cin >> n && n > 0)
  {
      double mean = n * p;  //������
      double std9 = sqrt((n*p)*(1-p));   //�зǮt

      /* �`�A������� */
  normal_distribution<double> norm(mean, std9); //(�����,�зǮt) �A ��m�Ѽ�(�M�w�F��������m)�P�ثװѼ�(�M�w�F�������T��)

   /* �`�A�����üƪ���� */
    int r[n+1]={};
    srand( time(NULL) );  //�T�w�üƺؤl
    int m = 0 ,y = 1;

    //���ժ�����n
    cout << "n: " ;
    int quiz;
    cin >> quiz;
    cout << endl;
    for (int i=0; i < quiz; ++i) {
    double x = norm(generator);
    if ((x >= 0.0) && (x <= n)) ++r[int(x)]; //�p��

    int pr = x;  // �X�{����������
    //cout << "��" << i+1 << "�����յ��G:" << endl;

        int test1 = 0, test2 = 0;
        while((test1+test2) != n){

            int num = rand() % (y - m + 1) + m;  /* ���� [0 , 1] ����ƶü� */
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
        //cout << "���� : " << test1 << "���A���v : " << test1 << "/" << n << endl;
        //cout << "�ϭ� : " << test2 << "���A���v : " << test2 << "/" << n << endl;
     }

    cout << "�X�{����������: " << endl;

    FILE *fp = NULL;
    fp = fopen("D:\\test4.xls","w");

    for (int i=0; i<=n; ++i) {
    cout << i << "��: ";
    cout << string(r[i], '*') << "        " << "���v: " << r[i] << "/" << quiz << endl;

    fprintf(fp,"%d\t%d\n",i,r[i]);
    }
    fclose(fp);
    cout << "�Y�w������: ";
  }


  return 0;

}
