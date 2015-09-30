#include<stdio.h>
int main(){
    int R,N,i,num,j,m,count,next[1000],pointer;
    long long rec[1000],K,sum,earn;
    long long accum[1000];
    scanf("%d",&num);
    for(i=0;i<num;i++){
        scanf("%d%lld%d",&R,&K,&N);
        for(j=0;j<N;j++){
            scanf("%lld",&rec[j]);
        }

        j=0;

        while(j<N){
            m=j;
            sum=0;
            count=0;
            while(1){
                if(m>=N)
                    m=0;
                if(count>=N){
                    next[j]=j;
                    break;
                }
                sum+=rec[m];
                if(sum>K){
                    next[j]=m;
                    break;
                }
                accum[j]=sum;
                m++;
                count++;
            }
            j++;
        }
        j=0;
        earn=0;
        pointer=0;
        while(j<R){
            earn+=accum[pointer];
            pointer=next[pointer];
            j++;
        }
        /*	for(j=0;j<N;j++)
            printf("%d ",next[j]);
            printf("\n");*/
        printf("Case #%d: %lld\n",i+1,earn);
    }
    return 0;
}
