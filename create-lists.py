# --------------------------------------------------------------------------------- #
# A code to create private lists on twitter using twitter api. I have written this  #
# code using available python framework "tweepy" for accessing twitter api. You     #
# just need to create your access token and secret keys for this code to work.      #                                                                  
# --------------------------------------------------------------------------------- #

import tweepy
import json
import time
import sys

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = "##########################"
consumer_secret = "##########################"
access_token = "##########################"
access_token_secret = "##########################"

# your twitter handle
screen_nm = "@######"

if __name__ == '__main__':

    # Create authentication token using our details
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Get API handler
    api = tweepy.API(auth)

    # create private list
    fn = sys.argv[1]    # txt filecontaining list of handles passed as an argument 1 
    des = sys.argv[2]   # description for list passed as an argument 2
    cln = fn.split("/")[-1].split(".")[0]   # cleaned list name for the private list to be created
    ln = cln.replace(" ", "-").lower()

    print "creating private list: {}".format(ln)
    api.create_list(cln, "private", des)

    # reading data from txt file
    with open(fn) as f:
        data = f.readlines()

    i = 1
    for d in data:  
        d = d.strip()
        if d:
            # cleaning twitter handle
            if d[0]=="@":
                d = d[1:] 
            n = "@{}".format(d)

            # adding some delay after adding 100 members
            if i==101:
                i = 0
                time.sleep(300)
            # main function call to add members to list
            try:
                print "adding member: {}".format(n) 
                api.add_list_member(screen_name=n, slug=ln, owner_screen_name=screen_nm)
            except Exception, e:
                print (e)
                err = e[0][0]["code"]
                if err == 104:
                    sys.exit()
    
            # delay after adding member to list
            time.sleep(5)
            i = i+1
