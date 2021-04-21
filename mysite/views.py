import pandas as pd
import requests
import numpy as np
import datetime
import csv
import time
import matplotlib.pyplot as plt
import io
import urllib, base64

from django.shortcuts import render
from mysite.get_data import get_all_user_info
from mysite.model_ml import predict
def button(request):
    return render(request, 'home.html')

def external(request):
	inp = request.POST.get('param')

	def check_bot(data):
	
		bot_count = 0
		real_count = 0

		start_time = time.time()
		all_info = get_all_user_info(data)

		bot_count = all_info.count('banned')
		real_count = all_info.count('verified')
		real_count += all_info.count('private')
		print(len(all_info))
		infos = [i for i in all_info if type(i) != str]
		print(len(infos))
		feature_df = pd.DataFrame(infos)
		# print(feature_df[:20])
		time_df = time.time() 
		print("--- %s seconds ---" % (time_df - start_time))
		# print(feature_df[:20])
		answers = predict(feature_df)
		print("--- %s seconds ---" % (time.time()  - time_df))
		# print(real_count, bot_count)
		real_count += np.sum(answers == 1)
		bot_count += np.sum(answers == 0)
		# print(len([i for i in answers if i != '1' and i != '0']))
		return real_count, bot_count



	real_count, bot_count = check_bot(inp)

	marks = dict()
	marks['real'] = real_count
	marks['bot'] = bot_count

	labels = ['Реальный пользователь', 'Бот']
	men_means = [real_count, bot_count]

	x = np.arange(len(labels))  # the label locations
	width = 0.35  # the width of the bars

	fig, ax = plt.subplots()
	rects1 = ax.bar(x, men_means, width)

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('Количество')
	ax.set_title('Рейтинг группы Вк')
	ax.set_xticks(x)
	ax.set_xticklabels(labels)
	ax.legend()

	ax.bar_label(rects1)

	fig.tight_layout()

	fig = plt.gcf()
	#convert graph into dtring buffer and then we convert 64 bit code into image
	buf = io.BytesIO()
	fig.savefig(buf,format='png')
	buf.seek(0)
	string = base64.b64encode(buf.read())
	uri =  urllib.parse.quote(string)
	return render(request,'image.html',{'data':uri})

	# return render(request,'home.html',{'data1':marks})
