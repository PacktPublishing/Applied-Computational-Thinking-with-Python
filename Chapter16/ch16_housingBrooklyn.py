import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\...\\brooklyn_sales_map.csv')

bins = [-100000000,20000,40000,60000,80000,100000,1000000,10000000,500000000]
ranges_prices = ['$0-$200k','$200k-$400k','$400k-$600k','$600k-$800k','$800k-$1mlln','$1mlln-$10mlln','$10mlln-$100mlln','$100mlln-$500mlln']
df['price_range'] = pd.cut(df['sale_price'], bins = bins, labels = ranges_prices)
def convert(year):
    return df[df['year_of_sale'] == year].groupby('price_range').size()
percent_total = [x/sum(x)*100 for x in [convert(2003),convert(2004),convert(2005),convert(2006),convert(2007),convert(2008),convert(2009),convert(2010),convert(2011),convert(2012),convert(2013),convert(2014),convert(2015),convert(2016),convert(2017)]]
year_names = list(range(2003,2018)


housing_df = pd.DataFrame(percent_total, index = year_names)
ax_two = housing_df.plot(kind = 'barh', stacked = True, width = 0.9, cmap = 'Spectral')
plt.legend(bbox_to_anchor = (1.45, 1), loc='upper right')

ax_two.set_xlabel('Percentages', fontname='Arial', fontsize = 12)
ax_two.set_ylabel('Years', fontname='Arial', fontsize = 12)
ax_two.set_title('Housing Sale ')

df.groupby(['neighborhood','price_range']).size().unstack().plot.bar(stacked = True, cmap = 'rainbow')
plt.legend(bbox_to_anchor = (1.45, 1), loc = 'upper right')
plt.title('Pricing by Neighborhoods in Brooklyn from 2003 to 2017')
plt.ylabel('Price Range')
plt.xticks(fontsize = 6)
