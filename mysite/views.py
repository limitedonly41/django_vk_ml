from django.shortcuts import render
from mysite.get_data import *
from mysite.model_ml import *
def button(request):
    return render(request, 'home.html')

def external(request):
    inp = request.POST.get('param')
# Train the RF classifier


# features={
#        "[IsCity]": 0,
#        "[IsProfile]": 0,
#        "[IsPrivate]": 0,
#        "[IsLinks]": 0,
#        "[IsPhone]": 0,
#        "[FriendCount]": 777,
#        "[PhotoCount]": 1898,
#        "[PagesCount]": 398,
#        "[FollowersCount]": 189,
#        "[AlbumsCount]": 16,
#        "[VideosCount]": 109,
#        "[AudiosCount]": 996,
#        "[UserVideosCount]": 0,
#        "[OfflineDays]": 0,
#        "[HasPhoto]": 1,
#        "[Site]": 0,
#        "[Career]": 0,
#        "[Education]": 0,
#        "[following_followers_ratio]": 4.2769354,
#        "[following_photos_ratio]": 57.6236559,
#        "[followers_photos_ratio]": 13.4731183
# }

# print(train_model.predict(features))
# Driver
    def check_bot(data):
        if(data):
            feature = features(data)
            if feature:
                if feature == "verified" or feature == "private":
                    return 1
                elif feature == "banned":
                    return 0
                elif feature == "mistake":
                    return "Error"
                else:
                    train()
                    return predict(feature)
    acc = train()
    data = check_bot(inp)
    if data == 1:
        data = "Real"
    elif data == 0:
        data = "Bot"
    else:
        data = "Error"
    marks = dict();
    marks['accuracy'] = acc
    marks['bot'] = data
    return render(request,'home.html',{'data1':marks})