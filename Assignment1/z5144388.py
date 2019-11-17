import pandas as pd
import matplotlib.pyplot as plt

def question_1():
    print("--------------- question_1 ---------------")
    df1 = pd.read_csv('Olympics_dataset1.csv',skiprows =1,thousands=',')
    df2 = pd.read_csv('Olympics_dataset2.csv',skiprows =1,thousands=',')
    df1.columns = ['Country','summer_rubbish','summer_participation','summer_gold','summer_silver','summer_bronze','summer_total']
    to_drop = ['Number of Games the country participated in.1',
                'Gold.1',
                'Silver.1',
                'Bronze.1',
                'Total.1']
    df2.drop(to_drop,inplace=True,axis=1)
    df2.columns = ['Country','winter_ participation','winter_gold','winter_silver','winter_bronze','winter_total']
    df3 = pd.merge(df1,df2,on='Country')
    df3=df3.drop(df3.tail(1).index)
    # print(df3.head(5))
    print(df3[0:5].to_string(index=False))
    return df3
    


def question_2(df3):
    print("--------------- question_2 ---------------")
    df3['Country']=df3['Country'].str.extract(r'(\w.*(?=\())')
    df3['Country']=df3['Country'].str.strip()
    df3 = df3.set_index(['Country'])
    drop_columns=['summer_rubbish',
                'summer_total',
                'winter_total']
              

    df3.drop(drop_columns,inplace=True,axis=1)
    print(df3[0:5].to_string())
    return df3

def question_3(df3):
    print("--------------- question_3 ---------------")
    df3 = df3.dropna()
    print(df3[-10:].to_string())
    return df3


def question_4(df3):
    print("--------------- question_4 ---------------")
    max_gold_nb = df3['summer_gold'].max()
    max_gold_country_list=df3[df3.summer_gold==max_gold_nb].index.to_list()
    print(' '.join(max_gold_country_list))
    


def question_5(df3):
    print("--------------- question_5 ---------------")
    df=df3.copy()
    df['gold_difference'] = abs(df.summer_gold-df.winter_gold)
    max_gold_difference=df['gold_difference'].max()
    biggest_gold_difference_country_list=df[df.gold_difference==max_gold_difference].index.to_list()
    print(' '.join(biggest_gold_difference_country_list),int(max_gold_difference))


def question_6(df3):
    print("--------------- question_6 ---------------")
    df6=df3.copy()
    df6['total_of_medals']= df6[['summer_gold','summer_silver','summer_bronze','winter_gold','winter_silver','winter_bronze']].sum(axis=1)
    df6 = df6.sort_values(by='total_of_medals',ascending=False)
    print("--------------- Head5 ---------------")
    print(df6[0:5].to_string())
    print("--------------- Tail5 ---------------")
    print(df6[-5:].to_string())
    return df6


def question_7(df):
    print("--------------- question_7 ---------------")
    df['summer_medals']= df[['summer_gold','summer_silver','summer_bronze']].sum(axis=1)
    df['winter_medals']= df[['winter_gold','winter_silver','winter_bronze']].sum(axis=1)
    top_10_df = df.head(10)
    q7=pd.DataFrame({'Winter Games':top_10_df['winter_medals'],'Summer Games':top_10_df['summer_medals']})
    ax=q7.plot.barh(stacked=True,figsize=(10,6),legend=True)
    ax.legend(loc='lower center',bbox_to_anchor=(0.5,-0.2),ncol=2,borderaxespad=3,frameon=False)
    plt.title('Total medals for winter and summer games' )
    plt.show()


def question_8(df):
    print("--------------- question_8 ---------------")
    q8=df.loc[['United States','Australia','Great Britain','Japan','New Zealand'],:]
    q8_bar=pd.DataFrame({'Gold':q8['winter_gold'],'Silver':q8['winter_silver'],'Bronze':q8['winter_bronze']})
    ax = q8_bar.plot.bar(rot=0,legend=True,figsize=(10,6))
    ax.set_xlabel('')
    ax.legend(loc='lower center',bbox_to_anchor=(0.5,-0.2),ncol=3,borderaxespad=3,frameon=False)
    plt.title('Medals for winter games' )
    plt.show()


def question_9(df3):
    df=df3.copy()
    print("--------------- question_9 ---------------")
    df['points_per_participation'] = (df['summer_gold']*5 +df['summer_silver']*3+df['summer_bronze'])/df['summer_participation']
    df = df.sort_values(by='points_per_participation', ascending=False)
    df9=df[['points_per_participation']]
    print(df9[0:5].to_string())
    return df


def question_10(df9):
    print("--------------- question_10 ---------------")
    df=df9.copy()
    df['winter_points'] = (df['winter_gold']*5 +df['winter_silver']*3+df['winter_bronze'])/df['winter_ participation']
    df = df.sort_values(by='winter_points', ascending=False)
    Countinents_df = pd.read_csv('Countries-Continents.csv')
    df_merge = pd.merge(df,Countinents_df,how='left',on='Country')
    Africa_df=df_merge.query('Continent=="Africa"')
    Europe_df=df_merge.query('Continent=="Europe"')
    North_America_df=df_merge.query('Continent=="North America"')
    South_America_df=df_merge.query('Continent=="South America"')
    Asia_df=df_merge.query('Continent=="Asia"')
    Oceania_df=df_merge.query('Continent=="Oceania"')

    ax =df_merge.plot.scatter(x='points_per_participation',y='winter_points',label='Unknown',color='grey',figsize=(10,5))
    ax =Africa_df.plot.scatter(x='points_per_participation',y='winter_points',label='Africa',color='black',ax=ax)
    ax =Europe_df.plot.scatter(x='points_per_participation',y='winter_points',label='Europe',color='blue',ax=ax)
    ax =North_America_df.plot.scatter(x='points_per_participation',y='winter_points',label='North America',color='red',ax=ax)
    ax =South_America_df.plot.scatter(x='points_per_participation',y='winter_points',label='South America',color='orange',ax=ax)
    ax =Asia_df.plot.scatter(x='points_per_participation',y='winter_points',label='Asia',color='yellow',ax=ax)
    ax =Oceania_df.plot.scatter(x='points_per_participation',y='winter_points',label='Oceania',color='green',ax=ax)
    for i in range(0,len(df_merge)):
        ax.annotate(df_merge.iloc[i]['Country'],(df_merge.iloc[i]['points_per_participation'],df_merge.iloc[i]['winter_points']))
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    df1=question_1()
    df2=question_2(df1)
    df3=question_3(df2)
    question_4(df3)
    question_5(df3)
    df6=question_6(df3)
    question_7(df6)
    question_8(df6)
    df9=question_9(df3)
    question_10(df9)